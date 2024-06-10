# Importación de las bibliotecas necesarias
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window

# Establecer el tamaño de la ventana de la aplicación
Window.size = (300, 450)

# Definición del diseño de la interfaz de usuario utilizando el lenguaje KV
KV = '''
ScreenManager:
    LoginScreen:
    InicioAdminScreen:
    AdminUsuariosScreen:
    AdminArtefactosScreen:

<LoginScreen>:
    name: 'login'
    MDCard:
        size_hint: None, None
        size: 300, 450
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
        padding: 65
        spacing: 35
        orientation: 'vertical'

        MDIcon:
            icon: "account"
            icon_color: 0, 0, 0, 1
            halign: "center"
            font_size: 180

        MDTextField:
            id: user
            hint_text: "Username"
            icon_left: "account-check"
            mode: "rectangle"
            size_hint_x: None
            width: 220
            font_size: 20
            pos_hint: {"center_x": 0.5}

        MDTextField:
            id: password
            hint_text: "Password"
            icon_left: "key-variant"
            mode: "rectangle"
            size_hint_x: None
            width: 220
            font_size: 20
            pos_hint: {"center_x": 0.5}
            password: True

        MDFillRoundFlatButton:
            text: "LOG IN"
            font_size: 15
            pos_hint: {"center_x": 0.5}
            on_press: app.login()
            
        MDFillRoundFlatButton:
            text: "Volver"
            pos_hint: {"center_x": 0.5}
            on_release: app.root.current = 'inicio'

<InicioAdminScreen>:
    name: 'inicio_admin'
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)

        MDLabel:
            text: "Panel de Administración"
            halign: "center"
            font_style: "H4"
            size_hint_y: None
            height: self.texture_size[1]

        MDFillRoundFlatButton:
            text: "Administrar Usuarios"
            pos_hint: {"center_x": 0.5}
            on_release: app.root.current = 'admin_usuarios'

        MDFillRoundFlatButton:
            text: "Administrar Artefactos"
            pos_hint: {"center_x": 0.5}
            on_release: app.root.current = 'admin_artefactos'

        MDFillRoundFlatButton:
            text: "Cerrar Sesión"
            pos_hint: {"center_x": 0.5}
            on_release: app.logout()

<AdminUsuariosScreen>:
    name: 'admin_usuarios'
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)

        MDLabel:
            text: "Administrar Usuarios"
            halign: "center"
            font_style: "H4"
            size_hint_y: None
            height: self.texture_size[1]

        MDFillRoundFlatButton:
            text: "Volver"
            pos_hint: {"center_x": 0.5}
            on_release: app.root.current = 'inicio_admin'

<AdminArtefactosScreen>:
    name: 'admin_artefactos'
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)

        MDLabel:
            text: "Administrar Artefactos"
            halign: "center"
            font_style: "H4"
            size_hint_y: None
            height: self.texture_size[1]

        MDFillRoundFlatButton:
            text: "Volver"
            pos_hint: {"center_x": 0.5}
            on_release: app.root.current = 'inicio_admin'
        '''

# Definición de las pantallas de la aplicación
class LoginScreen(Screen):
    pass

class InicioAdminScreen(Screen):
    pass

class AdminUsuariosScreen(Screen):
    pass

class AdminArtefactosScreen(Screen):
    pass

# Definición de la clase principal de la aplicación
class ChiriARApp(MDApp):
    # Inicialización de la variable de diálogo como nula
    dialog = None

    # Método para construir la aplicación
    def build(self):
        # Configuración del tema de la aplicación
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.accent_palette = 'Blue'
        # Carga de la interfaz de usuario desde la cadena KV
        return Builder.load_string(KV)

    # Método para el inicio de sesión
    def login(self):
        # Obtención de los valores de usuario y contraseña ingresados
        user_text = self.root.get_screen('login').ids.user.text
        password_text = self.root.get_screen('login').ids.password.text

        # Verificación de las credenciales ingresadas
        if user_text == '+zt' and password_text == '+zt':
            # Cambio de la pantalla actual a la pantalla de inicio de administración
            self.root.current = 'inicio_admin'
        else:
            # Mostrar un diálogo de error si las credenciales son incorrectas
            if not self.dialog:
                self.dialog = MDDialog(
                    title='Login',
                    text='Usuario o contraseña incorrecta',
                    buttons=[
                        MDFlatButton(
                            text="Ok",
                            text_color=self.theme_cls.accent_color,
                            on_release=self.close_dialog
                        ),
                    ],
                )
            self.dialog.open()

    # Método para cerrar el diálogo de error
    def close_dialog(self, *args):
        self.dialog.dismiss()

    # Método para cerrar sesión
    def logout(self):
        # Cambio de la pantalla actual a la pantalla de inicio de sesión
        self.root.current = 'login'

# Ejecución de la aplicación si se ejecuta este script directamente
if __name__ == '__main__':
    ChiriARApp().run()
