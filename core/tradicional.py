from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton

class Content(BoxLayout):
    pass

class Tradicional(Screen):
    def selecionarmaterias(self):
        select = MDDialog(title = 'dialogo',
        type="custom",
        content_cls=Content(),
        buttons = [MDFlatButton(
                        text="CANCEL"
                    )])
        return select.open()




