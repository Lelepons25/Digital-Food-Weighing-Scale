import sqlite3

conn = sqlite3.connect('mp_database\\food_history.db')
cursor = conn.cursor()



cursor.execute('''CREATE TABLE IF NOT EXISTS food_history (foodId TEXT, 
                                                foodName TEXT, 
                                                food_intake INTEGER, 
                                                current_time TEXT, 
                                                current_date TEXT)''')

conn.commit()
conn.close()