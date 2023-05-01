from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.popup import Popup
from kivy.uix.label import Label

Builder.load_file('View\Home_page\Homepage.kv')
# Register the CategoryPage class

class Homepage(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.weight_input.text = "9"
        self.ids.tracker.text = "Carbohydrate Intake Tracker"
        self.on_enter()
        # self.ids.cal_tracker.text = f"{progress_value}% Progress"

    
    def on_enter(self):
        # Check which to track from user.txt database
        with open("users.txt", "r") as f:
            line = f.readline()
            fields = line.strip().split(";")
            track_goal = str(fields[5])
        

        if track_goal == "Calorie Deficit" or track_goal == "Default":
            self.ids.tracker.text = "Calorie Deficit Tracker"
        elif track_goal == "Low Carb Diet":
            self.ids.tracker.text = "Low Carb Diet Tracker"
        
   
    def enter_topButton(self, button):
        if button == "Profile":
            self.manager.current = "EditProfilePage"
        elif button == "Save":
            content = Label(text='Please choose which category \nand what food is being weighed.', halign='center')
            popup = Popup(title='Error', content=content, size_hint=(None, None), size=(400, 200))
            popup.open()
            return
        elif button == "Clear":
            print("Clear")

    def update_progress_bar(self):


        # Get a reference to the app object
        app = MDApp.get_running_app()

        # Get the progress value from the app object
        progress_value = app.get_progress_value()

        # Update the progress bar widget
        self.ids.progress_bar.value = progress_value




