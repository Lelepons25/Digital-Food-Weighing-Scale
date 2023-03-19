from kivy.config import Config
# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', '0')
# fix the width of the window
Config.set('graphics', 'width', '800')
# fix the height of the window
Config.set('graphics', 'height', '420')


import kivy

from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.vkeyboard import VKeyboard




# Define the different screens
class FruitsPage(Screen):
    pass

class VegPage(Screen):
    pass

class GrainsPage(Screen):
    pass

class ProteinPage(Screen):
    pass

class DairyPage(Screen):
    pass

class MorePage(Screen):
    pass

class Homepage(Screen):
    pass

class ProfilePage(Screen):
    pass

class AccountPage(Screen):
    pass

class MealPlanPage(Screen):
    pass

class WindowManager(ScreenManager):
    pass



class DFWS(MDApp):

        
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file('design3.kv') 
    
    # function that will display the weight
    def computeWeight(self, weight):

        if( weight < 0):
            weight = weight * (-1)
        elif( weight >= 10000):
            weight = 0

    # function that would display the food weight
    def displayWeight(self, weight):
        foodWeight = self.ids.weight_input.text


if __name__ == '__main__':
    DFWS().run()
