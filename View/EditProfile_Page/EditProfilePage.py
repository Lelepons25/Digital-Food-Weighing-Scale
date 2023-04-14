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

    def on_enter(self, *args):
        print("INSIDE")
        user_name, sex, age, user_weight, user_height, track_goal  = db.get_user(self.current)
        self.user_name.text = "Name: " + user_name
        self.sex.text = "Sex: " + sex
        self.age.text = "Age: " + age
        self.user_weight.text = "Weight: " + user_weight
        self.user_height.text = "Height: " + user_height
        self.track_goal.text = "Track: " + track_goal
        self.bmi.text = "BMI: empty" 