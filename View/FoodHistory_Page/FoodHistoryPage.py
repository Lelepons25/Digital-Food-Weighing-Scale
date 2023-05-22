from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconRightWidget
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from functools import partial
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from functools import partial

import sqlite3

Builder.load_file("View\FoodHistory_Page\FoodHistoryPage.kv")

class FoodHistoryPage(Screen):

    dialog = None

    def __init__(self, manager = None, **kwargs):
        super(FoodHistoryPage, self).__init__(**kwargs)
        self.manager = manager
        self.on_enter()
    
    def on_enter(self, *args):
        self.display_foodHistory()
        
    
    def display_foodHistory(self):
            
        conn = sqlite3.connect("mp_database/food_history.db")
        cursor = conn.cursor()


        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        self.day_buttons = []
        if not tables:
            label = MDLabel(text = "No Food History")
            self.ids.food_history.add_widget(label)
        else:
            table_count = len(tables)

            for i in range(table_count):
                dayButtons = MDFlatButton( id = f"day{i}",
                                        text=f"Day {i+1}",
                                        size_hint=(1, 0.1),
                                        text_color="black",
                                        line_color="blue")
                self.day_buttons.append(dayButtons)
                dayButtons.bind(on_press=partial(self.display_FoodValues, table_count=i))
                self.ids.food_history.add_widget(dayButtons)
        
        conn.close()

    def display_FoodValues(self, instance, table_count):

        for dayButtons in self.day_buttons:
            self.ids.food_history.remove_widget(dayButtons)

        table_name = f"food_history_{table_count}"

        conn = sqlite3.connect("mp_database/food_history.db")
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {table_name}")
        food_rows = cursor.fetchall()

        if len(food_rows) == 0:
            label = MDLabel(text = "No Food History")
            self.ids.food_history.add_widget(label)
        else:
        # Add each list item to the layout
            for row in food_rows:
                historyList = ThreeLineAvatarIconListItem(
                    IconRightWidget(icon="minus"),
                    text=row[3],
                    secondary_text=row[1],
                    tertiary_text=f"Food Intake: {row[2]}"
                )

                historyList.foodId = row[0]
                historyList.bind(on_press=lambda historyList, table_name=table_name: self.confirmation_dialog(historyList, table_name))
                self.ids.food_history.add_widget(historyList)
        
        # Computation
        cursor.execute(f"SELECT food_intake FROM {table_name}")
        intakes = cursor.fetchall()

        ########### COMPUTATION
        computeIntake = sum([intake[0] for intake in intakes])

        ########### DISPLAY Food History Information
        
        # Check if the history is empty
        if len(food_rows) == 0:
            self.ids.history_date.text = f"Date Saved: Not Available"
            self.ids.history_intake.text = f"Total Intake: Not Available"
        else:
            self.ids.history_date.text = f"Date Saved: {row[4]}"
            self.ids.history_intake.text = f"Total Intake: {computeIntake}"



        conn.commit()
        conn.close()
    
    def delete_history(self, foodId, table_name):
        conn = sqlite3.connect("mp_database/food_history.db")
        cursor = conn.cursor()

        # Check if the table has only one row
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]

        if count <= 1:
            cursor.execute(f"DROP TABLE {table_name}")
        else:
            cursor.execute(f"DELETE FROM {table_name} WHERE foodId = ?", (str(foodId),))

        popupMessage("Food History Deleted")
        conn.commit()
        conn.close()
        self.dialog.dismiss()
        self.manager.generateFoodHistoryPageScreen()



    def confirmation_dialog(self, instance, table_name):
        if not self.dialog:
            self.dialog = MDDialog(
                title = "Delete Food Intake History?",
                type = "custom",
                buttons = [
                    MDFlatButton(
                        text = "Cancel",
                        theme_text_color = "Custom",
                        on_release = self.cancel_dialog,
                    ),
                    MDFlatButton(
                        text = "Delete",
                        theme_text_color = "Custom",
                        on_release=lambda x: self.delete_history(instance.foodId, table_name)
                    )
                ]
            )
        self.dialog.open() 

    def cancel_dialog(self, instance):
        self.dialog.dismiss()

    def clear_foodHistory(self):
        for dayButtons in self.day_buttons:
            self.ids.card_foodHistory.remove_widget(dayButtons)

def popupMessage(message):
    pop = Popup(title = "Successs",
                content = Label(text = f"{message}"),
                size_hint = (None, None),
                size = (400, 200))
    pop.open()
