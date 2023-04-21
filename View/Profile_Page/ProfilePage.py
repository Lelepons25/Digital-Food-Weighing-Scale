from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from kivy.lang import Builder
from kivy.uix.vkeyboard import VKeyboard
from View.EditProfile_Page.EditProfilePage import EditProfilePage
from kivy.core.window import Window

import os
import sys
import subprocess
Builder.load_file("View\Profile_Page\ProfilePage.kv")

db = DataBase("users.txt")

def restart_program():
    # Kill the current process
    subprocess.call([sys.executable, "-c", "import os; os.kill(os.getpid(), 9)"])

    # Start a new instance of the program
    subprocess.Popen([sys.executable] + sys.argv)


class ProfilePage(Screen):
    user_name = ObjectProperty(None)
    sex = ObjectProperty(None)
    age = ObjectProperty(None)
    user_weight = ObjectProperty(None)
    user_height = ObjectProperty(None)
    track_goal = ObjectProperty(None)

    # Inherits the manager attribute for screen manager
    def __init__(self, manager = None, **kwargs):
        super(ProfilePage, self).__init__(**kwargs)
        self.manager = manager
        # Bind on_focus event of each TextInput to on_text_focus()
        self.user_name.bind(focus=self.on_text_focus)
        self.age.bind(focus=self.on_text_focus)
        self.user_weight.bind(focus=self.on_text_focus)
        self.user_height.bind(focus=self.on_text_focus)

    def on_text_focus(self, widget, value):
        if value:
            keyboard = VKeyboard(target=widget, layout='qwerty', size_hint = (0.35, 0.4))
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

    def get_sex_spinner(self, value):
        self.sex.text = value
    
    def get_trackgoal_spinner(self, value):
        self.track_goal.text = value

    # Add info of the user
    def saveProfile(self):
        # Check if all required fields are filled
        if self.user_name.text and self.sex.text and self.age.text and self.user_weight.text and self.user_height.text and self.track_goal.text:
            # Check the length of the name 
            if len(self.user_name.text) >= 4 and len(self.user_name.text)<=50:
            # Check if age is a valid positive integer
                if self.age.text.isdigit() and 2 < int(self.age.text) < 100:
                    # Check if user weight and height are valid positive integers
                    if self.user_weight.text.isdigit() and int(self.user_weight.text) > 0 and int(self.user_weight.text) < 400:
                        if self.user_height.text.isdigit() and int(self.user_height.text) > 0 and int(self.user_height.text) <300:
                        # Add user to the database
                            if os.path.getsize(db.file_path) == 0:
                                db.add_user(self.user_name.text, self.sex.text, int(self.age.text), float(self.user_weight.text), float(self.user_height.text), self.track_goal.text)
                                self.reset()
                                EditProfile_Page = EditProfilePage()
                                EditProfile_Page.display_database()
                                self.manager.current = "Homepage"
                            else :
                                db.update_user(self.user_name.text, self.sex.text, int(self.age.text), float(self.user_weight.text), float(self.user_height.text), self.track_goal.text)
                                restart()
                                self.reset()
                                # restart_program()
                                EditProfile_Page = EditProfilePage()
                                EditProfile_Page.display_database()
                                self.manager.current = "EditProfilePage"
                        else: 
                            invalidForm("Input height in cm raging from 50 - 300")
                    else:
                        invalidForm("Input weight in kg raging from 2 - 400")
                else:
                    invalidForm("Input age between 0 - 100")
            else:
                invalidForm("Input name with 4-50 characters")
        else:
            invalidForm("Please complete the form")

    
    def reset(self):
        self.user_name.text = ""
        self.sex.text = ""
        self.age.text = ""
        self.user_weight.text = ""
        self.user_height.text = ""

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