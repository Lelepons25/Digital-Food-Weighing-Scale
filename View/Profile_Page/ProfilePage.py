from kivy.properties import ObjectProperty
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


    def __init__(self, manager = None, **kwargs):
        self.manager = manager
        super(ProfilePage, self).__init__(**kwargs)
        

    # Add info of the user
    def saveProfile(self):
        if self.user_name.text != "" and self.sex.text != "" and self.age.text != "":
            if self.user_weight.text != "" and self.user_height.text != "":
                db.add_user(self.user_name.text,
                            self.sex.text,
                            self.age.text,
                            self.user_weight.text,
                            self.user_height.text)
                self.reset()
                self.manager.current = "Homepage"
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
