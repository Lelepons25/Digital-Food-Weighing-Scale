import pandas as pd
import sqlite3
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, OneLineListItem
import matplotlib.pyplot as plt




Builder.load_file('View\FoodHistoryAnalysis_Page\FoodHistoryAnalysisPage.kv')

class FoodHistoryAnalysisPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.on_enter()

    def on_enter(self):
        conn = sqlite3.connect('mp_database/food_history.db')
        cursor = conn.cursor()

        # Check if table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if not tables:
            label = MDLabel(text="No Food History")
            self.ids.card_foodAnalysisFreq.add_widget(label)
            self.ids.card_foodAnalysisIntake.add_widget(label) 
        elif len(tables) != 7:
            label = MDLabel(text="Your Food History Analysis will be available after 7 days")
            self.ids.card_foodAnalysisFreq.add_widget(label)
            self.ids.card_foodAnalysisIntake.add_widget(label)
        elif len(tables) == 7:
            self.analyis_frequency()
            self.analysis_intake()


    def analyis_frequency(self):

        conn = sqlite3.connect('mp_database/food_history.db')

        # Frequency analysis
        dfs = []
        for i in range(7):
            table_name = f"food_history_{i}"
            df = pd.read_sql_query(f"SELECT * from {table_name}", conn)
            dfs.append(df)

        df = pd.concat(dfs)

        # Group the data by foodName and count the frequency of each foodName
        food_counts = df.groupby('foodName')['foodName'].count()

        # Get the top 5 most frequent foods
        most_frequent_food = food_counts.nlargest(5)
        # Extract the food name and frequency from the most_frequent_food series
        df = most_frequent_food.reset_index(name='frequency')[['foodName', 'frequency']]

        # Add the food items as MDListItems to the list
        for food, frequency in df.values:
            item = OneLineListItem(text=f"{food}: {frequency}")
            self.ids.food_AnalysisFreq.add_widget(item)
        
        conn.close()
    
    def analysis_intake(self):
        
        conn = sqlite3.connect('mp_database/food_history.db')
        # Get the top 5 highest food intake from the database
        dfsIntake = []
        for i in range(7):
            table_name = f"food_history_{i}"
            df = pd.read_sql_query(f"SELECT * from {table_name}", conn)
            dfsIntake.append(df)

        dfIntake = pd.concat(dfsIntake)

        # Group the data by foodName, get the maximum food_intake for each foodName, and get the top 5 largest values
        highest_food_intakes = dfIntake.groupby('foodName')['food_intake'].max().nlargest(5)


        # Add the food items as MDListItems to the list
        for food, food_intake in highest_food_intakes.items():
            item = OneLineListItem(text=f"{food}: {food_intake}")
            self.ids.food_AnalysisIntake.add_widget(item)
        
        conn.close()