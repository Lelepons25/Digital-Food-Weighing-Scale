import sqlite3
import pandas as pd

conn = sqlite3.connect("root_products.db")

conn.execute('''
    CREATE TABLE RootProductsTable (
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

conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B001','Cassava','Kamoteng kahoy/Balinghoy',74,63,145,0.6,0.2,35.3,0.9,1.7,1.6,30,41,1.1,0,2,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B002','Cassava, boiled','Kamoteng kahoy/Balinghoy, nilaga',71,71.8,111,0.4,0.1,27.1,0.6,1.3,1.2,10,22,0.3,0,3,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B003','Cassava, yellow','Kamoteng kahoy/Balinghoy, dilaw',85,61,155,0.7,0.2,37.7,0.4,1.7,1.6,37,47,1,0,1.4,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B004','East Indian arrowroot','Yabyaban',85,63.1,144,3.1,0.1,32.6,1.1,2.5,0,19,68,1.1,0,50,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B005','East Indian arrowroot, boiled','Yabyaban, nilaga',100,77.2,88,3.1,0.2,18.5,1,1.5,0,14,57,1.3,0,31,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B006','Palauan','Galiang/Swamp taro',75,61.4,153,0.5,0.2,37.3,0.6,54,0.5,232,10,1.8,0,14,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B007','Potato','Patatas',85,79.9,78,2.4,0.1,16.8,0.8,2.1,0.8,36,49,1.1,0,29,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B008','Potato, boiled','Patatas, nilaga',100,83.8,63,1.7,0.1,13.7,0.7,1.3,0.6,34,44,0.8,0,4,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B009','Sweet potato, purple','Kamote, murado',77,68.1,125,0.6,0.4,29.8,1.1,4.2,5.9,21,40,0.4,0,1,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B010','Sweet potato, purple, boiled','Kamote, murado, nilaga',90,68.6,122,0.6,0.2,29.5,1.1,4,9.1,22,39,0.2,0,43,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B011','Sweet potato, white','Kamote, puti',89,73.5,105,0.7,0.5,24.3,1,3.5,4.9,152,50,1.1,0,3,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B012','Sweet potato, white, boiled','Kamote, puti, nilaga',86,68.8,126,0.4,0.8,29.3,0.7,3.9,9,83,37,0.7,0,42,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B013','Sweet potato, yellow','Kamote, dilaw',88,65.5,135,1.1,0.4,31.8,1.2,4.6,6.3,55,51,0.7,0,4,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B014','Sweet potato, yellow, boiled','Kamote, dilaw, nilaga',86,68.1,128,0.5,0.3,31.7,0.4,4,9.2,30,26,0.4,0,43,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B015','Taro','Gabi',77,64.1,141,2.3,0.2,32.6,0.8,5,0.5,39,62,0.9,0,13,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B016','Taro, boiled','Gabi, nilaga',69,73.4,105,1.5,0.1,24.4,0.6,3.7,0.4,37,41,0.7,0,11,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B017','White spot arum','Pongapong',91,84.4,61,3.1,0.2,11.7,0.6,2.1,0.3,64,42,0.6,0,5,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B018','Yam, Luzon','Pakit/Kamangeg',77,74.7,99,2.5,0.1,22.1,0.6,3.4,0.4,60,41,0.7,0,7,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B019','Yam, nami','Nami/Asiatic bitter yam',86,73.5,105,2.3,0.3,23.3,0.6,3.6,0.4,35,22,1.2,0,8,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B020','Yam, purple','Ubi/Ube',83,74.9,97,1.7,0.2,22.2,1,3.4,0.4,19,44,0.1,0,7,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B021','Yam, purple, boiled','Ubi/Ube, nilaga',74,80.4,77,0.7,0.1,18.2,0.6,2.6,0.3,10,23,0.4,0,5,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B022','Yam, spiny','Tugi/Lesser yam',82,67.3,141,1,2.7,28.2,0.8,4.4,0.5,92,39,1.5,0,10,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B023','Yam, spiny, boiled','Tugi/Lesser yam, nilaga',97,83.8,69,0.4,1.2,14.1,0.5,2.1,0.3,41,11,0.3,0,4,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B024','Yautia','Gabing Cebu',95,68.7,122,0.8,0.1,29.4,1,1.7,0.4,38,53,1.5,0,24,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B025','Arrowroot starch','Uraro starch',100,12.6,351,0.1,0.5,86.4,0.4,3.4,0,33,24,7.2,0,2,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B026','Cassava cake, bibingka','Kamoteng kahoy, bibingka',100,54.4,1814,0.4,0.3,44.1,0.8,1.6,23.9,30,28,3,0,26,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B027','Cassava flour','Kamoteng kahoy, arina',100,9.5,362,1.1,0.7,87.8,0.9,0.9,3.8,84,37,1,0,1,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B028','Cassava fritter','Kamoteng kahoy, maruya',100,20.8,360,0.7,10,66.7,1.8,5,7.8,26,21,0,0,295,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B029','Cassava pudding','Kamoteng kahoy, budin',100,49.3,203,1.2,0.5,48.4,0.6,0,26.8,62,44,0.7,0,261,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B030','Cassava, mashed, w/ sugar & marg','Kamoteng kahoy, linupak',100,55,183,0.4,1.3,42.4,0.9,1.3,13.5,140,27,0.8,0,60,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B031','Cassava, suman','Kamoteng kahoy, suman',100,48.5,210,0.5,1.4,48.9,0.7,1.4,18.9,20,35,2.4,0,6,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B032','East Indian arrowroot starch','Yabyaban starch',100,13.5,348,0.1,0.5,85.8,0.1,3.3,0,56,8,1.5,0,2,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B033','Potato chips, cheese flvr','N/A',100,3,556,6.2,36,51.8,3,5.1,0.3,114,141,1.4,0,720,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B034','Potato, French-fried','French fries',100,37.4,328,3.7,16.8,40.5,1.6,3.9,0.2,15,128,0,0,187,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B035','Tapioca starch ball','Sago/Tapioca pearl',100,15.6,341,0.4,1.1,52.4,0.5,0.5,3.2,88,10,1,0,11,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B036','Tapioca starch ball, boiled','Sago, nilaga/Tapioca pearl, boiled',100,79.3,83,0,0.2,20.3,0.2,0.1,0.8,37,3,0.4,0,3,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B037','Sweet potato, w/ sugar, fried','Kamote cue',100,47.8,239,1.1,6.9,43.1,1.1,4.3,27.4,51,40,1,0,7,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B038','Yam, nami, brined','Nami, inasnan',100,83.3,66,1,0.2,15,0.5,2.2,0.3,15,8,1.2,0,136,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B039','Yam, nami, dried','Nami, tuyo',100,11.5,351,6.6,0.4,80.3,1.2,11.9,1.5,136,56,12.4,0,26,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B040','Yam, purple, pudding','Ubi, maja',100,53.5,187,1.2,0.8,43.8,0.7,1.7,25.1,24,51,3.1,0,12,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B041','Yam, purple, pudding,w/ grtd coconut topping','Ubi, maja, may niyog',100,53,191,1.7,1.2,43.4,0.7,2,25.9,18,47,2.4,0,14,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B042','Yacon tuber, raw','Peruvian ground apple',87,91,35,0.4,0.1,8.1,0.4,0.7,1.6,6,16,0.4,0,27,0)")
conn.execute("INSERT into RootProductsTable (food_ID,foodName,altName,edible,water,kCal,protein,fat,carbo,ash,fiber,sugar,calcium,phos,iron,potassium,sodium,zinc) VALUES ('B043','Sweet potato, orange','-',80,69.6,121,1.1,0.3,28.4,0.6,2.9,5,13,45,0.4,0,83,0)")


conn.commit()

cur = conn.execute("SELECT * FROM RootProductsTable")
for row in cur:
    print("FOOD ID = ", row[0])
    print("FOOD NAME = ", row[1])
    print("ALT NAME= ", row[2])
    print("EDIBLE = ", row[3], "\n")
    
print("Records created successfully")
#conn.close()
