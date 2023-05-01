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
from View.MealPlan_Page.MealPlanPage import MealPlanPage
from View.Profile_Page.ProfilePage import ProfilePage
from View.EditProfile_Page.EditProfilePage import EditProfilePage
from View.More_Page.MorePage import MorePage

from database import DataBase


Builder.load_file("dfwsv2.kv")

class WindowManager(ScreenManager):
    

    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)
        
        db = DataBase("users.txt")
        if os.path.getsize(db.file_path) == 0:
            self.current = "ProfilePage"
        else:
            print("Check")
            # Create a new instance of the Homepage class
            self.Homepage_widget = Homepage(manager = self)
            # Add the Homepage widget to the ScreenManager
            self.ids.Homepage.add_widget(self.Homepage_widget)
            # Set the current screen to the Homepage
            self.current = "Homepage"
            
        self.MealPlanPage_widget = MealPlanPage(manager = self)
        self.ProfilePage_widget = ProfilePage(manager = self)
        self.MorePage_widget = MorePage(manager = self)

        self.ids.MealPlanPage.add_widget(self.MealPlanPage_widget)
        self.ids.ProfilePage.add_widget(self.ProfilePage_widget)
        self.ids.MorePage.add_widget(self.MorePage_widget)

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


    def generateCategoryPageScreen(self, table_name):
         # Remove the CategoryPage widget if it already exists
        if hasattr(self, 'CategoryPage_widget'):
            self.ids.CategoryPage.remove_widget(self.CategoryPage_widget)
        # Create a new instance of the CategoryPage class with the specified category
        self.CategoryPage_widget = CategoryPage(manager=self, table_name=table_name)
        # Add the CategoryPage widget to the ScreenManager
        self.ids.CategoryPage.add_widget(self.CategoryPage_widget)
        # Switch to the CategoryPage screen
        self.current = "CategoryPage"


class DFWS(MDApp):
    progress_value = NumericProperty(0)
    
    def on_start(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

    def build(self):      
        return WindowManager()
    
    def update_progress_value(self, value):
        # Update the progress value and save it to the global variable
        self.progress_value = value
        

    def get_progress_value(self):
        # Retrieve the progress value from the global variable
        return self.progress_value




DFWS().run()