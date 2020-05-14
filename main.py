from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from core.planodeestudo import PlanoDeEstudo
from core.organizese import OrganizeSe
from core.tradicional import Tradicional

class Manager(ScreenManager):
    def transicao(self,*args):
        self.transition.direction = args[1]
        self.current=args[0]
    
   

class Main(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = 'A400'
        self.theme_cls.accent_palette = 'Blue'

Main().run()