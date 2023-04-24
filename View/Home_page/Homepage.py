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
        self.category_page = CategoryPage()



    def on_button_press(self, button_id):
        if button_id == 'cereals_categ':
            print("HOME: Cereals category button pressed")
            self.category_page.display_cereals_buttons()
            
            
        elif button_id == 'starchy_categ':
            print("HOME: Starchy foods category button pressed")
            self.category_page.display_starchy_buttons()
        
          
    def enter_topButton(self, button):
        if button == "Profile":
            self.manager.current = "EditProfilePage"
        elif button == "Save":
            print("Save")
        elif button == "Clear":
            print("Clear")






