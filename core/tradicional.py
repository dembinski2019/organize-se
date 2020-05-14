from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton,MDRaisedButton
from kivymd.uix.picker import MDTimePicker
from kivymd.uix.menu import MDDropdownMenu

class MateriasCadastradas(BoxLayout):
    
    def __init__(self,context={},**kwargs):
        super().__init__(**kwargs)
        self.ids.materia_cadastrada.text = context['materia']
        self.ids.horario_cadastrado.text = context['horario']
    
    

class Content(BoxLayout):
    lista_materias=['Português', 'Matematica', 'Fisica', 'Quimica', 'Biologia']
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        menu_items = [{ "text": f"{i}"} for i in self.lista_materias]
        self.menu = MDDropdownMenu(
            caller=self.ids.drop_item,
            items=menu_items,
            position="bottom",
            callback=self.set_item,
            width_mult=4,
            
        )

    def set_item(self, instance):
        self.materia = instance.text
        self.ids.drop_item.set_item(instance.text)


    def clock(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time)
        time_dialog.open()

    
    def get_time(self, instance, time):
        self.horario = str(time)
        self.ids.time.text = str(time)

    def add_materia(self):
        context = {
            'materia':self.materia,
            'horario':self.horario
        }
        self.ids.box.add_widget(MateriasCadastradas(context))

class Tradicional(Screen):
    def selecionarmaterias(self):
        select = MDDialog(title = 'Cadastrar Materias',
        type="custom",
        content_cls=Content(),
        buttons = [MDRaisedButton(text='OK',md_bg_color=(1, 0, 1, 1)),MDFlatButton(
                        text="CANCEL"
                    )]
        )
        select.ids.container.height='500dp'
        select.ver_growth = 'down'
        return select.open()
    
    