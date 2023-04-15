from kivy.uix.screenmanager import Screen
from kivymd.uix.list import TwoLineListItem
from kivy.lang import Builder
from kivy.uix.button import Button

import pandas as pd
import sqlite3
#import ConnectDB

Builder.load_file('View\Category_Page\CategoryPage.kv')

conn = sqlite3.connect('food_mixtures.db')
#conn = ConnectDB.connectFoodMix()

class CategoryPage(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # check if the button is pressed
        def presser(self):
            print("Pressed")

        cursor = conn.execute("SELECT foodName FROM FoodMixturesTable")

        data = []
        
        for row in cursor:
            data.append(row[0])

        for item in data:
            foodList = Button(text = item, 
                    size_hint_y = (None),
                    size = ("50dp", "50dp"))
            foodList.bind(on_press = presser)
            self.ids.foodList.add_widget(foodList)

        cursor.close()
        conn.close()
            
    def reset(self):
        self.ids.food.clear_widgets()
        self.manager.current = "Homepage"