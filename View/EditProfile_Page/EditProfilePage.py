from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from database import DataBase


Builder.load_file('View\EditProfile_Page\EditProfilePage.kv')
db = DataBase("users.txt")

class EditProfilePage(Screen):
    
    user_name = ObjectProperty(None)
    sex = ObjectProperty(None)
    age = ObjectProperty(None)
    user_weight = ObjectProperty(None)
    user_height = ObjectProperty(None)
    track_goal = ObjectProperty(None)
    bmi = ObjectProperty(None)
    current = ""

    print("Inside1")
            

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        first_line = db.load()
        if first_line:
            fields = first_line.strip().split(";")
            if len(fields) == 6:
                user_name, sex, age, user_weight, user_height, track_goal = fields
                self.ids.user_name.text = f"Name: {user_name}"
                self.ids.sex.text = f"Sex: {sex}"
                self.ids.age.text = f"Age: {age}"
                self.ids.user_weight.text = f"Weight: {user_weight}"
                self.ids.user_height.text = f"Height: {user_height}"
                self.ids.track_goal.text = f"Track: {track_goal}"
                self.ids.bmi.text = "BMI: empty"
            else:
                print(f"Invalid line format in file {self.filename}: {first_line}")
        else:
            print("Database is empty.")
