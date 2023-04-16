from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from View.Category_Page.CategoryPage import CategoryPage

Builder.load_file('View\Home_page\Homepage.kv')
    
class Homepage(Screen):
    # Icons for each category
    def buttonIcons(self):
        self.ids.fruits_icon.source = 'icons/fruits.png'
        self.ids.veg_icon.source = 'icons/vegetable.png'
        self.ids.grains_icon.source = 'icons/grains.png'
        self.ids.protein_icon.source = 'icons/protein.png'
        self.ids.dairy_icon.source = 'icons/dairy.png'
        self.ids.more_icon.source = 'icons/more.png'

    # define the presser function to switch to another screen and print "Pressed"
    #def presser(self, instance):
        #print("Pressed")
        # switch to another screen or page
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
        
    
 
        
    def __init__(self, manager = None, **kwargs):
        self.manager = manager
        super().__init__(**kwargs)

    def enter_EditProfilePage(self):
        self.manager.current = "EditProfilePage"


