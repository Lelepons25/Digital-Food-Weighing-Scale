from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.popup import Popup
from kivy.uix.label import Label

Builder.load_file('View\Home_page\Homepage.kv')

import sqlite3

class Homepage(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.weight_input.text = "9"
        self.ids.tracker.text = "Carbohydrate Intake Tracker"
        wm = self.manager
        progress_value = wm.progress_value
        print(progress_value)
        self.ids.cal_tracker.text = f"{progress_value}% Progress"
        self.on_enter()
        # self.ids.cal_tracker.text = f"{progress_value}% Progress"

    
    def on_enter(self):
        conn = sqlite3.connect('user_database\\userDB.db')
        cursor = conn.cursor()
        cursor.execute("SELECT CAST(track_goal AS TEXT) FROM user")
        track_goal = cursor.fetchone()

        wm = self.manager
        progress_value = wm.progress_value
        print(progress_value)
        self.ids.cal_tracker.text = f"{progress_value}% Progress"

        # Check which to track from user.txt database
        with open("users.txt", "r") as f:
            line = f.readline()
            fields = line.strip().split(";")
            track_goal = str(fields[5])
        
        if str(track_goal[0]) == "Calories" or str(track_goal[0]) == "Default":
            self.ids.tracker.text = "Calorie Intake Tracker"
        elif str(track_goal[0]) == "Carbohydrates":
            self.ids.tracker.text = "Carbohydrates Intake Tracker"

        conn.commit()
        conn.close()

        if track_goal == "Calorie Deficit" or track_goal == "Default":
            self.ids.tracker.text = "Calorie Deficit Tracker"
        elif track_goal == "Low Carb Diet":
            self.ids.tracker.text = "Low Carb Diet Tracker"
>>>>>>> 45794e505e73c419d0f9c4dbedca3151ed8d26e2
        
   
    def enter_topButton(self, button):
        if button == "Profile":
            self.manager.current = "EditProfilePage"
        elif button == "Save":
            content = Label(text='Please choose which category \nand what food is being weighed.', halign='center')
            popup = Popup(title='Error', content=content, size_hint=(None, None), size=(400, 200))
            popup.open()
            return
        elif button == "Clear":
            print("Clear")

 




