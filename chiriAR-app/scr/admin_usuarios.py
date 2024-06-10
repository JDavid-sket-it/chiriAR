from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.lang import Builder


class AdminUsuariosScreen(Screen):
    pass


class ChiriARApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.accent_palette = 'Blue'

        Builder.load_string('''
ScreenManager:
    AdminUsuariosScreen:

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
        ''')

        return AdminUsuariosScreen()


if __name__ == '__main__':
    ChiriARApp().run()
