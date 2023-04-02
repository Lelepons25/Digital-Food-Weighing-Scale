import sqlite3
import pandas as pd

conn = sqlite3.connect("food_mixtures.db")

#CREATE TABLE
conn.execute('''
    CREATE TABLE FoodMixturesTable (
        food_ID CHAR(100) PRIMARY KEY, 
        foodName CHAR(100),
        altName CHAR(100),
        edible INTEGER NOT NULL,
        water INTEGER NOT NULL,
        kCal REAL,
        protein INTEGER NOT NULL,
        fat INTEGER NOT NULL,
        carbo INTEGER NOT NULL,
        ash INTEGER NOT NULL,
        fiber INTEGER NOT NULL, 
        sugar INTEGER NOT NULL,
        calcium INTEGER NOT NULL,
        phos INTEGER NOT NULL,
        iron INTEGER NOT NULL,
        potassium INTEGER NOT NULL,
        sodium INTEGER NOT NULL,
        zinc INTEGER NOT NULL);''')


conn.execute("INSERT into FoodMixturesTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('T001','Azolla pinnata','N/A',100,95.3,18,1.4,0.4,2.1,0.8,1.9,0,111,28,14.9,0,41,0)")
conn.execute("INSERT into FoodMixturesTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('T002','Baking powder','N/A',100,10.4,166,0.2,0.3,40.7,48.4,0.2,0,222,22,0,0,9997,0)")
conn.execute("INSERT into FoodMixturesTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('T004','Ceylon moss/Agar-agar bar','Gulaman',100,17.9,311,2.6,0.3,74.5,4.7,6.9,2.7,488,28,27,0,92,0)")
conn.execute("INSERT into FoodMixturesTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('T005','Coffee creamer, non-dairy','N/A',100,1.6,390,4.1,0.7,91.9,1.7,0,55.3,34,88,0.9,0,105,0)")
conn.execute("INSERT into FoodMixturesTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('T006','Chlorella','N/A',100,7,351,53.3,4.9,23.4,11.4,12.4,0.4,602,2019,514,0,0,0)")
conn.execute("INSERT into FoodMixturesTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('T007','Gelatin powder','N/A',100,12.4,351,85.4,1,0,1.4,0,0,351,42,4,0,197,0)")
conn.execute("INSERT into FoodMixturesTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('T008','Rice washing','Hugas-bigas',100,98.6,6,0.1,0.2,1,0.1,0,0,22,16,0.3,0,0,0)")
conn.execute("INSERT into FoodMixturesTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('T009','Yeast, bakers, active, dry','Lebadura, bakers tuyo',100,6.2,363,37.2,1.3,50.5,4.8,0,0,102,0,1,0,0,0)")
conn.execute("INSERT into FoodMixturesTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('T012','Locust','Balang',81,66.3,147,13.7,4.3,13.4,2.3,0,0,102,0,1,0,0,0)")


conn.commit()


cur = conn.execute("SELECT * FROM FoodMixturesTable")
for row in cur:
    print("FOOD ID = ", row[0])
    print("FOOD NAME = ", row[1])
    print("ALT NAME= ", row[2])
    print("EDIBLE = ", row[3], "\n")
    
print("Records created successfully")
conn.close()