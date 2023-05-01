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
        app = MDApp.get_running_app()
        progress_value = app.progress_value
        print(progress_value)
        self.ids.cal_tracker.text = f"{progress_value}% Progress"

        self.food_buttons =[] 
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

        self.kCal = record[5]
        tFat = record[7]
        chole = record[3]
        sodium = record[16]
        tCarbo = record[8]
        protein = record[6]
        calcium = record[12]
        iron = record[14]

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
        weight_input = self.ids.weight_input
        calories_input = self.ids.food_calories

        weight = weight_input.text.strip()
        if weight == '0':
            # Show an error message using a pop-up
            content = Label(text='No weight has been detected.')
            popup = Popup(title='Error', content=content, size_hint=(None, None), size=(400, 200))
            popup.open()
            return
        weight = float(weight)

        calories = calories_input.text.strip()
        if calories == '0':
            # Show an error message using a pop-up
            content = Label(text='Please enter a calories value.')
            popup = Popup(title='Error', content=content, size_hint=(None, None), size=(400, 200))
            popup.open()
            return
        cal = float(self.kCal)

        # if with decimals: totalCal = round(((weight / 100) * calories), 2) //2 decimal point
        totalCal = round((weight / 100) * cal)
        # Show a success message using a pop-up
        content = Label(text=f'The amount of calorie is {totalCal} \n and has been saved to progress bar and history.',  halign='center')
        popup = Popup(title='Successfully saved!', content=content, size_hint=(None, None), size=(500, 200))
        popup.open()

        print(totalCal)

        # Update the total calories for the category
        self.total_calories += totalCal

        # Update the progress bar value and label text
        self.progress_bar.value = self.total_calories
        self.update_progress_label()

         
    def update_progress_label(self):
        # Update the progress bar label text based on the total calories and the maximum value of the progress bar
        progress_percent = int((self.total_calories / self.progress_bar.max) / 100)
        self.ids.cal_tracker.text = f"{progress_percent}% Progress"
        
        app = MDApp.get_running_app()
        app.progress_value = progress_percent
        print(app.progress_value)
        app.update_progress_value(progress_percent)
        