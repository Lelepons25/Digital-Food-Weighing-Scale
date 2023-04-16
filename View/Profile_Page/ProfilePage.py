from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from kivy.lang import Builder
from kivy.uix.vkeyboard import VKeyboard



Builder.load_file("View\Profile_Page\ProfilePage.kv")

db = DataBase("users.txt")

class ProfilePage(Screen):
    user_name = ObjectProperty(None)
    sex = ObjectProperty(None)
    age = ObjectProperty(None)
    user_weight = ObjectProperty(None)
    user_height = ObjectProperty(None)
    track_goal = ObjectProperty(None)



    # Inherits the manager attribute for screen manager
    def __init__(self, manager = None, **kwargs):
        self.manager = manager
        self.user = "User"
        print(self.user)
        super(ProfilePage, self).__init__(**kwargs)
        # Define Keyboard
        keyboard = VKeyboard(size_hint = (0.4, 0.4),
                             on_key_up = self.key_up)
        self.add_widget(keyboard)

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
            print(self.user_name.text)
            if len(self.user_name.text) >= 4 and len(self.user_name.text)<=50:
            # Check if age is a valid positive integer
                if self.age.text.isdigit() and 2 < int(self.age.text) < 100:
                    # Check if user weight and height are valid positive integers
                    if self.user_weight.text.isdigit() and int(self.user_weight.text) > 0 and int(self.user_weight.text) < 400:
                        if self.user_height.text.isdigit() and int(self.user_height.text) > 0 and int(self.user_height.text) <300:
                        # Add user to the database
                            db.add_user(self.user_name.text, self.sex.text, int(self.age.text), float(self.user_weight.text), float(self.user_height.text), self.track_goal.text)
                            self.reset()
                            self.manager.current = "Homepage"
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
