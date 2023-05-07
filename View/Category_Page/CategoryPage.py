from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.label import Label
import sqlite3
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.metrics import dp
from functools import partial
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, NumericProperty
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from datetime import datetime

import re
import time

Builder.load_file('View\Category_Page\CategoryPage.kv')


class CategoryPage(Screen):
    foodList = ObjectProperty(None)
    total_calories = NumericProperty(0)
    
    def __init__(self , databaseName, manager = None, **kwargs):
        super(CategoryPage, self).__init__(**kwargs)
        self.manager = manager
        self.ids.weight_input.text = "54"
        self.databaseName = databaseName
        self.ids.foodList.clear_widgets()
        self.kCal = 0
        self.on_enter()
          
    def on_enter(self):
        self.food_buttons =[] 
        conn = sqlite3.connect(f'food_category//{self.databaseName}.db')
        c = conn.cursor()
        # Fetch the data from the database
        c.execute(f"SELECT foodName FROM Products")
        self.records = c.fetchall()

        self.data = []
        for record in self.records:
            self.data.append(record[:17])
        
        # Add the buttons to the screen
        for record in self.records:
            food = MDRectangleFlatButton(text=str(record[0]), size_hint = (1, 0.3), height='50dp', text_color = "black", line_color = "blue")
            food.bind(on_press=lambda instance, record=record: self.displayFoodValues(instance, record))
            self.ids.foodList.add_widget(food)
            self.food_buttons.append(food)
        # Close the database connection
        c.close()



    
    def displayProgressBar(self):

        # DISPLAY FOR PROGRESS BAR
        conn = sqlite3.connect('user_database\\userDB.db')
        cursor = conn.cursor()
        cursor.execute("SELECT CAST(track_goal AS TEXT) FROM user")
        track_goal = cursor.fetchone()

        
        if str(track_goal[0]) == "Calories" or str(track_goal[0]) == "Default":
            self.ids.tracker.text = "Calorie Intake Tracker"
        elif str(track_goal[0]) == "Carbohydrates":
            self.ids.tracker.text = "Carbohydrates Intake Tracker"

        conn.close()



    def displayFoodValues(self, instance, row_data):

        self.ids.food_edible.text = ""
        self.ids.food_calories.text = ""
        self.ids.food_fat.text = ""
        self.ids.food_choles.text = ""
        self.ids.food_sodium.text = ""
        self.ids.food_carbo.text = ""
        self.ids.food_protein.text = ""
        self.ids.food_calcium.text = ""
        self.ids.food_iron.text = ""
        offset = self.records.index(row_data)
        conn = sqlite3.connect(f'food_category//{self.databaseName}.db')
        c = conn.cursor()
        c.execute(f"SELECT * FROM Products LIMIT 1 OFFSET {offset}")
        record = c.fetchone()

        self.foodId = record[0]
        self.foodName = record[1]
        ep = record[3]
        self.kCal = record[5]
        tFat = record[7]
        chole = record[3]
        sodium = record[16]
        tCarbo = record[8]
        protein = record[6]
        calcium = record[12]
        iron = record[14]

        self.ids.food_edible.text = f"Edible Portion                 {str(ep)}%"
        self.ids.food_calories.text = f"Calories                    {str(self.kCal)}"
        self.ids.food_fat.text = f"Total Fat (g)              {str(tFat)}"
        self.ids.food_choles.text =  f"Cholesterol (mg)      {str(chole)}"
        self.ids.food_sodium.text =  f"Sodium (mg)             {str(sodium)}"
        self.ids.food_carbo.text =  f"Total Carbo (g)         {str(tCarbo)}"
        self.ids.food_protein.text =  f"Protein (g)                 {str(protein)}"
        self.ids.food_calcium.text =  f"Calcium (mg)            {str(calcium)}"
        self.ids.food_iron.text = f"Iron (mg)                    {str(iron)}"
        c.close()
    
    def reset(self):
        self.ids.foodList.clear_widgets()
        self.manager.current = "Homepage"
    
    def saveFood (self):
         
        weight_input = self.ids.weight_input.text
        weight_input = float(weight_input)
        tracker_text = self.ids.tracker.text
        edible_text = self.ids.food_edible.text

        # Check which to track/save
        if tracker_text == "Calorie Intake Tracker":
            track_field = self.ids.food_calories
        elif tracker_text == "Carbohydrates Intake Tracker":
            track_field = self.ids.food_carbo
        else:
            print("Error")

        if 'track_field' in locals():
            track_text = track_field.text.strip()
            # Remove all non-numeric characters and the first period (if it exists)
            track_text = re.sub(r'[^\d.]+', '', track_text)

            edible_text = edible_text.strip()
            edible_text = ''.join(filter(str.isdigit, edible_text))


        if not track_text and not edible_text:
            popupMessage("No food has been selected.")
        elif weight_input == '0':
            popupMessage("No weight has been detected.")
        else:
            track_text = float(track_text)
            edible_text = float(edible_text)

            # COMPUTATION
            weight_ep = (edible_text / 100) * weight_input
            food_intake = (track_text / 100) * weight_ep
            
            # GET the current time and date
            current_time = datetime.now().strftime('%H:%M:%S')
            current_date = datetime.now().strftime('%Y-%m-%d')

            conn = sqlite3.connect('mp_database\\food_history.db')
            cursor = conn.cursor()


 
            cursor.execute('''CREATE TABLE IF NOT EXISTS food_history (foodId TEXT, 
                                                            foodName TEXT, 
                                                            food_intake TEXT, 
                                                            current_time TEXT, 
                                                            current_date TEXT)''')

            cursor.execute("INSERT INTO food_history (foodId, foodName, food_intake, current_time, current_date) VALUES (?, ?, ?, ?, ?)", (self.foodId, self.foodName, food_intake, current_time, current_date))

            
            conn.commit()
            conn.close()

            popupMessage("Food Saved!", food_intake)



def popupMessage(message, food_intake = None):

    if message == "Food Saved!":
        pop = Popup(title = "Success",
                    content = Label(text = f"{message} \nFood Intake: {food_intake}"),
                    size_hint = (None, None),
                    size = (400, 200)
        )
        pop.open()
    else:
        pop = Popup(title = "Error",
                    content = Label(text = message),
                    size_hint = (None, None),
                    size = (400, 200)
        )
        pop.open() 