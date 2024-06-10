from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.lang import Builder


class InicioAdminScreen(Screen):
    pass


class AdminUsuariosScreen(Screen):
    pass


class AdminArtefactosScreen(Screen):
    pass


class ChiriARApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.accent_palette = 'Blue'

        Builder.load_string('''
ScreenManager:
    InicioAdminScreen:
    AdminUsuariosScreen:
    AdminArtefactosScreen:

<InicioAdminScreen>:
    name: 'inicio_admin'
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

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
        ''')

        return InicioAdminScreen()


if __name__ == '__main__':
    ChiriARApp().run()
