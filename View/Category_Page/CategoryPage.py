from kivy.uix.screenmanager import Screen
from kivymd.uix.list import TwoLineListItem
from kivy.lang import Builder

Builder.load_file('View\Category_Page\CategoryPage.kv')

class CategoryPage(Screen):
    def foodList(self):
        for i in range(20):
            item = TwoLineListItem(text = str(i) + ' item',
                                    secondary_text = '2nd ' + str(i) + 'th item')
            self.ids.food.add_widget(item)