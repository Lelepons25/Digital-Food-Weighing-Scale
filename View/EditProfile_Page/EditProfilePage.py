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

    def identify_bmiCategory(self, bmi):
        if bmi >= 0 and bmi <= 16.0:
            bmiCategory = "Severely underweight"
        elif bmi >= 16.1 and bmi <= 18.5:
            bmiCategory = "Underweight"
        elif bmi >= 18.6 and bmi <= 25:
            bmiCategory = "Normal"
        elif bmi >= 25.1 and bmi <= 30:
            bmiCategory = "Overweight"
        elif bmi >= 30.1 and bmi <= 35:
            bmiCategory = "Obese"
        
        return bmiCategory
    

    def on_pre_enter(self, *args):    
        super().on_pre_enter(*args)
        print("I'm here")
        user = db.get_user()
        self.user_name.text = user['user_name']
        self.sex.text = user['sex']
        self.age.text = str(user['age'])
        self.user_weight.text = str(user['user_weight'])
        self.user_height.text = str(user['user_height'])
        self.track_goal.text = user['track_goal']
        self.bmi.text = str(user['bmi'])


    def __init__(self, manager = None, **kwargs):
        super().__init__(**kwargs)
        self.manager = manager
        super().on_pre_enter()
        self.display_database()
        print("Enter init")
    
    def display_database(self):
        first_line = db.load()
        if first_line:
            fields = first_line.strip().split(";")
            if len(fields) == 6:
                user_name, sex, age, user_weight, user_height, track_goal = fields
                self.ids.user_name.text = f"Name: {user_name}"
                self.ids.sex.text = f"Sex: {sex}"
                self.ids.age.text = f"Age: {age}"
                self.ids.user_weight.text = f"Weight: {user_weight} kg"
                self.ids.user_height.text = f"Height: {user_height} cm"
                self.ids.track_goal.text = f"Track: {track_goal}"
                bmi = float(user_weight) / ((float(user_height)/100) ** 2)
                bmiCategory = self.identify_bmiCategory(bmi)
                self.ids.bmi.text = f"BMI: {bmi:.2f} - {bmiCategory}"
            else:
                print(f"Invalid line format in file {self.filename}: {first_line}")
        else:
            print("Database is empty.")
    

    def enter_editButton(self):
        self.reset()
        current = self.manager.current = "ProfilePage"

        first_line = db.load()
        if first_line:
            fields = first_line.strip().split(";")
            if len(fields) == 6:
                user_name, sex, age, user_weight, user_height, track_goal = fields
                self.ids.user_name.text = f"Name: {user_name}"
                self.ids.sex.text = f"Sex: {sex}"
                self.ids.age.text = f"Age: {age}"
                self.ids.user_weight.text = f"Weight: {user_weight} kg"
                self.ids.user_height.text = f"Height: {user_height} cm"
                self.ids.track_goal.text = f"Track: {track_goal}"
                bmi = float(user_weight) / ((float(user_height)/100) ** 2)
                bmiCategory = self.identify_bmiCategory(bmi)
                self.ids.bmi.text = f"BMI: {bmi:.2f} - {bmiCategory}"
            else:
                print(f"Invalid line format in file {self.filename}: {first_line}")
        else:
            print("Database is empty.")


    def reset(self): 
        self.user_name.text = "Name: "
        self.sex.text = "Sex: "
        self.age.text = "Age: "
        self.user_weight.text = "Weight: "
        self.user_height.text = "Height: "
        self.track_goal.text = "Track: "
        self.bmi.text = "Bmi: "