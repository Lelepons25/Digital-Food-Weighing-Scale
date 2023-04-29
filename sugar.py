import sqlite3
import pandas as pd

conn = sqlite3.connect("sugar.db")

conn.execute('''
    CREATE TABLE SugarTable (
        food_ID CHAR(100), 
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

conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M021','Honey','Pulot-pukyutan',100,35.6,258,0.1,0.1,64.1,0.1,0.2,63.8,29,6,3.2,0,5,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M022','Ice candy','N/A',100,83.3,66,0,0,16.5,0.2,0,11.7,4,7,0.1,0,6,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M023','Ice drop','N/A',100,79.5,82,0.6,0.2,19.5,0.2,0,14.4,0,0,0,0,7,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M024','Jam, jackfruit & pineapple, cnd','N/A',100,50.2,198,0.7,0.1,48.6,0.4,0.8,34.7,36,5,0.5,0,23,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M025','Jam, mango, cnd','N/A',100,27.8,287,0.9,0.2,70.5,0.6,0.6,50.4,47,12,3.1,0,10,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M026','Jam, pineapple','N/A',100,26.7,298,0.2,1.1,71.7,0.3,1.1,51.1,95,6,14.3,0,9,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M027','Jam, yam','Halaya, ubi',100,24.4,296,7.1,0.4,66.1,2,1.2,52.7,344,94,0.3,0,35,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M028','Jelly, guava','N/A',100,14.5,345,0,0.8,84.5,0.2,1.2,62.4,17,4,0.6,0,37,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M030','Jelly, pineapple','N/A',100,23.2,310,0.1,0.7,75.9,0.1,1.1,56,46,2,0.4,0,33,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M031','Jelly, strawberry','N/A',100,37.4,255,0.1,1,61.4,0.1,0.9,45.7,20,1,0.5,0,27,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M032','Masareal','Mazareal',100,4.7,484,13.9,21.2,59.4,0.8,2.4,49.3,53,158,1.7,0,427,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M033','Marshmallow','N/A',100,20.8,317,3,0.3,75.6,0.3,0.1,54.5,3,8,0.2,0,76,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M034','Milk choc bar, orange crunch','N/A',100,0.9,535,2.7,28.7,66.5,1.2,1,49,182,147,2.8,0,54,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M035','Nata de coco, sweetn','N/A',100,63.7,146,0,0.2,36.1,0,0.8,33.5,12,2,0.5,0,4,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M036','Nata de piña, sweetn','N/A',100,55.1,181,0.1,0.2,44.6,0,0.9,41.4,10,4,0.7,0,5,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M037','Peanut brittle','N/A',100,5.3,493,15,24.2,53.9,1.6,2.4,49,53,172,2,0,424,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M038','Peanut brittle w/ sesame seed','N/A',100,2.6,522,14,27.6,54.4,1.4,2.5,50.3,52,174,1.4,0,436,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M039','Peanut, milk choc-coated','Mani, binalot sa tsokolate gatas',100,2.8,506,13.8,25.2,56,2.2,4.7,37.2,180,179,1.3,0,87,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M040','Polvoron','N/A',100,2.7,469,6.8,16.4,73.6,0.5,1.2,46.2,68,93,3.9,0,194,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M041','Popsicle, choc flvr','N/A',100,79.6,83,0.8,0.5,18.8,0.3,0,14.3,0,27,0.1,0,7,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M042','Sugar, brown','Asukal, pula',100,0.7,398,0.1,0.3,98.7,0.2,0,97.6,148,14,0.4,0,15,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M043','Sugar, crude, pakaskas','Pakaskas',100,10.6,34.6,2.2,0.2,83.9,3.1,0,0,16,94,2.3,0,102,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M044','Sugar, crude, panocha','Panocha',100,5.9,376,0.2,0.4,92.8,0.7,0,92.5,34,54,3.6,0,27,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M045','Sugar, pwdr','Asukal, pulbos/Confectioners sugar',100,0,400,0,0,100,0,0,98,255,3,0.3,0,2,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M046','Sugar, white, refined','Asukal, puti, refinado',100,0.1,400,0,0,99.9,0,0,99.7,0,0,0,0,1,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M047','Syrup','Arnibal',100,22.6,308,0,0.1,76.8,0.5,0,76.6,41,8,1.2,0,61,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M048','Syrup','Pulot',100,29.6,260,1.8,0.4,62.4,5.8,0,0,470,85,17.5,0,33,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M049','Tamarind, candied','Sampalok, candied',93,16.7,335,0.4,0.7,81.7,0.5,0,80.7,62,12,0.4,0,98,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M050','Tamarind, candied','Kundol, candied',100,18.3,327,0.2,0.1,81.2,0.2,1.6,79.1,50,7,1.2,0,96,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M051','Sugar, coconut sap','Coco sugar',100,1.7,385,1.2,0.1,94.8,2.2,0,94.1,8,0,0.6,0,112,0)")
conn.execute("INSERT into SugarTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('M052','Syrup, coconut sap','Coco syrup',100,18.1,321,1,0.1,79.1,1.7,0.6,67.6,2,0,0.4,0,126,0)")

conn.commit()


cur = conn.execute("SELECT * FROM SugarTable")
for row in cur:
    print("FOOD ID = ", row[0])
    print("FOOD NAME = ", row[1])
    print("ALT NAME= ", row[2])
    print("EDIBLE = ", row[3], "\n")
    
print("Records created successfully")
conn.close()