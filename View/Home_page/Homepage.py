from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from View.Category_Page.CategoryPage import CategoryPage
Builder.load_file('View\Home_page\Homepage.kv')
# Register the CategoryPage class

class Homepage(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.weight_input.text = "54"
    

    def enter_topButton(self, button):
        if button == "Profile":
            self.manager.current = "EditProfilePage"
        elif button == "Save":
            print("Save")
        elif button == "Clear":
            print("Clear")






