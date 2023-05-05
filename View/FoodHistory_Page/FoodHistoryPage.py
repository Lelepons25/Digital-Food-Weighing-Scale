from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconRightWidget
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from functools import partial

import sqlite3

Builder.load_file("View\FoodHistory_Page\FoodHistoryPage.kv")

class FoodHistoryPage(Screen):

    def __init__(self, manager = None, **kwargs):
        super(FoodHistoryPage, self).__init__(**kwargs)
        self.manager = manager
        self.on_enter()
    
    def on_enter(self, *args):
        self.display_food_history()
        
    
    def display_food_history(self):
            
        conn = sqlite3.connect("mp_database/food_history.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM food_history")
        food_rows = cursor.fetchall()

        # Add each list item to the layout
        for row in food_rows:
            historyList = ThreeLineAvatarIconListItem(
                IconRightWidget(icon="minus"),
                text=row[4],
                secondary_text=row[1],
                tertiary_text=f"Food Intake: {row[2]}"
            )

            historyList.foodId = row[0]
            historyList.bind(on_press=self.delete_history)

            self.ids.food_history.add_widget(historyList)

        conn.close()

    def delete_history(self, instance):
        foodId = instance.foodId
        conn = sqlite3.connect("mp_database/food_history.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM food_history WHERE foodId = ?", (str(foodId),))
        popupMessage("Food History Deleted")
        conn.commit()
        conn.close()
        self.manager.generateFoodHistoryPageScreen()

def popupMessage(message):
    pop = Popup(title = "Successs",
                content = Label(text = f"{message}"),
                size_hint = (None, None),
                size = (400, 200))
    pop.open()