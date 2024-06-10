# Importamos las bibliotecas necesarias de Kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from kivy.uix.camera import Camera
from kivy.uix.screenmanager import Screen
import cv2
import cv2.aruco as aruco
import numpy as np
import threading
import os

# Diccionario que relaciona los IDs de los marcadores ARUCO con los nombres de las imágenes
marker_dict = {(0,): "Momia-AncianoChiribaya", (1,): "Vasija_de_Caracol", (2,): "Momia-AncianoChiribaya"}

def findArucoMarkers(img, markerSize=6, totalMarkers=250, draw=True):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    arucoDict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    arucoParam = aruco.DetectorParameters_create()
    bboxs, ids, rejectedImgPoints = aruco.detectMarkers(imgGray, arucoDict, parameters=arucoParam)
    if draw:
        aruco.drawDetectedMarkers(img, bboxs, ids)
    return bboxs, ids

def reproducir_audio(audio_file):
    try:
        os.system(f'start {audio_file}')  # Reproducir archivo de audio
    except Exception as e:
        print(f"Error al reproducir el archivo MP3: {e}")
def augmentAruco(bbox, id, img, imgAug, drawId=True):
    # 1. Extracción de coordenadas delimitadoras del contorno del marcador ARUCO
    tl = bbox[0][0][0], bbox[0][0][1]  # Se extraen las coordenadas de la esquina superior izquierda del contorno
    tr = bbox[0][1][0], bbox[0][1][1]  # Se extraen las coordenadas de la esquina superior derecha del contorno
    br = bbox[0][2][0], bbox[0][2][1]  # Se extraen las coordenadas de la esquina inferior derecha del contorno
    bl = bbox[0][3][0], bbox[0][3][1]  # Se extraen las coordenadas de la esquina inferior izquierda del contorno

    # 2. Obtención de la matriz de homografía
    h, w, c = imgAug.shape
    pts1 = np.array([tl, tr, br, bl])  # Puntos de la imagen superpuesta
    pts2 = np.float32([[0, 0], [w, 0], [w, h], [0, h]])  # Puntos de la imagen original
    matrix, _ = cv2.findHomography(pts2, pts1)  # Se calcula la matriz de homografía para la superposición

    # 3. Superposición de la imagen
    imgOut = cv2.warpPerspective(imgAug, matrix, (img.shape[1], img.shape[0]))  # Se superpone la imagen
    cv2.fillConvexPoly(img, pts1.astype(int), (0, 0, 0))  # Se rellena el contorno del marcador con negro
    imgOut = img + imgOut  # Se combina la imagen superpuesta con la original

    # 4. Dibujo del identificador
    if drawId:
        cv2.putText(imgOut, str(marker_dict[tuple(id)]), (int(tl[0]), int(tl[1] - 10)), cv2.FONT_HERSHEY_PLAIN, 2,
                    (255, 0, 255), 2)# Se dibuja el identificador del marcador

    # 5. Retorno de la imagen resultante
    return imgOut


# Definición de la clase Screen para la pantalla de escaneo QR
class EscanearQR(Screen):
    def __init__(self, **kwargs):
        super(EscanearQR, self).__init__(**kwargs)
        self.cap = cv2.VideoCapture(0)
        self.imgAug = cv2.imread("media/Markers/Momia-AncianoChiribaya.png")

        if self.imgAug is None:
            raise ValueError("No se pudo cargar la imagen de aumento")

        layout = FloatLayout()

        self.camera = Camera(play=True, resolution=(480, 640))
        layout.add_widget(self.camera)
        # Botón "Atrás"
        btn_atras = Button(
            text="Atrás",
            size_hint=(1, 0.2),
            font_size=24,
            #background_color=get_color_from_hex("#303F9F")
        )
        btn_atras.bind(on_press=self.ir_a_inicio)
        layout.add_widget(btn_atras)

        self.add_widget(layout)
        Clock.schedule_interval(self.update, 1.0 / 30)

    def update(self, dt):
        success, img = self.cap.read()
        if not success:
            print("Error al leer la imagen de la cámara")
            return

        bboxs, ids = findArucoMarkers(img)
        if len(bboxs) != 0:
            for bbox, id in zip(bboxs, ids):
                img = augmentAruco(bbox, id, img, self.imgAug, drawId=False)

        img = cv2.flip(img, 0)

        texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='bgr')
        texture.blit_buffer(img.tostring(), colorfmt='bgr', bufferfmt='ubyte')
        self.camera.texture = texture

    def ir_a_inicio(self, instance):
        App.get_running_app().stop()
        #app = App.get_running_app()
        #app.root.current = 'inicio'

    #def atras(self, instance):
     #   app = App.get_running_app()
      #  app.root.current = 'inicio'

    def on_stop(self):
        self.cap.release()

class ChiriARApp(App):
    def build(self):
        return EscanearQR()

if __name__ == "__main__":
    ChiriARApp().run()
