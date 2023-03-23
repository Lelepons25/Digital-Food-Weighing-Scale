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
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.vkeyboard import VKeyboard
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem



# Define the different screen
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
    # Icons for each category
    def buttonIcons(self):
        self.ids.fruits_icon.source = 'icons/fruits.png'
        self.ids.fruits_icon.source = 'icons/vegetable.png'
        self.ids.fruits_icon.source = 'icons/grains.png'
        self.ids.fruits_icon.source = 'icons/protein.png'
        self.ids.fruits_icon.source = 'icons/dairy.png'
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
        self.theme_cls.theme_style = "Dark"
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


    # function that would display the calorie tracker
    def calorieTracker(self):
        current = self.ids.cal_tracker_bar.value
        # Start over after 100
        if current == 1:
            current = 0
        
        # Increment Value by calorie
        # Edit: test : .25
        current += .25
        # Update progress bar
        self.ids.cal_tracker_bar.value = current
        # Update Label
        self.ids.cal_tracker.text = f'{int(current*100)}% Progress'

    def foodList(self):
        for i in range(20):
            item = TwoLineListItem(text = str(i) + ' item',
                                    secondary_text = '2nd ' + str(i) + 'th item')
            self.root.ids.food.add_widget(item)
        
    


if __name__ == '__main__':
    DFWS().run()
