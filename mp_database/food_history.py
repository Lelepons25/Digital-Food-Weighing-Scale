import sqlite3

conn = sqlite3.connect('/home/pi/Digital-Food-Weighing-Scale/mp_database/food_history.db')
cursor = conn.cursor()



cursor.execute('''CREATE TABLE IF NOT EXISTS food_history (
                                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                foodId TEXT, 
                                                foodName TEXT, 
                                                food_intake INTEGER, 
                                                current_time TEXT, 
                                                current_date TEXT)''')

conn.commit()
conn.close()