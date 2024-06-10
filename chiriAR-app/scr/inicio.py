from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivy.utils import get_color_from_hex
import subprocess

class Inicio(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        # Título de la pantalla
        titulo = Label(
            text="Bienvenido a chiriAR",
            font_size=36,
            bold=True,
            size_hint=(1, 0.2),
            color=get_color_from_hex("#303F9F")
        )
        layout.add_widget(titulo)

        # Botón para escanear QR
        btn_escanear_qr = Button(
            text="Escanear QR",
            size_hint=(1, 0.2),
            font_size=24,
            background_color=get_color_from_hex("#303F9F")
        )
        btn_escanear_qr.bind(on_press=self.abrir_ar_scan_detection)
        layout.add_widget(btn_escanear_qr)

        # Botón para iniciar sesión
        btn_login = Button(
            text="Login",
            size_hint=(1, 0.2),
            font_size=24,
            background_color=get_color_from_hex("#303F9F")
        )
        btn_login.bind(on_press=self.abrir_login)
        layout.add_widget(btn_login)

        # Botón "Acerca de la app"
        btn_about = Button(
            text="Acerca de la app",
            size_hint=(1, 0.2),
            font_size=24,
            background_color=get_color_from_hex("#303F9F")
        )
        btn_about.bind(on_press=self.abrir_info)
        layout.add_widget(btn_about)

        self.add_widget(layout)

    def abrir_ar_scan_detection(self, instance):
        subprocess.Popen(['python', 'ar_scan_detection.py'])

    def abrir_login(self, instance):
        subprocess.Popen(['python', 'login.py'])

    def abrir_info(self, instance):
        app = App.get_running_app()
        app.root.current = 'info'

class ARScanDetection(Screen):
    pass

class Login(Screen):
    pass

class Info(Screen):
    def __init__(self, **kwargs):
        super(Info, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        # Título de la pantalla
        titulo = Label(
            text="Acerca de la App",
            font_size=36,
            bold=True,
            size_hint=(1, 0.2),
            color=get_color_from_hex("#303F9F")
        )
        layout.add_widget(titulo)

        # Descripción de la aplicación
        descripcion = Label(
            text="chiriAR es una aplicación de realidad aumentada diseñada para facilitar la experiencia de los visitantes en museos y exposiciones. Permite escanear códigos QR asociados a artefactos exhibidos para acceder a información detallada, imágenes en 3D y descripciones interactivas. Con chiriAR, los usuarios pueden explorar de manera intuitiva y educativa el contenido de las exposiciones, enriqueciendo su experiencia cultural.",
            font_size=24,
            size_hint=(1, 0.6),
            color=get_color_from_hex("#000000")
        )
        layout.add_widget(descripcion)

        # Botón "Atrás"
        btn_atras = Button(
            text="Atrás",
            size_hint=(1, 0.2),
            font_size=24,
            background_color=get_color_from_hex("#303F9F")
        )
        btn_atras.bind(on_press=self.ir_a_inicio)
        layout.add_widget(btn_atras)

        self.add_widget(layout)

    def ir_a_inicio(self, instance):
        app = App.get_running_app()
        app.root.current = 'inicio'

class ChiriARApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Inicio(name='inicio'))
        sm.add_widget(ARScanDetection(name='ar_scan_detection'))
        sm.add_widget(Login(name='login'))
        sm.add_widget(Info(name='info'))
        return sm

if __name__ == "__main__":
    ChiriARApp().run()
