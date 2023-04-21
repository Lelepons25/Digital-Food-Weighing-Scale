from kivy.uix.screenmanager import Screen
from kivymd.uix.list import TwoLineListItem
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
import pandas as pd
import sqlite3
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.button import Button


Builder.load_file('View\Category_Page\CategoryPage.kv')


class CategoryPage(Screen):
    foodList = ObjectProperty(None)

    def __init__(self, manager, button_id, **kwargs):
        super(CategoryPage, self).__init__(**kwargs)
        self.manager = manager
        self.button_id = button_id
        cursor = None
        


        if button_id == 'cereals_categ':
            print('Cereals button pressed!')
            with sqlite3.connect("root_products.db") as conn:
                print('Database connecting...')
                cursor = conn.execute("SELECT foodName FROM ProductsTable")
                data = [str(row[0]) for row in cursor.fetchall()]
                print(data)
                layout = MyLayout(data=data)
                

        elif button_id == 'starchy_categ':
            print('Starchy foods button pressed!')
            with sqlite3.connect("food_mixtures.db") as conn:
                print('Database connecting...')
                cursor = conn.execute("SELECT foodName FROM ProductsTable")
                data = [str(row[0]) for row in cursor.fetchall()]
                print(data)
                layout = MyLayout(data=data)
            

    def on_enter(self, *args):
        food_list = self.ids.foodList
        for child in food_list.children:
            if isinstance(child, Button):
                print(child.text)

    def reset(self):
        self.ids.foodList.clear_widgets()
        self.manager.current = "Homepage"

class MyLayout(GridLayout):
    print("This is Layout Class")

    def __init__(self, data, **kwargs):
        super(MyLayout, self).__init__(**kwargs)   

    def add_buttons(self, data):
        layout = GridLayout(id='foodList', size_hint_y=None, height=500, cols=2, spacing=10, padding=10)

        for text in data:
            layout.add_widget(Button(text=text))

        scroll_view = ScrollView(size=(400, 420), pos_hint={'center_x':0.5, 'center_y':0.5}, do_scroll_x=False, bar_width=10, scroll_type=['bars', 'content'], effect_cls='ScrollEffect')
        scroll_view.add_widget(layout)
        self.add_widget(scroll_view)
            #food.bind(on_press=self.presser)
            
            # print(char)
            # print(self.ids.foodList)
    def presser(self, instance):
        # do something when a button is pressed
        print("Button pressed:", instance.text)

  
    