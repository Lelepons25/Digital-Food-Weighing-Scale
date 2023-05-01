import sqlite3


class DataBase:
    def __init__(self, file_path):
        self.conn = sqlite3.connect(file_path)
        self.cursor = self.conn.cursor()
        self.user = None
        self.file_path = file_path
        self.load()

    def load(self):
    # Create the "user" table if it does not exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS user (
                user_name TEXT,
                sex TEXT,
                age INTEGER,
                user_weight REAL,
                user_height REAL,
                track_goal TEXT,
                activity_level TEXT
            )
        """)

        self.cursor.execute("SELECT * FROM user")
        row = self.cursor.fetchone()

        # Check if row is not None before unpacking
        if row is not None:
            (
                user_name,
                sex,
                age,
                user_weight,
                user_height,
                track_goal,
                activity_level,
            ) = row
            self.user = {
                "user_name": user_name,
                "sex": sex,
                "age": age,
                "user_weight": user_weight,
                "user_height": user_height,
                "track_goal": track_goal,
                "activity_level": activity_level,
            }
        else:
            print("Database is empty.")


    def get_user(self, user_name):
        if self.user and user_name == self.user["user_name"]:
            return self.user
        else:
            self.cursor.execute(
                "SELECT * FROM user WHERE user_name = ?", (user_name,)
            )
            row = self.cursor.fetchone()
            if row:
                (
                    user_name,
                    sex,
                    age,
                    user_weight,
                    user_height,
                    track_goal,
                    activity_level,
                ) = row
                return {
                    "user_name": user_name,
                    "sex": sex,
                    "age": age,
                    "user_weight": user_weight,
                    "user_height": user_height,
                    "track_goal": track_goal,
                    "activity_level": activity_level,
                }
            else:
                return None

    def add_user(
        self, user_name, sex, age, user_weight, user_height, track_goal, activity_level
    ):
        if self.user:
            print("This database can only accept one user.")
            return -1
        else:
            self.cursor.execute(
                "INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    user_name,
                    sex,
                    age,
                    user_weight,
                    user_height,
                    track_goal,
                    activity_level,
                ),
            )
            self.conn.commit()
            self.load()
            return 1

    def update_user(
        self,
        user_name,
        sex=None,
        age=None,
        user_weight=None,
        user_height=None,
        track_goal=None,
        activity_level=None,
    ):
        if user_name:
            self.user["user_name"] = user_name.strip()
        if sex:
            self.user["sex"] = sex.strip()
        if age:
            self.user["age"] = int(age)
        if user_weight:
            self.user["user_weight"] = float(user_weight)
        if user_height:
            self.user["user_height"] = float(user_height)
        if track_goal:
            self.user["track_goal"] = track_goal.strip()
        if activity_level:
            self.user["activity_level"] = activity_level.strip()

        self.cursor.execute(
            "UPDATE user SET sex = ?, age = ?, user_weight = ?, user_height = ?, track_goal = ?, activity_level = ? WHERE user_name = ?",
            (
                self.user["sex"],
                self.user["age"],
                self.user["user_weight"],
                self.user["user_height"],
                self.user["track_goal"],
                self.user["activity_level"],
                self.user["user_name"],
            ),
        )
        self.conn.commit()
