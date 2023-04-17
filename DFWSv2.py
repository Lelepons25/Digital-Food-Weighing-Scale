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
from kivy.properties import StringProperty

# import
from View.Home_page.Homepage import Homepage
from View.Category_Page.CategoryPage import CategoryPage
from View.MealPlan_Page.MealPlanPage import MealPlanPage
from View.Profile_Page.ProfilePage import ProfilePage
from View.EditProfile_Page.EditProfilePage import EditProfilePage
from View.More_Page.MorePage import MorePage

from database import DataBase


Builder.load_file("dfwsv2.kv")

class WindowManager(ScreenManager):
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        user = StringProperty("None")
        
        db = DataBase("users.txt")
        if os.path.getsize(db.file_path) == 0:
            self.current = "ProfilePage"
        else:
            self.current ="Homepage"
            
        self.Homepage_widget = Homepage(manager = self)
        self.CategoryPage_widget = CategoryPage(manager = self)
        self.MealPlanPage_widget = MealPlanPage(manager = self)
        self.ProfilePage_widget = ProfilePage(manager = self, user = user)
        self.EditProfilePage_widget = EditProfilePage(manager = self)
        self.MorePage_widget = MorePage(manager = self)

        self.ids.Homepage.add_widget(self.Homepage_widget)
        self.ids.CategoryPage.add_widget(self.CategoryPage_widget)
        self.ids.MealPlanPage.add_widget(self.MealPlanPage_widget)
        self.ids.ProfilePage.add_widget(self.ProfilePage_widget)
        self.ids.EditProfilePage.add_widget(self.EditProfilePage_widget)
        self.ids.MorePage.add_widget(self.MorePage_widget)

class DFWS(MDApp):

    def on_start(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

    def build(self):    
        return WindowManager()



DFWS().run()