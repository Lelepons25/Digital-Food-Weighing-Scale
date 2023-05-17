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

Builder.load_file('View\Home_page\Homepage.kv')

import sqlite3
import datetime
from datetime import date

class Homepage(Screen):

    now_date = StringProperty()
    dialog = None
    input_goalText = None
    
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)

        self.now_date = datetime.date.today().strftime("%Y%m%d")
        print("NOW INIT:", self.now_date)

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


        conn = sqlite3.connect('user_database/userDB.db')
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
        
        connHistory = sqlite3.connect('mp_database/food_history.db')
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


    def confirmation_resetDialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title = "Reset your food intake?",
                text = "This will also delete the history of your food intake. Are you sure?",
                type = "custom",
                buttons=[
                    MDFlatButton(
                        text = "CANCEL",
                        theme_text_color="Custom",
                        on_release=self.cancel_dialog,
                    ),
                    MDFlatButton(
                        text = "RESET",
                        theme_text_color="Custom",
                        on_release=self.reset_dialog,
                    ),
                ]
            )
        self.dialog.open()

    def reset_dialog(self, instance):
       
        conn = sqlite3.connect('mp_database/food_history.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM food_history")
        conn.commit()
        conn.close()

        self.dialog.dismiss()
        popupResetMessage("Your food intake has been reset!")
        self.manager.generateHomePageScreen()

    # customize the goal based on the tracker selected
    def confirmation_dialog(self):
        # set the dialog title based on the tracker selected
        if self.ids.tracker.text == "Calorie Intake Tracker":
            dialog_title = "Customize Calorie Intake Goal:"
        elif self.ids.tracker.text == "Carbohydrates Intake Tracker":
            dialog_title = "Customize Minimum Carbohydrate Intake Goal:"

        # Bind on_focus event of each TextInput to on_text_focus()
        self.input_goalText.bind(focus=self.on_text_focus)

        # create the dialog if it does not exist
        if not self.dialog:
            self.dialog = MDDialog(
                title=f"{dialog_title}",
                type="custom",
                content_cls=self.input_goalText,
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        on_release=self.cancel_dialog,
                    ),
                    MDFlatButton(
                        text="SAVE",
                        theme_text_color="Custom",
                        on_release=self.save_custom_goal,
                    ),
                ],
            )
        # open the dialog
        self.dialog.open()

    # cancel the dialog
    def cancel_dialog(self, instance):
        self.dialog.dismiss()

    
    def save_custom_goal(self, instance):
        goal = self.input_goalText.text

        if goal == "":
            popupMessage("Please enter a goal.")
        elif not goal.isdigit() > 0:
            popupMessage("Please enter a number.")
        else:
        # connect to the database
            with sqlite3.connect('user_database\\userDB.db') as conn:
                cursor = conn.cursor()

                # update the goal based on the tracker selected
                if self.ids.tracker.text == "Calorie Intake Tracker":
                    cursor.execute("UPDATE user SET tdee = ? WHERE track_goal = ?", (goal, "Calories"))
                elif self.ids.tracker.text == "Carbohydrates Intake Tracker":
                    carbs_max = None
                    carbs_max = float(goal) * (0.65/0.45)
                    cursor.execute("UPDATE user SET carbs_min = ?, carbs_max = ? WHERE track_goal = ?", (goal, carbs_max, "Carbohydrates"))

                # commit the changes
                conn.commit()
            
            conn.close()
            self.dialog.dismiss()
            self.manager.generateHomePageScreen()

    def on_text_focus(self, widget, value):
        if value and widget is self.input_goalText:
            keyboard = VKeyboard(target=widget, layout='qwerty', size_hint=(0.5, 0.4), pos_hint={"center_x": 0.4, "center_y": 0.2})
            keyboard.bind(on_key_up=self.key_up) # Add this line to bind the key_up method
            Window.add_widget(keyboard)
        else:
            for child in Window.children[:]:
                if isinstance(child, VKeyboard):
                    Window.remove_widget(child)

    
    def key_up(self, keyboard, keycode, text, modifiers):
        active_textfield = None 
        if isinstance(keycode, tuple):
            keycode = keycode[1]

        active_textfield = self.input_goalText

        if active_textfield is not None:
            if keycode == 'backspace':
                active_textfield.text = active_textfield.text[:-1]
            elif keycode == 'spacebar':
                active_textfield.text += ' '
            elif keycode == 'capslock':
                active_textfield.text.upper()
            elif keycode == 'shift':
                pass
            elif keycode == 'enter':
                pass
            elif keycode == 'layout':
                pass
            else:
                active_textfield.insert_text(text)


    def enter_topButton(self, button):
        if button == "Save":
            content = Label(text='Please choose which category \nand what food is being weighed.', halign='center')
            popup = Popup(title='Error', content=content, size_hint=(None, None), size=(400, 200))
            popup.open()
            return
        elif button == "Tare":
            self.ids.weight_input.text = "0"

def popupMessage(message):
    pop = Popup(title = " Invalid Form ",
        content = Label (text = message),
        size_hint = (None, None),
        size = (300, 300)
    )
    pop.open()

def popupResetMessage(message):
    pop = Popup(title = " Success ",
        content = Label (text = message),
        size_hint = (None, None),
        size = (300, 300)
    )
    pop.open()


