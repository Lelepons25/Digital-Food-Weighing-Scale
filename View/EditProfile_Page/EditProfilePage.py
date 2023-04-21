from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from database import DataBase
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel


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

    # Identify which category the user belongs
    def identify_bmiCategory(self, bmi):
        bmiCategory = "Unknown"
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
    
    # Identify which meal to be loaded
    def identify_mealPlan(self):
        print(self.age)

    def __init__(self, manager = None, **kwargs):
        super(EditProfilePage, self).__init__(**kwargs)
        self.manager = manager
        self.display_database()
        self.display_mealPlan()
    
    def display_database(self):
        print("INSIDE")
        first_line = db.load()
        if first_line:
            fields = first_line.strip().split(";")
            print(fields)
            if len(fields) == 6:
                user_name, sex, age, user_weight, user_height, track_goal = fields
                self.user_name.text = f"Name: {user_name}"
                self.sex.text = f"Sex: {sex}"
                self.age.text = f"Age: {age}"
                self.user_weight.text = f"Weight: {user_weight} kg"
                self.user_height.text = f"Height: {user_height} cm"
                self.track_goal.text = f"Track: {track_goal}"
                bmi = float(user_weight) / ((float(user_height)/100) ** 2)
                bmiCategory = self.identify_bmiCategory(bmi)
                self.bmi.text = f"BMI: {bmi:.2f} - {bmiCategory}"
            else:
                print(f"Invalid line format in file {self.filename}: {first_line}")
        else:
            print("Database is empty.")

    
    def display_mealPlan(self):
        
        for i in range(7):
            card = MDCard(
                size_hint=(None, None),
                size=(350, 250),
                pos_hint={"center_x": 0.5, "top": 0.96},
                padding=5,
                spacing=5,
                elevation=1,
                orientation="vertical",
            )
            label = MDLabel(
                text=f"Meal Plan for Day {i+1}",
                halign="center",
                size_hint_y=None,
                height=card.height - 50,
            )
            card.add_widget(label)
            self.ids.carousel.add_widget(card)

        
    def enter_editButton(self):
        self.manager.current = "ProfilePage"
    
    def enter_saveButton(self):
        pass

    def reset(self): 
        self.ids.user_name.text = "Name: "
        self.ids.sex.text = "Sex: "
        self.ids.age.text = "Age: "
        self.ids.user_weight.text = "Weight: "
        self.ids.user_height.text = "Height: "
        self.ids.track_goal.text = "Track: "
        self.ids.bmi.text = "Bmi: "