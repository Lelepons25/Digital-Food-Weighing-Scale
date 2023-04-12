from kivy.config import Config
# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', '0')
# fix the width of the window   
Config.set('graphics', 'width', '800')
# fix the height of the window
Config.set('graphics', 'height', '420')


from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
# from View.Manager_Screen.ManagerScreen import ManagerScreen

# import

from View.Category_Page.CategoryPage import CategoryPage

class WindowManager(ScreenManager):

    def on_pre_enter(self, *args):
        self.categoryPage_widget = CategoryPage()
        self.ids.CategoryPage.add_widget(self.categoryPage_widget)



class DFWS(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

    def build(self):    
        return WindowManager()
        """self.manager_screen = ManagerScreen()

    def on_current(self, *args):
        super().on_current(*args)

    def build(self) -> ManagerScreen:
        self.manager_screen.add_widget(self.manager_screen.create_screen("Profile"))
        return self.manager_screen"""


DFWS().run()
