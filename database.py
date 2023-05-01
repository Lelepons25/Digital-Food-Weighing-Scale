import os

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.file_path = os.path.join(os.getcwd(), filename)
        self.user = None
        self.file = None
        first_line = self.load()
        if first_line:
            fields = first_line.strip().split(";")
            if len(fields) == 7:
                user_name, sex, age, user_weight, user_height, track_goal, activity_level= fields
                self.user = {
                    'user_name': user_name,
                    'sex': sex,
                    'age': int(age),
                    'user_weight': float(user_weight),
                    'user_height': float(user_height),
                    'track_goal': track_goal,
                    'activity_level': activity_level
                }
            else:
                print(f"Invalid line format in file {self.filename}: {first_line}")
        else:
            print("Database is empty.")

    def load(self):
        with open(self.filename, "r") as f:
            line = f.readline()
            if line:
                return line
            else:
                return None


    def get_user(self, user_name):
        if self.user and user_name == self.user['user_name']:
            return self.user
        else:
            return None

    def add_user(self, user_name, sex, age, user_weight, user_height, track_goal, activity_level):
        if self.user:
            print("This database can only accept one user.")
            return -1
        else:
            self.user = {
                'user_name': user_name.strip(),
                'sex': sex.strip(),
                'age': int(age),
                'user_weight': float(user_weight),
                'user_height': float(user_height),
                'track_goal': track_goal,
                'activity_level': activity_level
            }
            self.save()
            return 1
        
    def update_user(self, user_name, sex=None, age=None, user_weight=None, user_height=None, track_goal=None, activity_level=None):
        if user_name:
            self.user['user_name'] = user_name.strip()
        if sex:
            self.user['sex'] = sex.strip()
        if age:
            self.user['age'] = int(age)
        if user_weight:
            self.user['user_weight'] = float(user_weight)
        if user_height:
            self.user['user_height'] = float(user_height)
        if track_goal:
            self.user['track_goal'] = track_goal.strip()
        if activity_level:
            self.user['activity_level'] = activity_level.strip()
        
        self.save()
        self.load()
        return 1
    

    def save(self):
        with open(self.filename, "w") as f:
            if self.user:
                f.write(
                    self.user['user_name'] + ";" 
                    + self.user['sex'] + ";" 
                    + str(self.user['age']) + ";" 
                    + str(self.user['user_weight']) + ";" 
                    + str(self.user['user_height']) + ";"
                    + self.user['track_goal'] + ";"
                    + self.user['activity_level'] + "\n" 
                )