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
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock
import pandas as pd
import sqlite3
from kivy.uix.boxlayout import BoxLayout


from View.Profile_Page import ProfilePage
from View.Home_page import Homepage
from View.Category_Page import CategoryPage
from View.EditProfile_Page import EditProfilePage
from View.MealPlan_Page import MealPlanPage
from View.More_Page import MorePage
from View.SplashScreen_Page import SplashScreenPage



class WindowManager(BoxLayout):
    
    ProfilePage_widget = ProfilePage()
    Homepage_widget = Homepage()
    CategoryPage_widget = CategoryPage()
    EditProfilePage_widget = EditProfilePage()
    MealPlanPage_widget = MealPlanPage()
    MorePage_widget = MorePage()
    SplashScreenPage_widget = SplashScreenPage()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.ProfilePage.add_widget(self.ProfilePage_widget)
        self.ids.Homepage.add_widget(self.Homepage_widget)
        self.ids.CategoryPage.add_widget(self.CategoryPage_widget)
        self.ids.EditProfilePage.add_widget(self.EditProfilePage_widget)
        self.ids.MealPlanPage.add_widget(self.MealPlanPage_widget)
        self.ids.MorePage.add_widget(self.MorePage_widget)
        self.ids.SplashScreenpage.add_widget(self.SplashScreenPage_widget)

class DFWS(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return WindowManager()
            


if __name__ == '__main__':
    DFWS().run()
