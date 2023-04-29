from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from View.Category_Page.CategoryPage import CategoryPage

Builder.load_file('View\Home_page\Homepage.kv')

class Homepage(Screen):

    def __init__(self, **kwargs):
        super(Homepage, self).__init__(**kwargs)
        self.button_id = ''
        self.ids.weight_input.text = "54"
        category_page = CategoryPage(manager=self.manager, button_id="")
    def on_button_press(self, button_id):
        
        if button_id == "cereals_categ":
            print("HOME: Cereals category button pressed")
            category_page = CategoryPage(manager=self.manager, button_id="cereals_categ")
            #category_page.display_cereals_buttons()
            self.manager.current = "CategoryPage"
            
        elif button_id == "starchy_categ":
            print("HOME: Starchy foods category button pressed")
            category_page = CategoryPage(manager=self.manager, button_id="starchy_categ")
            self.manager.current = "CategoryPage"
        
        
        
        
    def enter_topButton(self, button):
        if button == "Profile":
            self.manager.current = "EditProfilePage"
        elif button == "Save":
            print("Save")
        elif button == "Clear":
            print("Clear")






