import pandas as pd
import sqlite3
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, OneLineListItem
import matplotlib.pyplot as plt
import shutil
import datetime
import math


Builder.load_file('View\FoodHistoryAnalysis_Page\FoodHistoryAnalysisPage.kv')

class FoodHistoryAnalysisPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.on_enter()

    def on_enter(self):
        conn = sqlite3.connect('mp_database/Duplicatefood_history.db')
        cursor = conn.cursor()

        # Check if table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if not tables:
            self.ids.title_foodAnalysisFreq.text= "Your Food History Analysis will be available after 7 days"
            self.ids.title_foodAnalysisIntake.text= "Your Food History Analysis will be available after 7 days"
            self.ids.title_foodAnalysisTime.text= "Your peak consumption time of the week will be available after 7 days"
        elif len(tables) == 7:
            self.ids.title_foodAnalysisFreq.text= "Your most frequent food of the week"
            self.ids.title_foodAnalysisIntake.text= "Your highest food intake of the week"
            self.ids.title_foodAnalysisTime.text = "Peak consumption time of the week"
            self.analyis_frequency()
            self.analysis_intake()
            self.analysis_timeIntake()


    def analyis_frequency(self):

        conn = sqlite3.connect('mp_database/Duplicatefood_history.db')

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
        
        conn = sqlite3.connect('mp_database/Duplicatefood_history.db')
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
    

    def analysis_timeIntake(self):
        conn = sqlite3.connect('mp_database/Duplicatefood_history.db')

        # Get the sum of food intake
        df = []
        for i in range(7):
            table_name = f"food_history_{i}"
            dfs = pd.read_sql_query(f"SELECT * from {table_name}", conn)
            df.append(dfs)

        df = pd.concat(df)
        df['current_time'] = pd.to_datetime(df['current_time'], format='%H:%M:%S')
        df['time_range'] = df['current_time'].apply(lambda x: get_time_range(x.strftime('%H:%M:%S')))
        sum_intake = df.groupby('time_range')['food_intake'].sum() / 7
        sum_intake = sum_intake.apply(math.ceil)
        sum_intake = sum_intake.sort_values(ascending=False)
        print(sum_intake)


        # Add the food items as MDListItems to the list
        for time, food_intake in sum_intake.items():
            item = OneLineListItem(text=f"{time}: {food_intake}")
            self.ids.food_AnalysisTime.add_widget(item)




def get_time_range(time_str):
    time = datetime.datetime.strptime(time_str, '%H:%M:%S').time()
    if datetime.time(6, 0) <= time <= datetime.time(10, 0):
        return '6:00 - 10:00'
    elif datetime.time(11, 0) <= time <= datetime.time(14, 0):
        return '11:00 - 14:00'
    elif datetime.time(17, 0) <= time <= datetime.time(21, 0):
        return '17:00 - 21:00'
    else:
        return 'Snacks'