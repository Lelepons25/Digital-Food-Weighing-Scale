from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp

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
        super(ProfilePage, self).__init__(**kwargs)

    def get_sex_spinner(self, value):
        self.sex.text = value
    
    def get_trackgoal_spinner(self, value):
        self.track_goal.text = value


    # Add info of the user
    def saveProfile(self):
        
        # Check if all required fields are filled
        if self.user_name.text and self.sex.text and self.age.text and self.user_weight.text and self.user_height.text and self.track_goal.text:
            # Check if age is a valid positive integer
            if self.age.text.isdigit() and 0 < int(self.age.text) < 100:
                # Check if user weight and height are valid positive integers
                if self.user_weight.text.isdigit() and int(self.user_weight.text) > 0 and self.user_height.text.isdigit() and int(self.user_height.text) > 0:
                    # Add user to the database
                    db.add_user(self.user_name.text, self.sex.text, int(self.age.text), float(self.user_weight.text), float(self.user_height.text), self.track_goal.text)
                    self.reset()
                    self.manager.current = "Homepage"
                else:
                    invalidForm()
            else:
                invalidForm()
        else:
            invalidForm()

    
    def reset(self):
        self.user_name.text = ""
        self.sex.text = ""
        self.age.text = ""
        self.user_weight.text = ""
        self.user_height.text = ""

def invalidForm():
    pop = Popup(title = " Invalid Form ",
        content = Label (text = "Fill in with valid information"),
        size_hint = (None, None),
        size = (400, 400)
    )
    pop.open()
