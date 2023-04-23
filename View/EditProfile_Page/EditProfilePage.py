from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from database import DataBase
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton

import sqlite3



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

    def __init__(self, manager = None, **kwargs):
        super(EditProfilePage, self).__init__(**kwargs)
        self.manager = manager
        self.display_database()
        # self.display_mealPlan()

    # Identify which category the user belongs
    def identify_bmiCategory(self, bmi):
        if bmi < 0:
            return "Unknown"
        elif bmi <= 16.0:
            return "Severely underweight"
        elif bmi <= 18.5:
            return "Underweight"
        elif bmi <= 25:
            return "Normal"
        elif bmi <= 30:
            return "Overweight"
        else:
            return "Obese"
    
    # Identify which meal to be loaded
    def identify_mealPlan(self):
        print(self.age)

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
                pass
                #print(f"Invalid line format in file {self.filename}: {first_line}")
        else:
            print("Database is empty.")


    def presser(self, instance):
        print("Pressed")
    
    def enter_pinggangPinoy(self):
        pp_button = self.ids.pinggang_pinoy
        # mp_label = self.ids.mp_title
        self.ids.mp_title.text = "Pinggang Pinoy"
        self.ids.card_mealPlan.remove_widget(pp_button)
        # self.ids.card_mealPlan.remove_widget(mp_label)

        
        # Create Button for pinggang pinoy Day 1 - Day 8
        # Create a list to store the day buttons
        self.day_buttons =[] 
        for i in range (1, 8):
            dayButton = MDRectangleFlatButton(id = f'day{i}',
                                            text = f'Day {i}',
                                            size_hint = (0.8, None),
                                            text_color = "black",
                                            line_color = "red",
                                            pos_hint =  {"center_x": .5})
            dayButton.bind(on_press = self.display_mealPlan)
            self.day_buttons.append(dayButton)
            self.ids.card_mealPlan.add_widget(dayButton)

        # Add back button for this card



    def display_mealPlan(self, instance):

        dayClicked = instance.text

        # remove the day buttons
        for dayButton in self.day_buttons:
            self.ids.card_mealPlan.remove_widget(dayButton)

        if dayClicked == "Day 1":
            conn = sqlite3.connect('mp_maleAdol.db')
            curr = conn.cursor()

             # Get the first row from the table
            curr.execute("SELECT * FROM mp_maleAdol LIMIT 1")
            row = curr.fetchone()

            # Create a card for the meal plan
            breakfast_card = MDCard(
                size_hint=(None, None),
                size=(350, 250),
                pos_hint={"center_x": 0.5, "top": 0.96},
                padding=5,
                spacing=5,
                elevation=1,
                orientation="vertical",
            )
            lunch_card = MDCard(
                size_hint=(None, None),
                size=(350, 250),
                pos_hint={"center_x": 0.5, "top": 0.96},
                padding=5,
                spacing=5,
                elevation=1,
                orientation="vertical",
            )
            supper_card = MDCard(
                size_hint=(None, None),
                size=(350, 250),
                pos_hint={"center_x": 0.5, "top": 0.96},
                padding=5,
                spacing=5,
                elevation=1,
                orientation="vertical",
            )
            snack_card = MDCard(
                size_hint=(None, None),
                size=(350, 250),
                pos_hint={"center_x": 0.5, "top": 0.96},
                padding=5,
                spacing=5,
                elevation=1,
                orientation="vertical",
            )


            # Add the meal plan data for each meal
            breakfast_label = MDLabel(
                text="BREAKFAST\n\n" 
                    + row[0] + " - " + row[14] + "\n" 
                    + row[1] + " - " + row[15] + "\n"
                    + row[2] + " - " + row[16] + "\n" 
                    + row[3] + " - " + row[17] + "\n"
                    + "\n",
                halign="center",
                height=breakfast_card.height,
                font_size=12
            )
            breakfast_card.add_widget(breakfast_label)

            lunch_label = MDLabel(
                text="LUNCH\n\n" 
                    + row[4] + " - " + row[18] + "\n" 
                    + row[5] + " - " + row[19] + "\n"
                    + row[6] + " - " + row[20] + "\n" 
                    + row[7] + " - " + row[21] + "\n"
                    + "\n",
                halign="center",
                height=lunch_card.height,
                font_size=12
            )
            lunch_card.add_widget(lunch_label)

            supper_label = MDLabel(
                text="SUPPER\n\n" 
                    + row[8] + " - " + row[22] + "\n" 
                    + row[9] + " - " + row[23] + "\n"
                    + row[20] + " - " + row[24] + "\n" 
                    + row[11] + " - " + row[25] + "\n",
                halign="center",
                height=supper_card.height,
                font_size=12
            )
            supper_card.add_widget(supper_label)

            snack_label = MDLabel(
                text="SNACK\n\n" 
                    + row[12] + " - " + row[26] + "\n" 
                    + row[13] + " - " + row[27] + "\n",
                halign="center",
                height=supper_card.height,
                font_size=12
            )
            snack_card.add_widget(snack_label)

            self.ids.carousel.add_widget(breakfast_card)
            self.ids.carousel.add_widget(lunch_card)
            self.ids.carousel.add_widget(supper_card)  
            self.ids.carousel.add_widget(snack_card)  
                   
        elif dayClicked == "Day 2":
            print("Day 2")
        elif dayClicked == "Day 3":
            print("Day 3")
        elif dayClicked == "Day 4":
            print("Day 4")
        elif dayClicked == "Day 5":
            print("Day 5")
        elif dayClicked == "Day 6":
            print("Day 6")
        elif dayClicked == "Day 7":
            print("Day 7")
  
    def enter_editButton(self):
        self.manager.current = "ProfilePage"
    

    def reset(self): 
        self.user_name.text = "Name: "
        self.sex.text = "Sex: "
        self.age.text = "Age: "
        self.user_weight.text = "Weight: "
        self.user_height.text = "Height: "
        self.track_goal.text = "Track: "
        self.bmi.text = "Bmi: "