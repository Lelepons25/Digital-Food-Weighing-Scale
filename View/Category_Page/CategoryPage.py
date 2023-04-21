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
    
    def presser(self, instance):
        # do something when a button is pressed
        print("Button pressed:", instance.text)

    def __init__(self, manager, button_id, **kwargs):
        super(CategoryPage, self).__init__(**kwargs)
        self.manager = manager
        self.button_id = button_id
        cursor = None
        data = []

        if button_id == 'cereals_categ':
            print('Cereals button pressed!')
            with sqlite3.connect("root_products.db") as conn:
                print('Database connecting...')
                cursor = conn.execute("SELECT foodName FROM ProductsTable")
                data = [str(row[0]) for row in cursor.fetchall()]

        elif button_id == 'starchy_categ':
            print('Starchy foods button pressed!')
            with sqlite3.connect("food_mixtures.db") as conn:
                print('Database connecting...')
                cursor = conn.execute("SELECT foodName FROM ProductsTable")
                data = [str(row[0]) for row in cursor.fetchall()]
                    
        print(data)
        for char in data:
            food = Button(text= char, 
                        size_hint_y=0.2,
                        height="50dp")
            food.bind(on_press=self.presser)
            self.ids.foodList.add_widget(food)
            #print(char)
            #print(self.ids.foodList)

    def reset(self):
        self.ids.foodList.clear_widgets()
        self.manager.current = "Homepage"
    


class CategoryButton(Button):
    pass