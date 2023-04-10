from kivy.uix.screenmanager import Screen
from kivymd.uix.list import TwoLineListItem
from kivy.lang import Builder
from kivy.uix.button import Button

Builder.load_file('View\Category_Page\CategoryPage.kv')

class CategoryPage(Screen):
    # Edit: Di mudisplay ang list
    def on_pre_enter(self, *args):
        for i in range(0, 100):
            foodList = Button(text = str(i+1), 
                       size_hint_y = (None),
                       size = ("50dp", "50dp"))
            self.ids.food.add_widget(foodList)
    
    def reset(self):
        self.ids.food.clear_widgets()
        self.manager.current = "Homepage"