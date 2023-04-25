from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.label import Label
import pandas as pd
import sqlite3
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRectangleFlatButton
from kivy.metrics import dp
from functools import partial

Builder.load_file('View\Category_Page\CategoryPage.kv')


class CategoryPage(Screen):
    #foodList = ObjectProperty(None)
    
    def __init__(self, manager, **kwargs):
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
<<<<<<< HEAD
        print(records)
        c.close()
        conn.close()
        #buttons = []
        #word =[tuple(row) for row in rows]
        for record in records:
            #word = record[0]
            food = Button(text = str(record[0]), 
                    size_hint_y = 0.5,
                    size = ("50dp", "50dp"))
            food.bind(on_press = self.displayCerealValues)
            #self.food_buttons.append(foodList)
            self.ids.foodList.add_widget(food)
            #buttons.append(food)
            print(type(record[0]))
            print(record[0])
            print(food)

        


    def display_starchy_buttons(self):
       # self.ids.foodList.clear_widgets()
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
=======
        
        
        layout = FloatLayout(size_hint_y=None, height=dp(40*10), pos_hint = {"center_x": 0.5, "top": 0.96} )
        y_value = 0.6 # initialize y value
        for record in records:
            food = MDRectangleFlatButton(
                id=f'{record}',
                text= str(record[0]),
                size_hint=(0.8, None),
                height=dp(40),
                text_color="black",
                line_color="red",
                pos_hint={"center_x": 0.5, "top": y_value},
                padding=(0, 0, 10, 0)
            )
            layout.add_widget(food)
            y_value -= 0.1 # decrease y value for next button
            
        # Add the layout to a scrollview
        scrollview = ScrollView(size_hint=(None, None), size = (400, 280))
        scrollview.add_widget(layout)
        self.ids.card_foodList.add_widget(scrollview)
>>>>>>> 85311403ff72b5bdac34a45f2fdb744778e08c20

    def displayCerealValues(self, instance):
        foodClicked = instance.text



    def reset(self):
        self.ids.foodList.clear_widgets()
        self.manager.current = "Homepage"
    
    def presser(self, button):
        # do something when a button is pressed
        print("Button pressed:", button.text)