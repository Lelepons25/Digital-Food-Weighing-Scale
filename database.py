import datetime
import os

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.file_path = os.path.join(os.getcwd(), filename)
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            user_name, sex, age, user_weight, user_height, track_goal,  created = line.strip().split(";")
            self.users[user_name] = (sex, age, user_weight, user_height, track_goal, created)

        self.file.close()

    def get_user(self, user_name):
        if user_name in self.users:
            return self.users[user_name]
        else:
            return -1

    def add_user(self, user_name, sex, age, user_weight, user_height, track_goal):
        if user_name.strip() not in self.users:
            self.users[user_name.strip()] = (sex.strip(), 
                                             str(age).strip(), 
                                             str(user_weight).strip(),
                                             str(user_height).strip(),
                                             track_goal.strip(),
                                             DataBase.get_date())
            self.save()
            return 1
        else:
            print("Username exists already")
            return -1


    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" 
                        + self.users[user][0] + ";" # sex
                        + self.users[user][1] + ";" # age
                        + self.users[user][2] + ";" # weight
                        + self.users[user][3] + ";" # height
                        + self.users[user][4] + ";" # track_goal
                        + self.users[user][5] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]
    
