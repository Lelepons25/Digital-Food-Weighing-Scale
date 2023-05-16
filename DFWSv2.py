from kivy.config import Config
# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', '0')
# fix the width of the window   
Config.set('graphics', 'width', '800')
# fix the height of the window
Config.set('graphics', 'height', '420')

import os
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, NumericProperty

# import
from View.Home_page.Homepage import Homepage
from View.Category_Page.CategoryPage import CategoryPage
from View.Profile_Page.ProfilePage import ProfilePage
from View.EditProfile_Page.EditProfilePage import EditProfilePage
from View.More_Page.MorePage import MorePage
from View.Help_Page.HelpPage import HelpPage
from View.FoodHistory_Page.FoodHistoryPage import FoodHistoryPage

import datetime

import sqlite3

Builder.load_file("dfwsv2.kv")

class WindowManager(ScreenManager):
    weight_text = StringProperty("0")

    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)

        conn = sqlite3.connect('user_database/userDB.db')
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM user")
        count = cursor.fetchone()

        if count[0] == 0:
            self.generateProfilePageScreen()
        else:
            self.generateHomePageScreen()
            
    def generateMorePageScreen(self):
        if hasattr(self, 'MorePage_widget'):
            self.ids.MorePage.remove_widget(self.MorePage_widget)
        self.MorePage_widget = MorePage(manager = self)
        self.ids.MorePage.add_widget(self.MorePage_widget)
        self.current = "MorePage"

    def generateProfilePageScreen(self):
        if hasattr(self, 'ProfilePage_widget'):
            self.ids.ProfilePage.remove_widget(self.ProfilePage_widget)
        self.ProfilePage_widget = ProfilePage(manager=self)
        self.ids.ProfilePage.add_widget(self.ProfilePage_widget)
        self.current = "ProfilePage"

    def generateHomePageScreen(self):
        if hasattr(self, 'Homepage_widget'):
            self.ids.Homepage.remove_widget(self.Homepage_widget)
        self.Homepage_widget = Homepage(manager=self)
        self.ids.Homepage.add_widget(self.Homepage_widget)
        self.current = "Homepage"

      
    def generateEditProfilePageScreen(self):
        if hasattr(self, 'EditProfilePage_widget'):
            self.ids.EditProfilePage.remove_widget(self.EditProfilePage_widget)
        self.EditProfilePage_widget = EditProfilePage(manager=self)
        self.ids.EditProfilePage.add_widget(self.EditProfilePage_widget)
        self.current = "EditProfilePage"


    def generateHelpPageScreen(self):
        if hasattr(self, 'HelpPage_widget'):
            self.ids.HelpPage.remove_widget(self.HelpPage_widget)
        self.HelpPage_widget = HelpPage(manager=self)
        self.ids.HelpPage.add_widget(self.HelpPage_widget)
        self.current = "HelpPage"
    
    
    def generateFoodHistoryPageScreen(self):
        if hasattr(self, 'FoodHistoryPage_widget'):
            self.ids.FoodHistoryPage.remove_widget(self.FoodHistoryPage_widget)
        self.FoodHistoryPage_widget = FoodHistoryPage(manager=self)
        self.ids.FoodHistoryPage.add_widget(self.FoodHistoryPage_widget)
        self.current = "FoodHistoryPage"


    def generateCategoryPageScreen(self, databaseName):
        if hasattr(self, 'CategoryPage_widget'):
            self.ids.CategoryPage.remove_widget(self.CategoryPage_widget)
        # now_date = datetime.date.today().strftime("%Y%m%d")
        self.CategoryPage_widget = CategoryPage(manager=self, databaseName= databaseName)
        self.ids.CategoryPage.add_widget(self.CategoryPage_widget)
        self.current = "CategoryPage"
    
class DFWS(MDApp):

    def on_start(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

    def build(self):     
    
        return WindowManager()
    
    




DFWS().run()