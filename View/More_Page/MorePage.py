from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivy.properties import ObjectProperty
from kivy.uix.vkeyboard import VKeyboard
from kivy.core.window import Window
from kivy.properties import StringProperty
import sqlite3
import datetime
from datetime import date

Builder.load_file('/home/pi/Digital-Food-Weighing-Scale/View/More_Page/MorePage.kv')

# More Page displays the other categories
class MorePage(Screen):
    
    now_date = StringProperty()
    dialog = None
    input_goalText = None
    
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)
        

        self.now_date = datetime.date.today().strftime("%Y%m%d")
        self.ids.weight_input.text = "54"
        self.manager = manager
        self.on_enter()

        self.input_goalText = MDTextField(
            hint_text="Enter your goal here",
            multiline=False
        )




    def on_enter(self):
        self.tracker()


    def tracker(self):

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
                goal = carbs_min[0]

    
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

            # Check if it is empty
            if not records:
                computeIntake = 0
                userIntake = 0
            else:
                previous_date = records[-1]
                prev = int(previous_date[4])

                if int(self.now_date) > prev:
                    computeIntake = 0
                    userIntake = 0
                    cursor.execute("UPDATE user SET totalIntake = ?", (computeIntake,))
                else:
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

    def enter_topButton(self, button):
        if button == "Save":
            content = Label(text='Please choose which category \nand what food is being weighed.', halign='center')
            popup = Popup(title='Error', content=content, size_hint=(None, None), size=(400, 200))
            popup.open()
            return
        elif button == "Clear":
            print("Clear")

def popupMessage(message):
    pop = Popup(title = " Invalid Form ",
        content = Label (text = message),
        size_hint = (None, None),
        size = (400, 400)
    )
    pop.open()
