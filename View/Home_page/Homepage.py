from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from View.Category_Page.CategoryPage import CategoryPage

Builder.load_file('View\Home_page\Homepage.kv')

class Homepage(Screen):

    def __init__(self, manager = None, **kwargs):
        self.manager = manager
        super().__init__(**kwargs)

    def on_button_press(self, button_id):
        if button_id == 'cereals_categ':
            button = 'cereals_categ'
            print("Cereals category button pressed")
            category_page=CategoryPage()
            category_page.show_categorypage(button)
        elif button_id == 'starchy_categ':
            button = 'starchy_categ'
            print("Starchy foods category button pressed")
            category_page=CategoryPage()
            category_page.show_categorypage(button)
        
        self.manager.current = 'CategoryPage'
          
    def enter_topButton(self, button):
        if button == "Profile":
            self.manager.current = "EditProfilePage"
        elif button == "Save":
            print("Save")
        elif button == "Clear":
            print("Clear")






