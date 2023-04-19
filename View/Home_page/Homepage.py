from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from View.Category_Page.CategoryPage import CategoryPage

Builder.load_file('View\Home_page\Homepage.kv')

class Homepage(Screen):

    def __init__(self, **kwargs):
        super(Homepage, self).__init__(**kwargs)
        self.button_id = None
        #self.button_id = button_id


    def on_button_press(self, button_id):
        if button_id == 'cereals_categ':
            print("Cereals category button pressed")
            category_page = CategoryPage(manager=self.manager, button_id='cereals_categ')
            
        elif button_id == 'starchy_categ':
            print("Starchy foods category button pressed")
            category_page = CategoryPage(manager=self.manager, button_id='starchy_categ')

        if not self.manager.has_screen(category_page.name):
            self.manager.add_widget(category_page)

        self.manager.current = category_page.name
          
    def enter_topButton(self, button):
        if button == "Profile":
            self.manager.current = "EditProfilePage"
        elif button == "Save":
            print("Save")
        elif button == "Clear":
            print("Clear")






