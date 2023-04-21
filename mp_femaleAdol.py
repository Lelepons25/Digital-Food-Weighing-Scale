import sqlite3
import pandas as pd

conn = sqlite3.connect("mp_femaleAdol.db")

conn.execute('''
    CREATE TABLE mp_femaleAdol (
    meal1 TEXT, meal2 TEXT, meal3 TEXT, meal4 TEXT, 
    meal5 TEXT, meal6 TEXT, meal7 TEXT, meal8 TEXT, 
    meal9 TEXT, meal10 TEXT, meal11 TEXT, meal12 TEXT, 
    meal13 TEXT, meal14 TEXT, 
    serv1 TEXT, serv2 TEXT, serv3 TEXT, serv4 TEXT, 
    serv5 TEXT, serv6 TEXT, serv7 TEXT, serv8 TEXT, 
    serv9 TEXT, serv10 TEXT, serv11 TEXT, serv12 TEXT, 
    serv13 TEXT, serv14 TEXT
    );''')

conn.execute("INSERT into mp_femaleAdol(meal1,meal2,meal3,meal4,meal5,meal6,meal7,meal8,meal9,meal10,meal11,meal12,meal13, meal14,serv1,serv2,serv3,serv4,serv5,serv6,serv7,serv8,serv9,serv10,serv11,serv12,serv13,serv14) VALUES ('Lakatan','Fried Bangus','Camote Tops Salad with Tomatoes','Rice','Chicken Tinola - Chicken Breast','Vegetables','Rice','Mango','Fried Galunggong','Pinakbet','Rice','Watermelon','AM: Suman sa ibos','PM: Boiled Camote','1 piece of 9x3 cm','1 slice','1-1 ½ cups','1 ½ cups','1 piece','1-1 ½ cups','1 ½ cups','1 slice of 12x7 cm','1 piece small size','1-1 ½ cups','1 ½ cups','1 slice of 12x6x3 cm','1 piece of 8x4x2 cm','½ piece of 11 cm long x 4 ½cm diameter')")
conn.execute("INSERT into mp_femaleAdol(meal1,meal2,meal3,meal4,meal5,meal6,meal7,meal8,meal9,meal10,meal11,meal12,meal13, meal14,serv1,serv2,serv3,serv4,serv5,serv6,serv7,serv8,serv9,serv10,serv11,serv12,serv13,serv14) VALUES ('Pineapple','Chicken Adobo - Chicken Breast','Steamed Carrots, Sayote and Baguio Beans','Rice','Sinigang na Turcillo -Turcillo','Vegetables','Rice','Papaya','Tofu Steak','Chopsuey','Rice','Dalanghita','AM: Boiled Corn','PM: Pancit Guisado','1 slice of 10x6x2cm','1 piece','1-1 ½ cups','1 ½ cups','1 slice','1-1 ½ cups','1-1 ½ cups','1 slice of 10x6x2 cm','1 piece, 6x6x2 cm','1-1 ½ cups','1 ½ cups','2 pieces, 6 cm diameter','1 piece, 12x4 cm','½ cup')")
conn.execute("INSERT into mp_femaleAdol(meal1,meal2,meal3,meal4,meal5,meal6,meal7,meal8,meal9,meal10,meal11,meal12,meal13, meal14,serv1,serv2,serv3,serv4,serv5,serv6,serv7,serv8,serv9,serv10,serv11,serv12,serv13,serv14) VALUES ('Dalandan','Tuna Sandwich with Cabbage and Tomatoes - Flaked Tuna','Cabbage and Tomatoes','Loaf Bread','Beef Steak','Adobong Sitaw','Rice','Pineapple','Fried Chicken Leg,small','Steamed Alugbati and Saluyot','Rice','Rambutan','AM: Kababayan','PM: Kutsinta','2 pieces, 6 cm diameter','2 Tbsps.','1-1 ½ cups','6 slices','1 matchbox size','1-1 ½ cups','1 ½ cups','1 slice of 10x6x2 cm','1 piece','1-1 ½ cups','1 ½ cups','8 pieces, 3 cm diameter each','2 pieces, 4 ½ cm diameter x 1 ½ cm thickness','1 piece, 6 cm diameter x 2 ½ cm')")
conn.execute("INSERT into mp_femaleAdol(meal1,meal2,meal3,meal4,meal5,meal6,meal7,meal8,meal9,meal10,meal11,meal12,meal13, meal14,serv1,serv2,serv3,serv4,serv5,serv6,serv7,serv8,serv9,serv10,serv11,serv12,serv13,serv14) VALUES ('Papaya','Homemade Pork Tocino','Pako Salad','Rice','Ginataang Dalagang Bukid with Pechay - Dalagang Bukid','Pechay','Rice','Red Guava','Beef Bulalo - Lean Beef','Vegetables','Rice','Latundan','AM: Pan de Coco','PM: Suman Cassava','1 slice of 10x6x2 cm','1 matchbox size','1-1 ½ cups','1 ½ cups','1 piece small size','1-1 ½ cups','1 ½ cups','2 pieces, 4 cm diameter','1 matchbox size','1-1 ½ cups','1 ½ cups','1 piece of 9x3 cm','1 piece, 7x6 cm','½ piece of 15x3x2 cm')")
conn.execute("INSERT into mp_femaleAdol(meal1,meal2,meal3,meal4,meal5,meal6,meal7,meal8,meal9,meal10,meal11,meal12,meal13, meal14,serv1,serv2,serv3,serv4,serv5,serv6,serv7,serv8,serv9,serv10,serv11,serv12,serv13,serv14) VALUES ('Mango','Chicken Arroz Caldo with Carrots and Malunggay - Chicken Breast','Vegetables','Rice','Pork Nilaga - Lean Pork','Vegetables','Rice','Boiled Saba','Fried Tilapia','Bulanglang','Rice','Apple','AM: Ensaymada','PM: Puto, white','1 slice of 12x7 cm','1 matchbox size','1-1 ½ cups','1 ½ cups','1 matchbox size','1-1 ½ cups','1 ½ cups','1 piece of 10x4 cm','1 piece small size','1-1 ½ cups','1 ½ cups','1 piece of 6 cm diameter','1 piece of 8 ½ cm diameter x 2 cm thick','1 slice of 9 ½x 3 x 3 ½ cm')")
conn.execute("INSERT into mp_femaleAdol(meal1,meal2,meal3,meal4,meal5,meal6,meal7,meal8,meal9,meal10,meal11,meal12,meal13, meal14,serv1,serv2,serv3,serv4,serv5,serv6,serv7,serv8,serv9,serv10,serv11,serv12,serv13,serv14) VALUES ('Melon Beef & Veggie Patty','Lean Ground Beef ','Vegetables','Pan de sal','Chicken Barbecue - Chicken Breast','Sweet Corn, and Sayote','Rice','Indian Mango','Porkchop','Dinengdeng','Rice','Pear','AM: Spanish Bread','PM: Turon','1 slice of 12x10x3 cm','2 Tbsps. ground beef ½ cup','1-1 ½ cups','6 small pieces','1 piece','1-1 ½ cups','1 ½ cups','1 piece of 6 cm diameter','1 matchbox size','1-1 ½ cups','1 ½ cups','1 piece of 6 cm diameter','1 piece, 10x4 cm','1 piece, 9 ½ x 3 ½ x 1 cm')")
conn.execute("INSERT into mp_femaleAdol(meal1,meal2,meal3,meal4,meal5,meal6,meal7,meal8,meal9,meal10,meal11,meal12,meal13, meal14,serv1,serv2,serv3,serv4,serv5,serv6,serv7,serv8,serv9,serv10,serv11,serv12,serv13,serv14) VALUES ('Latundan','Fried Tanigue','Adobong Kangkong Rice','Rice','Stir-fried Beef with Chinese Cabbage and Cauliflower - Lean Beef','Vegetables','Rice','Lansones','Sinampalukang Manok - Chicken leg, small','Vegetables','Rice','Pomelo','AM: Peanut Butter Sandwich','PM: Banana Cue','1 piece of 9x3 cm','1 slice','1-1 ½ cups','1 ½ cups','1 matchbox size','1-1 ½ cups','1 ½ cups','8 pieces, 4x2 cm each','1 piece','1-1 ½ cups','1 ½ cups','3 segments, 8x4x3 cm each','1 piece loaf bread and 2 tsp. peanut butter','1 piece, 9 ½ x 4 cm')")

conn.commit()

cur = conn.execute("SELECT * FROM mp_femaleAdol")
for row in cur:
    print("DAY = ", row[0])
    print("MEAL TYPE = ", row[1])
    print("FOOD NAME = ", row[2])
    print("SERVING SIZE = ", row[3], "\n")
    
print("Records created successfully")