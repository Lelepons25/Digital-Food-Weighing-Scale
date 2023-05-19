from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivy.properties import ObjectProperty
from kivy.uix.vkeyboard import VKeyboard
from kivy.core.window import Window
import sqlite3

Builder.load_file('/home/pi/Digital-Food-Weighing-Scale/View/More_Page/MorePage.kv')

# More Page displays the other categories
class MorePage(Screen):
    
    dialog = None
    input_goalText = None
    
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)
        self.ids.weight_input.text = "9"
        self.manager = manager
        self.on_enter()

        self.input_goalText = MDTextField(
            hint_text="Enter your goal here",
            multiline=False
        )

    
    def on_text_focus(self, widget, value):
        if value and widget is self.input_goalText:
            keyboard = VKeyboard(target=widget, layout='qwerty', size_hint=(0.5, 0.4), pos_hint={"center_x": 0.4, "center_y": 0.2})
            keyboard.bind(on_key_up=self.key_up)
            Window.add_widget(keyboard)
        else:
            for child in Window.children[:]:
                if isinstance(child, VKeyboard):
                    Window.remove_widget(child)

    
    def key_up(self, keyboard, keycode, text, modifiers):
        active_textfield = None 
        if isinstance(keycode, tuple):
            keycode = keycode[1]

        active_textfield = self.input_goalText

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
                active_textfield.insert_text(text)


    def on_enter(self):

        totalIntake = 0
        userIntake = 0 
        conn = sqlite3.connect('/home/pi/Digital-Food-Weighing-Scale/user_database/userDB.db')
        cursor = conn.cursor()
        cursor.execute("SELECT CAST(track_goal AS TEXT) FROM user")
        track_goal = cursor.fetchone()

        connHistory = sqlite3.connect('/home/pi/Digital-Food-Weighing-Scale/mp_database/food_history.db')
        cursorHistory = connHistory.cursor()
        cursorHistory.execute("SELECT food_intake FROM food_history")
        intakes = cursorHistory.fetchall()

        for intake in intakes:
            totalIntake += intake[0]

        if str(track_goal[0]) == "Calories":
            self.ids.tracker.text = "Calorie Intake Tracker"
            
            cursor.execute("SELECT tdee FROM user")
            tdee = cursor.fetchone()

            userIntake = tdee[0] - totalIntake

            # Computation
            self.ids.user_goal.text = f"{tdee[0]} Kcal - {totalIntake} Kcal = {userIntake} remaining" 
            self.ids.user_goal.font_size = 12

        elif str(track_goal[0]) == "Carbohydrates":
            self.ids.tracker.text = "Carbohydrates Intake Tracker"

            cursor.execute("SELECT carbs_min, carbs_max FROM user")
            carbs_min, carbs_max = cursor.fetchone()

            userIntake = carbs_max - totalIntake
            self.ids.user_goal.text = f"{carbs_max} g maximum - {totalIntake} g = {userIntake} remaining"

        connHistory.commit()
        connHistory.close()
        conn.commit()
        conn.close()

    # customize the goal based on the tracker selected
    def confirmation_dialog(self):
        # set the dialog title based on the tracker selected
        if self.ids.tracker.text == "Calorie Intake Tracker":
            dialog_title = "Customize Calorie Intake Goal:"
        elif self.ids.tracker.text == "Carbohydrates Intake Tracker":
            dialog_title = "Customize Minimum Carbohydrate Intake Goal:"

        # Bind on_focus event of each TextInput to on_text_focus()
        self.input_goalText.bind(focus=self.on_text_focus)

        # create the dialog if it does not exist
        if not self.dialog:
            self.dialog = MDDialog(
                title=f"{dialog_title}",
                type="custom",
                content_cls=self.input_goalText,
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        on_release=self.cancel_dialog,
                    ),
                    MDFlatButton(
                        text="SAVE",
                        theme_text_color="Custom",
                        on_release=self.save_custom_goal,
                    ),
                ],
            )
        # open the dialog
        self.dialog.open()

    # cancel the dialog
    def cancel_dialog(self, instance):
        self.dialog.dismiss()

    # save the custom goal in the database
    def save_custom_goal(self, instance):
        goal = self.input_goalText.text

        if goal == "":
            popupMessage("Please enter a goal.")
        elif not goal.isdigit() > 0:
            popupMessage("Please enter a number.")
        else:
        # connect to the database
            with sqlite3.connect('/home/pi/Digital-Food-Weighing-Scale/user_database/userDB.db') as conn:
                cursor = conn.cursor()

                # update the goal based on the tracker selected
                if self.ids.tracker.text == "Calorie Intake Tracker":
                    cursor.execute("UPDATE user SET tdee = ? WHERE track_goal = ?", (goal, "Calories"))
                elif self.ids.tracker.text == "Carbohydrates Intake Tracker":
                    carbs_max = None
                    carbs_max = float(goal) * (0.65/0.45)
                    cursor.execute("UPDATE user SET carbs_min = ?, carbs_max = ? WHERE track_goal = ?", (goal, carbs_max, "Carbohydrates"))

                # commit the changes
                conn.commit()
            
            conn.close()
            self.dialog.dismiss()
            self.manager.generateHomePageScreen()

    def enter_topButton(self, button):
        if button == "Save":
            content = Label(text='Please choose which category \nand what food is being weighed.', halign='center')
            popup = Popup(title='Error', content=content, size_hint=(None, None), size=(400, 200))
            popup.open()
            return
        elif button == "Clear":
            print("Clear")

def popupMessage(message):
    pop = Popup(title = " Invalid Form ",
        content = Label (text = message),
        size_hint = (None, None),
        size = (400, 400)
    )
    pop.open()
