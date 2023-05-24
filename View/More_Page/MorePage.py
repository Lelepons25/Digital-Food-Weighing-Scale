from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.vkeyboard import VKeyboard
from kivy.core.window import Window
import sqlite3
import datetime

from View.Home_page.Homepage import Homepage

Builder.load_file('View\More_Page\MorePage.kv')

# More Page displays the other categories
class MorePage(Screen):
    now_date = StringProperty()
    dialog = None
    input_goalText = None
    
    def __init__(self, manager, **kwargs):
        super().__init__(**kwargs)
        

        self.now_date = datetime.date.today().strftime("%Y%m%d")
        self.ids.weight_input.text = "54"
        self.manager = manager
        self.on_enter()

        self.input_goalText = MDTextField(
            hint_text="Enter your goal here",
            multiline=False
        )

    def on_enter(self):

        # Display food intake tracker
        Homepage.tracker(self)

    def enter_topButton(self, button):
        if button == "Save":
            content = Label(text='Please choose which category \nand what food is being weighed.', halign='center')
            popup = Popup(title='Error', content=content, size_hint=(None, None), size=(400, 200))
            popup.open()
            return
        elif button == "Tare":
            self.ids.weight_input.text = "0"

def popupMessage(message):
    pop = Popup(title = " Invalid Form ",
        content = Label (text = message),
        size_hint = (None, None),
        size = (400, 400)
    )
    pop.open()