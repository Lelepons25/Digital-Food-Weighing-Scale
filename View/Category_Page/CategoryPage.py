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
from functools import partial

Builder.load_file('View\Category_Page\CategoryPage.kv')


class CategoryPage(Screen):
    def __init__(self, manager, button_id, **kwargs):
        super(CategoryPage, self).__init__(**kwargs)
        self.manager = manager
        self.button_id = button_id
        self.grid_layout = self.ids.foodList
        self.grid_layout.bind(minimum_height=self.grid_layout.setter('height'))
        word = ''
        if self.button_id == 'cereals_categ':
            print('Cereals button pressed!')
            conn =sqlite3.connect('root_products.db')
            c = conn.cursor()
            c.execute("SELECT foodName FROM ProductsTable")
            records = c.fetchall()
            print(records)
            c.close()
            #word =[tuple(row) for row in rows]
            for record in records:
                word = record[0]
                print(word)
                food = Button(text=', '.join(list(word)), size_hint_y = (None),
                        size = ("50dp", "100dp"))
                print(type(word))
                self.ids.foodList.bind(on_press=partial(presser, self))
                self.ids.foodList.add_widget(food)

            
        elif self.button_id == 'starchy_categ':
            print('Starchy foods button pressed!')
            with sqlite3.connect('food_mixtures.db') as conn:
                c = conn.cursor()
                c.execute("SELECT foodName FROM ProductsTable")
                records = c.fetchall()

                for record in records:
                    word=record[0]
                    food = Button(text=word, size_hint_y=None, height='50dp')
                    food.bind(on_press=self.presser)
                    self.grid_layout.add_widget(food)
        

    def reset(self):
        self.ids.foodList.clear_widgets()
        self.manager.current = "Homepage"
    
def presser(self, button):
    # do something when a button is pressed
    print("Button pressed:", button.text)