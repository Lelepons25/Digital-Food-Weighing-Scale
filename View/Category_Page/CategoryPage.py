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
import re



Builder.load_file('View\Category_Page\CategoryPage.kv')
conn = sqlite3.connect('food_category.db')

class CategoryPage(Screen):
    foodList = ObjectProperty(None)
    total_calories = NumericProperty(0)
    
    def __init__(self , table_name, manager = None, **kwargs):
        super(CategoryPage, self).__init__(**kwargs)
        self.manager = manager
        self.ids.weight_input.text = "54"
        self.table_name = table_name
        self.ids.foodList.clear_widgets()
        self.kCal = 0
        self.on_enter()
        # Get a reference to the progress bar widget
        self.progress_bar = self.ids.cal_tracker_bar
          
    def on_enter(self):
        wm = self.manager
        progress_value = wm.progress_value
        print(progress_value)
        self.ids.cal_tracker.text = f"{progress_value}% Progress"
        self.food_buttons =[] 
        # Connect to the database
        conn = sqlite3.connect('food_category.db')
        c = conn.cursor()
        # Fetch the data from the database
        c.execute(f"SELECT foodName FROM {self.table_name}")
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
        c = conn.cursor()
        c.execute(f"SELECT * FROM {self.table_name} LIMIT 1 OFFSET {offset}")
        record = c.fetchone()

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
            print(track_text)

            edible_text = edible_text.strip()
            edible_text = ''.join(filter(str.isdigit, edible_text))

            # CONVERT string to float
            track_text = float(track_text)
            edible_text = float(edible_text)


        if not track_text and not edible_text:
            popupMessage("No food has been selected.")
        elif weight_input == '0':
            popupMessage("No weight has been detected.")
        else:
            # COMPUTATION
            weight_ep = (edible_text / 100) * weight_input
            food_intake = (track_text / 100) * weight_ep

            print("edible_text:" + str(edible_text))
            print("track_text:" + str(track_text))
            print("weight_input:" + str(weight_input))
            print("weight_ep:" + str(weight_ep)) 
            print("Food Intake:")
            print(food_intake)

        
    
        # Update the total calories for the category
        # self.total_calories += totalCal


        # Update the progress bar value and label text
        self.progress_bar.value = self.total_calories
        self.update_progress_label()

    def update_progress_label(self):
        # Update the progress bar label text based on the total calories and the maximum value of the progress bar
        progress_percent = int((self.total_calories / self.progress_bar.max) / 100)
        self.ids.cal_tracker.text = f"{progress_percent}% Progress"
        
        wm = self.manager
        wm.progress_value = progress_percent
        wm.update_progress_value(progress_percent)


def popupMessage(message):
    pop = Popup(title = "Error",
                content = Label(text = message),
                size_hint = (None, None),
                size = (400, 200)
    )
    pop.open() 