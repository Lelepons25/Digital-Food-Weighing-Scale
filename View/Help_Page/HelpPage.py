from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from functools import partial

import sqlite3


Builder.load_file('/home/pi/Digital-Food-Weighing-Scale/View/Help_Page/HelpPage.kv')

class HelpPage(Screen):
    
    dialog = None
    def __init__(self, manager = None, **kwargs):
        super().__init__(**kwargs)
        self.manager = manager
        self.on_enter()

    def on_enter(self, *args):
        self.add_questions_to_list('help_gettingStarted', self.ids.gs_list)
        self.add_questions_to_list('help_goalSetting', self.ids.goalSetting_list)
        self.add_questions_to_list('help_foodHistory', self.ids.foodHistory_list)

    def add_questions_to_list(self, table_name, list_widget):
        with sqlite3.connect('user_database/userHelp.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT quesID, question FROM {table_name}")
            questions = cursor.fetchall()

            for question in questions:
                quesID = question[0]
                ques_button = MDRectangleFlatButton(
                    text="", 
                    size_hint=(1, None), 
                    height=150, 
                    text_color="black", 
                    line_color="blue"
                )
                ques_label = MDLabel(
                    text=question[1],
                    size_hint=(1, None),
                    size=(ques_button.width, ques_button.height),
                    height=150,
                    halign="left",
                    valign="center",
                    markup=True,
                )
                ques_label.font_size = 11
                ques_button.add_widget(ques_label)
                ques_button.bind(on_press=partial(self.display_helpAnswer, quesID, table_name))
                list_widget.add_widget(ques_button)

    def display_helpAnswer(self, quesID, table_name, instance):
        # Get the label widget that contains the question text
        ques_label = instance.children[0]

        # Get the answer text from the database
        answer = ""
        with sqlite3.connect('user_database/userHelp.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT answer FROM {table_name} WHERE quesID = '{quesID}'")
            answer = cursor.fetchone()[0]

        # If the dialog doesn't exist yet, create it and open it
        if not self.dialog:
            self.dialog = MDDialog(
                title=ques_label.text,
                text=f"{answer}",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        on_release=self.close_dialog,
                    ),
                ],
            )
            self.dialog.open()
        # If the dialog already exists, update its title and text and open it
        else:
            self.dialog.title = ques_label.text
            self.dialog.text = f"{answer}"
            self.dialog.open()





    def close_dialog(self, instance):
        self.dialog.dismiss()
