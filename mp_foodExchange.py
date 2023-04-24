import sqlite3
import pandas as pd

conn = sqlite3.connect("mp_foodExchange.db")

conn.execute('''
    CREATE TABLE mp_foodExchange (
    meal1 TEXT, meal2 TEXT, meal3 TEXT, meal4 TEXT, 
    meal5 TEXT, meal6 TEXT, meal7 TEXT, meal8 TEXT, 
    meal9 TEXT,
    serv1 TEXT, serv2 TEXT, serv3 TEXT, serv4 TEXT, 
    serv5 TEXT, serv6 TEXT, serv7 TEXT, serv8 TEXT, 
    serv9 TEXT
    );''')


conn.execute("INSERT into mp_foodExchange(meal1,meal2,meal3,meal4,meal5,meal6,meal7,meal8,meal9,serv1,serv2,serv3,serv4,serv5,serv6,serv7,serv8,serv9) VALUES ('1 cup of rice','1 cup of cooked vegetables','1 matchbox size of beef and pork','1 small chicken leg','1 medium chicken leg','1 matchbox size of chicken breast','1 small size fish','1 slice of fish','1 medium size fish','160 g','90 g','30g','30 g','45 g','30 g','35 g','35 g','55 g')")


conn.commit()
