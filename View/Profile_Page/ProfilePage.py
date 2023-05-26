from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.vkeyboard import VKeyboard
from kivy.core.window import Window
from kivy.factory import Factory
from View.Home_page.Homepage import Homepage

import os
import sqlite3
import math

Builder.load_file("View\Profile_Page\ProfilePage.kv")


class ProfilePage(Screen):
    user_name = ObjectProperty(None)
    sex = ObjectProperty(None)
    age = ObjectProperty(None)
    user_weight = ObjectProperty(None)
    user_height = ObjectProperty(None)
    track_goal = ObjectProperty(None)
    activity_level = ObjectProperty(None)

    # Inherits the manager attribute for screen manager
    def __init__(self, manager = None, **kwargs):
        super(ProfilePage, self).__init__(**kwargs)
        self.manager = manager
        # Bind on_focus event of each TextInput to on_text_focus()
        self.user_name.bind(focus=self.on_text_focus)
        self.age.bind(focus=self.on_text_focus)
        self.user_weight.bind(focus=self.on_text_focus)
        self.user_height.bind(focus=self.on_text_focus)

    def get_sex_spinner(self, value):
        self.sex.text = value
    
    def get_trackgoal_spinner(self, value):
        self.track_goal.text = value
    
    def get_activitylevel_spinner(self, value):
        self.activity_level.text = value


    def clear_error_message(self):
        for widget in self.root.children:
            if isinstance(widget, Label) and widget.text == "Please choose a valid option":
                self.root.remove_widget(widget)


    def compute_calIntake(self, age, sex, user_weight, user_height, activity_level):
        bmr = None
        tdee = None

        # COMPUTE FOR BMR
        if sex == "Male":
            bmr = 88.362 + (13.397 * float(user_weight)) + (4.799 * float(user_height)) - (5.677 * age)
        elif sex == "Female":
            bmr = 447.593 + (9.247 * float(user_weight)) + (3.098 * float(user_height)) - (4.330 * age)

        # COMPUTE FOR TDEE
        if activity_level == "Sedentary":
            tdee = bmr * 1.2
        elif activity_level == "Lightly active":
            tdee = bmr * 1.375
        elif activity_level == "Moderately active":
            tdee = bmr * 1.55
        elif activity_level == "Very active":
            tdee = bmr * 1.725
        elif activity_level == "Extra active":
            tdee = bmr * 1.9
        
        return tdee


    # Add info of the user
    def saveProfile(self):
        # Check if all required fields are filled
        if self.user_name.text and self.sex.text and self.age.text and self.user_weight.text and self.user_height.text and self.track_goal.text and self.activity_level.text:
            # Check the length of the name 
            if len(self.user_name.text) >= 4 and len(self.user_name.text)<=50:
                # Check spinner
                if self.sex.text in ["Male", "Female"]:
                    # Check if age is a valid positive integer
                    if self.age.text.isdigit() and 18 < int(self.age.text) < 100:
                        # Check if user weight and height are valid positive integers
                        if self.user_weight.text.isdigit() and int(self.user_weight.text) > 30 and int(self.user_weight.text) < 400:
                            if self.user_height.text.isdigit() and int(self.user_height.text) > 0 and int(self.user_height.text) <300:
                                # Check spinner
                                if self.track_goal.text in ["Calories", "Carbohydrates"]:
                                    if self.activity_level.text in ["Sedentary", "Lightly active", "Moderately active", "Very active", "Extra active"]:
                                    # Add user to the database
                                        user_name = self.user_name.text
                                        sex = self.sex.text
                                        age = int(self.age.text)
                                        user_weight = float(self.user_weight.text)
                                        user_height = float(self.user_height.text)
                                        track_goal = self.track_goal.text
                                        activity_level = self.activity_level.text
                                        totalIntake = None

                                        # COMPUTE BMI
                                        bmi = user_weight / ((user_height/100) ** 2)
                                    
                                        # check track goal:
                                        if track_goal == "Calories":                
                                            # COMPUTE TDEE 
                                            tdee = math.ceil(self.compute_calIntake(int(age), sex, user_weight, user_height, activity_level))
                                            carbs_min = None
                                            carbs_max = None
                                        else:
                                            tdee = math.ceil(self.compute_calIntake(int(age), sex, user_weight, user_height, activity_level))
                                            carbs_min = math.ceil((tdee * 0.45)/4)
                                            carbs_max = math.ceil((tdee * 0.65)/4)
                                    
                                        # Connect to the database
                                        conn = sqlite3.connect('user_database/userDB.db')
                                        cursor = conn.cursor()

                                        # Check if the database is empty
                                        cursor.execute("SELECT COUNT(*) FROM user")
                                        result = cursor.fetchone()

                                        if result[0] == 0:
                                            # User does not exist, insert new row
                                            cursor.execute("INSERT INTO user (user_name, sex, age, user_weight, user_height, track_goal, activity_level, bmi, tdee, carbs_min, carbs_max, totalIntake) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (user_name, sex, age, user_weight, user_height, track_goal, activity_level, bmi, tdee, carbs_min, carbs_max, totalIntake))
                                            conn.commit()
                                            conn.close()    
                                            self.manager.generateHomePageScreen()
                                        else:
                                            # User exists, update existing row
                                            cursor.execute("UPDATE user SET user_name=?, sex=?, age=?, user_weight=?, user_height=?, track_goal=?, activity_level=?, bmi=?, tdee=?, carbs_min=?, carbs_max=?, totalIntake=?", (user_name, sex, age, user_weight, user_height, track_goal, activity_level, bmi, tdee, carbs_min, carbs_max, totalIntake))
                                            conn.commit()
                                            conn.close()
                                            self.manager.generateEditProfilePageScreen()

                                            # Delete food history
                                            Homepage.deleteHistory(self)

                                        # Check if there's a duplicate in the database
                                            if os.path.exists('mp_database/Duplicatefood_history.db'):
                                                os.remove('mp_database/Duplicatefood_history.db')                            
                                    else:
                                        invalidForm("Select your activity level") 
                                else:
                                    invalidForm("Select your track goal")
                            else: 
                                invalidForm("Input height in cm raging from 50 - 300")
                        else:
                            invalidForm("Input weight in kg raging from 30 - 400")
                    else:
                        invalidForm("Age Limit: 18 - 100")
                else:
                    invalidForm("Select your sex assigned at birth")
            else:
                invalidForm("Input name with 4-50 characters")
        else:
            invalidForm("Please complete the form")


    def cancel_profile(self):

        conn = sqlite3.connect("user_database/userDB.db")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM user")
        count = cursor.fetchone()

        if count[0] == 0:
            # Display pop up message
            invalidForm("Please input your information to proceed")
        else:
            self.manager.generateEditProfilePageScreen()

    def on_text_focus(self, widget, value):
        if value:
            keyboard = VKeyboard(target=widget, layout='qwerty', size_hint=(0.35, 0.4))
            keyboard.bind(on_key_up=self.key_up) 
            Window.add_widget(keyboard)
        else:
            for child in Window.children[:]:
                if isinstance(child, VKeyboard):
                    Window.remove_widget(child)


    # key_up: when the keyboard is released
    def key_up(self, keyboard, keycode, text, modifiers):
        active_textfield = None 
        if isinstance(keycode, tuple):
            keycode = keycode[1]
        if self.user_name.focus:
            active_textfield = self.user_name
        elif self.age.focus:
            active_textfield = self.age
        elif self.user_weight.focus:
            active_textfield = self.user_weight
        elif self.user_height.focus:
            active_textfield = self.user_height
            
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
                active_textfield.text += text  

def invalidForm(message):
    pop = Popup(title = " Invalid Form ",
        content = Label (text = message),
        size_hint = (None, None),
        size = (400, 400)
    )
    pop.open()

def restart():
    pop = Popup(title = "Changes Saved!",
        content = Label (text = "Restart the program to see the changes"),
        size_hint = (None, None),
        size = (400,400)
    )
    pop.open()
