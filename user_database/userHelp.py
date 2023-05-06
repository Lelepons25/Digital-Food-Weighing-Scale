import sqlite3

# create a connection to the database
conn = sqlite3.connect('user_database\\userHelp.db')

# create a cursor object
cursor = conn.cursor()

# create the user table
cursor.execute('''CREATE TABLE user_help
                (question TEXT,
                answer TEXT
                )''')




# commit the changes and close the connection
conn.commit()
conn.close()
