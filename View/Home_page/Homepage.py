from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.popup import Popup
from kivy.uix.label import Label

Builder.load_file('View\Home_page\Homepage.kv')

import sqlite3

class Homepage(Screen):
    def on_pre_enter(self):
        app = MDApp.get_running_app()
        progress_value = app.get_progress_value()
        self.ids.cal_tracker.text = f"{progress_value}% Progress"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.weight_input.text = "9"
        self.ids.tracker.text = "Carbohydrate Intake Tracker"
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
        
        if str(track_goal[0]) == "Calories" or str(track_goal[0]) == "Default":
            self.ids.tracker.text = "Calorie Intake Tracker"
        elif str(track_goal[0]) == "Carbohydrates":
            self.ids.tracker.text = "Carbohydrates Intake Tracker"

        conn.commit()
        conn.close()

        
   
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

    def update_progress_bar(self):


        # Get a reference to the app object
        app = MDApp.get_running_app()

        # Get the progress value from the app object
        progress_value = app.get_progress_value()

        # Update the progress bar widget
        self.ids.progress_bar.value = progress_value




