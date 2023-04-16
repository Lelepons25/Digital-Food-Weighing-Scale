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
#from ConnectDatabase import connect_CerealsDB, connectFoodMix

Builder.load_file('View\Category_Page\CategoryPage.kv')

#conn = ConnectDB.connectFoodMix()
#DOUBLE CHECK DATABASE AGAIN
class CategoryPage(Screen):
    
    def presser(self, instance):
        # do something when a button is pressed
        print("Button pressed:", instance.text)

    def show_categorypage(self, button):
        # do something with the button
        #cursor = None 
    
        print("Button pressed:", button)
        cursor = None
        data =[]
        if button == 'cereals_categ':
            print('Cereals button pressed!')
            with sqlite3.connect("root_products.db") as conn:
                print('Database connecting...')
                cursor = conn.execute("SELECT foodName FROM RootProductsTable")
                for row in cursor:
                    data.append(row[0])
                #self.showDatabase(data)
                
        elif button == 'starchy_categ':
            print('Starchy foods button pressed!')
            with sqlite3.connect("food_mixtures.db") as conn:
                print('Database connecting...')
                cursor = conn.execute("SELECT foodName FROM FoodMixturesTable")
                for row in cursor:
                    data.append(row[0])
                #self.showDatabase(data)
        print('Creating buttons...')
        food_list = GridLayout(cols=2, spacing =10, size_hint_y=None)
        #food_list.clear_widgets() # remove any existing buttons
        food_list.bind(minimum_height=food_list.setter('height'))

        for i in range(len(data)):
            btn = Button(text=data[i], size_hint_y=None, height=50, valign='center', font_size=20, background_color = (0,.8,.8,.8))
            #btn.text_size = (btn.size)
            food_list.add_widget(btn)
            print(i)

        root = ScrollView(size_hint=(1,None), size =(400,420))
        root.add_widget(food_list)
        return root

            #conn.close() 

    def reset(self):
        self.ids.food.clear_widgets()
        self.manager.current = "Homepage"
    
