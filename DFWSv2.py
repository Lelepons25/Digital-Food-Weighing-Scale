from kivy.config import Config
# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', '0')
# fix the width of the window   
Config.set('graphics', 'width', '800')
# fix the height of the window
Config.set('graphics', 'height', '420')


from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.vkeyboard import VKeyboard
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem
from kivy.properties import ObjectProperty, DictProperty
from database import DataBase # for Login (Test Only)
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock
import mysql.connector
import pandas as pd
import sqlite3

conn = sqlite3.connect("food_mixtures.db")
cur = conn.cursor()

for row in cur.execute("SELECT * from FoodMixturesTable"):
    print(row)


# Define the different screen
class CategoryPage(Screen):

    # db input
    # food_name = ObjectProperty(None)
    # common_name = ObjectProperty(None)

    def createFoodList(self):
        pass

    # Edit: Di mudisplay ang list
    def foodList(self):
        for i in range(20):
            item = TwoLineListItem(text = str(i) + ' item',
                                    secondary_text = '2nd ' + str(i) + 'th item')
            self.root.ids.food.add_widget(item)

class MorePage(Screen):
    pass

class Homepage(Screen):
    # Icons for each category
    def buttonIcons(self):
        self.ids.fruits_icon.source = 'icons/fruits.png'
        self.ids.veg_icon.source = 'icons/vegetable.png'
        self.ids.grains_icon.source = 'icons/grains.png'
        self.ids.protein_icon.source = 'icons/protein.png'
        self.ids.dairy_icon.source = 'icons/dairy.png'
        self.ids.more_icon.source = 'icons/more.png'
    
 
class ProfilePage(Screen):
    user_name = ObjectProperty(None)
    sex = ObjectProperty(None)
    age = ObjectProperty(None)
    user_weight = ObjectProperty(None)
    user_height = ObjectProperty(None)

    # Add info of the user

    def saveProfile(self):
        if self.user_name.text != "" and self.sex.text != "" and self.age.text != "":
            if self.user_weight.text != "" and self.user_height.text != "":
                db.add_user(self.user_name.text,
                            self.sex.text,
                            self.age.text,
                            self.user_weight.text,
                            self.user_height.text)
                self.reset()
                self.manager.current = "Homepage"
            else:
                invalidForm()
        else:
            invalidForm()
    
    def reset(self):
        self.user_name.text = ""
        self.sex.text = ""
        self.age.text = ""
        self.user_weight.text = ""
        self.user_height.text = ""
                
class MealPlanPage(Screen):
    pass

class EditProfilePage(Screen):
    pass

class SplashScreenPage(Screen):
    pass

class WindowManager(ScreenManager):
    pass

def invalidForm():
    pop = Popup(title = " Invalid Form ",
        content = Label (text = "Fill in with valid information"),
        size_hint = (None, None),
        size = (400, 400)
    )
    pop.open()


db = DataBase("users.txt")

global sm
sm = ScreenManager()

screens = [SplashScreenPage (name = "SplashScreenPage"),
        ProfilePage (name = "ProfilePage"),
        Homepage (name = "Homepage"),
        MealPlanPage (name = "MealPlanPage"),
        EditProfilePage (name = "EditProfilePage"),
        CategoryPage (name = "EditCategoryPage"),
        MorePage (name = "MorePage")]

for screen in screens:
    sm.add_widget(screen)

class DFWS(MDApp):

    global sm
    sm = ScreenManager()

    screens = [SplashScreenPage (name = "SplashScreenPage"),
           ProfilePage (name = "ProfilePage"),
           Homepage (name = "Homepage"),
           MealPlanPage (name = "MealPlanPage"),
           EditProfilePage (name = "EditProfilePage"),
           CategoryPage (name = "EditCategoryPage"),
           MorePage (name = "MorePage")]

    for screen in screens:
        sm.add_widget(screen)

    data = DictProperty()

    def floatButton(self):
        self.data = {
            'Create Meal': 'food'
        } 

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        kv = Builder.load_file('dfws.kv')   
        return kv
    
    def on_start(self):
        # Delay time for splash screen before main screen
        Clock.schedule_once(self.change_screen, 5)
    
    def change_screen(self, dt):
        sm.current = "Homepage"


    # function that will display the weight
    def computeWeight(self, weight):
        if( weight < 0):
            weight = weight * (-1)
        elif( weight >= 10000):
            weight = 0

    weight = 10
    # function that would display the food weight 
    def displayWeight(self, weight):
        self.ids.weight_input.text = weight
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
            


if __name__ == '__main__':
    DFWS().run()

conn.close()