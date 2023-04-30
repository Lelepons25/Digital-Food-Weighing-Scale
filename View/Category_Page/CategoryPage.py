from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.label import Label
import pandas as pd
import sqlite3
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.metrics import dp
from functools import partial


Builder.load_file('View\Category_Page\CategoryPage.kv')
conn = sqlite3.connect('food_category.db')

class CategoryPage(Screen):
    foodList = ObjectProperty(None)
    
    def __init__(self , table_name, manager = None, **kwargs):
        super(CategoryPage, self).__init__(**kwargs)
        self.manager = manager
        self.ids.weight_input.text = "54"
        self.table_name = table_name
        self.ids.foodList.clear_widgets()
        self.on_enter()
        
        
    def on_enter(self):
        
        self.food_buttons =[] 

        print("ON ENTER PAGE")
        
        # Connect to the database
        c = conn.cursor()

        # Fetch the data from the database
        c.execute(f"SELECT foodName FROM {self.table_name}")
        self.records = c.fetchall()


        self.data = []
        for record in self.records:
            self.data.append(record[:17])

        # Add the buttons to the screen
        for record in self.records:
            food = Button(text=str(record[0]), size_hint_y=None, height='50dp')
            food.bind(on_press=lambda instance, record=record: self.displayFoodValues(instance, record))
            self.ids.foodList.add_widget(food)
            self.food_buttons.append(food)


        # Close the database connection
        c.close()


    def displayFoodValues(self, instance, row_data):
        print(instance.text)
        print(row_data)
        self.ids.food_calories.text = ""
        self.ids.food_fat.text = ""
        self.ids.food_choles.text = ""
        self.ids.food_sodium.text = ""
        self.ids.food_carbo.text = ""
        self.ids.food_protein.text = ""
        self.ids.food_calcium.text = ""
        self.ids.food_iron.text = ""
        offset = self.records.index(row_data)
        c = conn.cursor()
        c.execute(f"SELECT * FROM {self.table_name} LIMIT 1 OFFSET {offset}")
        record = c.fetchone()

        kCal = record[5]
        tFat = record[7]
        chole = record[3]
        sodium = record[16]
        tCarbo = record[8]
        protein = record[6]
        calcium = record[12]
        iron = record[14]

        self.ids.food_calories.text = str(kCal)
        self.ids.food_fat.text = str(tFat)
        self.ids.food_choles.text = str(chole)
        self.ids.food_sodium.text = str(sodium)
        self.ids.food_carbo.text = str(tCarbo)
        self.ids.food_protein.text = str(protein)
        self.ids.food_calcium.text = str(calcium)
        self.ids.food_iron.text = str(iron)

        c.close()
    
    
    def reset(self):
        self.ids.foodList.clear_widgets()
        self.manager.current = "Homepage"
    
    def presser(self, button):
        # do something when a button is pressed
        print("Button pressed:", button.text)

        