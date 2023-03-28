import datetime

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            username, password, created = line.strip().split(";")
            self.users[username] = (password, created)

        self.file.close()

    def get_user(self, username):
        if username in self.users:
            return self.users[username]
        else:
            return -1

    def add_user(self, username, password):
        if username.strip() not in self.users:
            self.users[username.strip()] = (password.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Username exists already")
            return -1

    def validate(self, username, password):
        if self.get_user(username) != -1:
            return self.users[username][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]
    
