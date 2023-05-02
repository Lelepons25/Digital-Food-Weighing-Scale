import sqlite3

# create a connection to the database
conn = sqlite3.connect('user_database\\userDB.db')

# create a cursor object
cursor = conn.cursor()

# create the user table
cursor.execute('''CREATE TABLE user
                (user_name TEXT, 
                sex TEXT, 
                age INTEGER, 
                user_weight REAL,
                user_height REAL, 
                track_goal TEXT, 
                activity_level TEXT,
                bmi REAL, 
                tdee REAL,
                carbs_min REAL,
                carbs_max REAL
                )''')


# commit the changes and close the connection
conn.commit()
conn.close()
