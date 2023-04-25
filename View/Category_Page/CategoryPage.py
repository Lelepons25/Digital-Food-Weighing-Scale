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
    #foodList = ObjectProperty(None)
    
    def __init__(self, manager = None, **kwargs):
        super(CategoryPage, self).__init__(**kwargs)
        self.manager = manager
        self.ids.weight_input.text = "54"

       
    def display_cereals_buttons(self):
        #remove buttons
        print('CATEG: Cereals button pressed!')
        conn =sqlite3.connect('root_products.db')
        c = conn.cursor()
        c.execute("SELECT foodName FROM ProductsTable")
        records = c.fetchall()
        print(records)
        buttons = []
        #word =[tuple(row) for row in rows]
        for record in records:
            #word = record[0]
            food = Button(text = str(record[0]), 
                    size_hint_y = (None),
                    size = ("50dp", "50dp"))
            food.bind(on_press = self.displayCerealValues)
            #self.food_buttons.append(foodList)
            self.ids.foodList.add_widget(food)
            #buttons.append(food)
            print(type(record[0]))
            print(record[0])
            print(food)

        c.close()
        conn.close()


    def display_starchy_buttons(self):
        self.ids.foodList.clear_widgets()
        print('CATEG: Starchy foods button pressed!')
        conn=sqlite3.connect('food_mixtures.db')
        c = conn.cursor()
        c.execute("SELECT foodName FROM ProductsTable")
        records = c.fetchall()
        buttons = []

        for record in records:
            #word = record[0]
            food = Button(text = str(record[0]), 
                    size_hint_y = (None),
                    size = ("50dp", "50dp"))
            food.bind(on_press = self.presser)
            #self.food_buttons.append(foodList)
            self.ids.foodList.add_widget(food)
            #buttons.append(food)
            print(type(record[0]))
            print(record[0])
            print(food)

        c.close()
        conn.close()

    def displayCerealValues(self, instance):
        foodClicked = instance.text



    def reset(self):
        self.ids.foodList.clear_widgets()
        self.manager.current = "Homepage"
    
    def presser(self, button):
        # do something when a button is pressed
        print("Button pressed:", button.text)