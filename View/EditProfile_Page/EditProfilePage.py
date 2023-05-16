from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivy.metrics import dp
from kivy.core.window import Window
from kivymd.app import MDApp
import sqlite3
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconRightWidget
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout


Builder.load_file('View\EditProfile_Page\EditProfilePage.kv')

class EditProfilePage(Screen):
    

    user_name = ObjectProperty(None)
    sex = ObjectProperty(None)
    age = ObjectProperty(None)
    user_weight = ObjectProperty(None)
    user_height = ObjectProperty(None)
    track_goal = ObjectProperty(None)
    bmi = ObjectProperty(None)
    activity_level = ObjectProperty(None)
    goal_intake = ObjectProperty(None)

    def __init__(self, manager = None, **kwargs):
        super(EditProfilePage, self).__init__(**kwargs)
        self.manager = manager
        self.on_enter()
       

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
    

    def on_enter(self):
        super().on_enter()

        conn = sqlite3.connect("user_database/userDB.db")
        curr = conn.cursor()

        curr.execute("SELECT * FROM user")
        row = curr.fetchone()

        bmi = row[7]
        track_goal = row[5]

        bmiCategory = self.identify_bmiCategory(bmi)

        if row is not None:
            # DISPLAY
            self.user_name.text = f"Name: {row[0]}"
            self.sex.text = f"Sex: {row[1]}"
            self.age.text = f"Age: {row[2]}"
            self.user_weight.text = f"Weight: {row[3]} kg"
            self.user_height.text = f"Height: {row[4]} cm"
            self.track_goal.text = f"Track: {row[5]}"
            self.activity_level.text = f"Activity Level: {row[6]}"
            self.bmi.text = f"BMI: {row[7]:.2f} - {bmiCategory}"

            if track_goal == "Calories":
                self.goal_intake.text = f"Carolie Intake Goal: {int(row[8])} kcal"
            else:
                self.goal_intake.text = f"Carbohydrate Intake range:  \n {int(row[9])} grams - {int(row[10])} grams"
        else:
            print("Database is empty")
        
        conn.commit()
        conn.close()

    def enter_foodExchange(self):
        self.clear_mealPlan()
        self.ids.mp_title.text = "Food Exchange List in Meal Planning"

        # Display the list
        conn = sqlite3.connect('mp_database/mp_foodExchange.db')
        curr = conn.cursor()
        curr.execute("SELECT * FROM mp_foodExchange")
        rows = curr.fetchall()

        foodExchange_card = MDCard(
            size_hint=(None, None),
            size=(360, 290),
            pos_hint={"center_x": 0.5, "top": 0.96},
            padding=5,
            spacing=5,
            elevation=1,
            orientation="vertical",
        )
        
        # create label to display the database contents
        label_text = ""
        for row in rows:
            label_text += f"{row[0]}, Serving Size: {row[9]}\n"
            label_text += f"{row[1]}, Serving Size: {row[10]}\n"
            label_text += f"{row[2]}, Serving Size: {row[11]}\n"
            label_text += f"{row[3]}, Serving Size: {row[12]}\n"
            label_text += f"{row[4]}, Serving Size: {row[13]}\n"
            label_text += f"{row[5]}, Serving Size: {row[14]}\n"
            label_text += f"{row[6]}, Serving Size: {row[15]}\n"
            label_text += f"{row[7]}, Serving Size: {row[16]}\n"
            label_text += f"{row[8]}, Serving Size: {row[17]}\n\n"

        label = MDLabel(text= label_text)
        foodExchange_card.add_widget(label)  # add label to card
        self.ids.card_mealPlan.add_widget(foodExchange_card)  # add card to screen

        conn.commit()
        conn.close()

    def enter_userFoodHistory(self):
        
        self.clear_mealPlan()

        conn = sqlite3.connect('mp_database/food_history.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM food_history")
        food_rows = cursor.fetchall()

    # Add each list item to the layout
        for row in food_rows:
            historyList = ThreeLineAvatarIconListItem(
                IconRightWidget(icon="minus"),
                text=row[4],
                secondary_text=row[1],
                tertiary_text=row[2]
            )
            self.ids.food_history.add_widget(historyList)
        

        conn.close()



    def enter_pinggangPinoy(self):
        self.clear_mealPlan()
        self.ids.mp_title.text = "Pinggang Pinoy"
        
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
            self.day_buttons.append(dayButton)
            dayButton.bind(on_release = self.display_mealPlan)
            self.ids.card_mealPlan.add_widget(dayButton)


    def display_mealPlan(self, instance):
        dayClicked = instance.text

        # remove the day buttons
        for dayButton in self.day_buttons:
            self.ids.card_mealPlan.remove_widget(dayButton)


        conn = sqlite3.connect("user_database/userDB.db")
        cursor = conn.cursor()
        cursor.execute("SELECT sex, age FROM user")
        rows = cursor.fetchall()

        conn.commit()
        conn.close()

        for row in rows:
            sex = row[0]
            age = row[1]
        
        
        conn = None
        curr = None
        table_name = None

        if sex == 'Male':
            if age == 18:
                table_name = 'mp_maleAdol'
            elif age in range(19, 60):
                table_name = 'mp_maleAdults'
            elif age in range(60, 101):
                table_name = 'mp_maleElderly'
        elif sex == 'Female':
            if age == 18:
                table_name = 'mp_femaleAdol'
            elif age in range(19, 60):
                table_name = 'mp_femaleAdults'
            elif age in range(60, 101):
                table_name = 'mp_femaleElderly'
        

        conn = sqlite3.connect("mp_database/mealplan.db")
        curr = conn.cursor()
        if table_name:
            offset = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7'].index(dayClicked)
            curr.execute(f"SELECT * FROM {table_name} LIMIT 1 OFFSET {offset}")
            row = curr.fetchone()


        meal_labels = []

        # Loop through the meal names and descriptions
        meal_names = ['BREAKFAST', 'LUNCH', 'SUPPER', 'SNACK']
        for i, meal_name in enumerate(meal_names):
            meal_label_text = meal_name + '\n\n'
            for j in range(4):
                k = i*4 + j
                if k + 14 < len(row):
                    meal_label_text += row[k] + ' - ' + row[k+14] + '\n'
            meal_label_text += '\n'
            meal_labels.append(MDLabel(
                text=meal_label_text,
                halign="center",
                height=250,
                font_size=12
            ))

        # Create cards for the meal plan and add labels to them
        breakfast_card = MDCard(
            size_hint=(None, None),
            size=(350, 250),
            pos_hint={"center_x": 0.5, "top": 0.96},
            padding=5,
            spacing=5,
            elevation=1,
            orientation="vertical",
        )
        breakfast_card.add_widget(meal_labels[0])
        lunch_card = MDCard(
            size_hint=(None, None),
            size=(350, 250),
            pos_hint={"center_x": 0.5, "top": 0.96},
            padding=5,
            spacing=5,
            elevation=1,
            orientation="vertical",
        )
        lunch_card.add_widget(meal_labels[1])
        supper_card = MDCard(
            size_hint=(None, None),
            size=(350, 250),
            pos_hint={"center_x": 0.5, "top": 0.96},
            padding=5,
            spacing=5,
            elevation=1,
            orientation="vertical",
        )
        supper_card.add_widget(meal_labels[2])
        snack_card = MDCard(
            size_hint=(None, None),
            size=(350, 250),
            pos_hint={"center_x": 0.5, "top": 0.96},
            padding=5,
            spacing=5,
            elevation=1,
            orientation="vertical",
        )
        snack_card.add_widget(meal_labels[3])

        # Add cards to the carousel
        self.ids.carousel.clear_widgets()
        self.ids.carousel.add_widget(breakfast_card)
        self.ids.carousel.add_widget(lunch_card)
        self.ids.carousel.add_widget(supper_card)
        self.ids.carousel.add_widget(snack_card)


    def clear_mealPlan(self):

        # remove the meal plan buttons
        fe_button = self.ids.food_exchange
        pp_button = self.ids.pinggang_pinoy

        self.ids.card_mealPlan.remove_widget(fe_button)
        self.ids.card_mealPlan.remove_widget(pp_button)


    def reset(self): 
        self.user_name.text = "Name: "
        self.sex.text = "Sex: "
        self.age.text = "Age: "
        self.user_weight.text = "Weight: "
        self.user_height.text = "Height: "
        self.track_goal.text = "Track: "
        self.bmi.text = "Bmi: "
        self.activity_level.text = "Activity: "
