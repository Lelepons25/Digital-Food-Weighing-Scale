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

    print(user_name.text)

    def on_enter(self, *args):
        user_data = db.get_user(self.current)
        print(user_data)
        if user_data:
            user_name, sex, age, user_weight, user_height, track_goal = user_data
            self.user_name.text = f"Name: {user_name}"
            self.sex.text = f"Sex: {sex}"
            self.age.text = f"Age: {age}"
            self.user_weight.text = f"Weight: {user_weight}"
            self.user_height.text = f"Height: {user_height}"
            self.track_goal.text = f"Track: {track_goal}"
            self.bmi.text = "BMI: empty"
        else:
            # Handle case where user data is not found
            pass