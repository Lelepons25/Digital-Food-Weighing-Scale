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
# import psycopg2
import re
import time
import math

Builder.load_file('/home/pi/Digital-Food-Weighing-Scale/View/Category_Page/CategoryPage.kv')


class CategoryPage(Screen):
    # now_date = StringProperty()
    foodList = ObjectProperty(None)
    total_calories = NumericProperty(0)
    
    def __init__(self , databaseName, manager = None, **kwargs):
        super(CategoryPage, self).__init__(**kwargs)
        self.manager = manager
        # self.now_date = kwargs['now_date']
        self.ids.weight_input.text = "54"
        self.databaseName = databaseName
        self.ids.foodList.clear_widgets()
        self.kCal = 0
        self.on_enter()

    def on_enter(self):
        self.food_buttons =[] 
        conn = sqlite3.connect(f'food_category/{self.databaseName}.db')
        c = conn.cursor()
        # Fetch the data from the database
        c.execute(f"SELECT foodName FROM Products")
        self.records = c.fetchall()

        self.data = []
        for record in self.records:
            self.data.append(record[:17])
        
        # Add the buttons to the screen
        for record in self.records:
            food = MDRectangleFlatButton(text=str(record[0]), size_hint = (1, 0.1), height='40dp', text_color = "black", line_color = "blue")
            food.bind(on_press=lambda instance, record=record: self.displayFoodValues(instance, record))
            self.ids.foodList.add_widget(food)
            self.food_buttons.append(food)
        # Close the database connection
        c.close()

        self.displayProgressBar()



    
    def displayProgressBar(self):

        computeIntake = 0
        userIntake = 0


        conn = sqlite3.connect('/home/pi/Digital-Food-Weighing-Scale/user_database/userDB.db')
        cursor = conn.cursor()
        cursor.execute("SELECT CAST(track_goal AS TEXT) FROM user")
        track_goal = cursor.fetchone()

        #########  DISPLAY
        if str(track_goal[0]) == "Calories":
                self.ids.tracker.text = "Calorie Intake Tracker"
                cursor.execute("SELECT tdee FROM user")
                tdee = cursor.fetchone()
                goal = tdee[0]

        elif str(track_goal[0]) == "Carbohydrates":
                self.ids.tracker.text = "Carbohydrates Intake Tracker"
                cursor.execute("SELECT carbs_min FROM user")
                carbs_min = cursor.fetchone()
                goal = carbs_min
    
        #########
        
        connHistory = sqlite3.connect('/home/pi/Digital-Food-Weighing-Scale/mp_database/food_history.db')
        cursorHistory = connHistory.cursor()


        # CHECK if there are tables
        cursorHistory.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursorHistory.fetchall()
        print(tables)

        if not tables:
            # There are no tables in the food_history database.
            computeIntake = 0
            userIntake = 0
        else:
            # Access the latest table
            table_count = len(tables)-1
            table_name = f"food_history_{table_count}"

            # Compare Dates
            cursorHistory.execute(f"SELECT * FROM {table_name}")
            records = cursorHistory.fetchall()
            previous_date = records[-1]
            prev = int(previous_date[4])

            '''if int(self.now_date) > prev:
                computeIntake = 0
                userIntake = 0
                cursor.execute("UPDATE user SET totalIntake = ?", (computeIntake,))
            else:'''
            
            cursorHistory.execute(f"SELECT food_intake FROM {table_name}")
            intakes = cursorHistory.fetchall()

            ########### COMPUTATION
            computeIntake = sum([intake[0] for intake in intakes])
            userIntake = goal - computeIntake   
            cursor.execute("UPDATE user SET totalIntake = ?", (computeIntake,))
            
        
        self.ids.user_goal.text = f"{goal} goal - {computeIntake} intake = {userIntake} remaining"
        self.ids.user_goal.font_size = 12

        connHistory.commit()
        connHistory.close()
        conn.commit()
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
        conn = sqlite3.connect(f'food_category/{self.databaseName}.db')
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
        tracker_text = self.ids.tracker.text  # Title of the tracker
        edible_text = self.ids.food_edible.text # Edible Portion

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
            food_intake = math.ceil((track_text / 100) * weight_ep)
            
            # GET the current time and date
            current_time = datetime.now().strftime('%H:%M:%S')
            current_date = datetime.now().strftime('%Y%m%d')

            conn = sqlite3.connect('/home/pi/Digital-Food-Weighing-Scale/mp_database/food_history.db')
            cursor = conn.cursor()


            # check if the first table from food_history if it is empty
            cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'")
            table_count = cursor.fetchone()[0]

            if table_count < 8:
                if table_count == 0:
                    # Create the first table in food_history
                    table_name = f"food_history_{table_count}"
                    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (foodID TEXT, foodName TEXT, food_intake INTEGER, current_time TEXT, current_date TEXT)")

                    cursor.execute(f"INSERT INTO {table_name}(foodID, foodName, food_intake, current_time, current_date) VALUES (?, ?, ?, ?, ?)", (self.foodId, self.foodName, food_intake, current_time, current_date))
                    conn.commit()
                    popupMessage("Food Saved!", food_intake)
                else:
                    # Check previous table
                    table_name = f"food_history_{table_count - 1}"

                    # COMPARE DATES
                    cursor.execute(f"SELECT * FROM {table_name}")
                    records = cursor.fetchall()
                    previous_date = records[-1]
                    prev = int(previous_date[4])

                    if int(current_date) == int(prev):
                        # Insert new record
                        cursor.execute(f"INSERT INTO {table_name}(foodID, foodName, food_intake, current_time, current_date) VALUES (?, ?, ?, ?, ?)", (self.foodId, self.foodName, food_intake, current_time, current_date))
                        conn.commit()
                        popupMessage("Food Saved!", food_intake)
                    else:
                        table_name = f"food_history_{table_count}"

                        if table_count != 7:
                            # Create 6 other tables
                            cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (foodID TEXT, foodName TEXT, food_intake INTEGER, current_time TEXT, current_date TEXT)")
                            cursor.execute(f"INSERT INTO {table_name}(foodID, foodName, food_intake, current_time, current_date) VALUES (?, ?, ?, ?, ?)", (self.foodId, self.foodName, food_intake, current_time, current_date))
                            conn.commit()
                            popupMessage("Food Saved!", food_intake)
                        else:
                            popupMessage("The database is full.")

                    conn.commit()

                conn.close()
                self.displayProgressBar()
            else:
                popupMessage("The database is full.")


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