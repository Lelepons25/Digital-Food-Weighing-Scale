from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


Builder.load_file('View\Home_page\Homepage.kv')

class Homepage(Screen):
    # Icons for each category

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def createFruit(self, instance):
        print("Inside")
        # self.ids.wm.current = "CategoryPage"
       

    def buttonIcons(self):
        self.ids.fruits_icon.source = 'icons/fruits.png'
        self.ids.veg_icon.source = 'icons/vegetable.png'
        self.ids.grains_icon.source = 'icons/grains.png'
        self.ids.protein_icon.source = 'icons/protein.png'
        self.ids.dairy_icon.source = 'icons/dairy.png'
        self.ids.more_icon.source = 'icons/more.png'


