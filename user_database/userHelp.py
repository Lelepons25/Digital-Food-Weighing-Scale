import sqlite3

# create a connection to the database
conn = sqlite3.connect('user_database\\userHelp.db')

# create a cursor object
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS help_gettingStarted
                (
                    quesID TEXT PRIMARY KEY,
                    question TEXT,
                    answer TEXT
                )''')


conn.execute("INSERT INTO help_gettingStarted(quesID, question, answer) VALUES ('A001','How does Digital Food Weighing Scale work?','The Digital Food Weighing Scale identifies your required Calorie/Carb Intake Goal based on your profile information. It monitors your calorie and carbohydrate intake as well as recommend the proper meal plan based on pinggang pinoy intended for the user based on their sex and age. It also has a wide selection of foods from each categories and displays their nutritional facts for you to add a food in your calorie/carb intake.')")
conn.execute("INSERT INTO help_gettingStarted(quesID, question, answer) VALUES ('A002','How do I change my original profile information?','Just simply click the edit button in the profile page and there you can already change your original profile information into another one.')")
conn.execute("INSERT INTO help_gettingStarted(quesID, question, answer) VALUES ('A003','How does Digital Food Weighing Scale calculate my initial goals?','TDEE is the number average number of calories you burn per day. You can accurately estimate your TDEE with your weight, height, age, and activity level. Once you know your TDEE, you can use this number to determine how many calories you should eat every day to lose, gain, or maintain your weight.')")
conn.execute("INSERT INTO help_gettingStarted(quesID, question, answer) VALUES ('A004','How do I change my preferred units of measure?','The unit of measurements are already fixed so it cannot be changed. The height will remain in cm and weight in kilograms, etc.')")
conn.execute("INSERT INTO help_gettingStarted(quesID, question, answer) VALUES ('A005','What is pinggang pinoy?','The Pinggang Pinoy meal plan is a scientifically designed 7-day meal plan that takes into account the age and sex. It is intended to provide a framework for healthy eating, but it should be noted that individual results may vary, and the plan should be used as a guide for food intake rather than a guarantee of outcomes.')")
conn.execute("INSERT INTO help_gettingStarted(quesID, question, answer) VALUES ('A006','What is BMI and how is it calculated?','BMI is also known as body mass index.It is a tool that healthcare providers use to estimate the amount of body fat by using your height and weight measurements. It is calculated by your weight in kg divided by the square of your height in meters.')")
conn.execute("INSERT INTO help_gettingStarted(quesID, question, answer) VALUES ('A007','What is Calories and How is my Calorie Track Goal Determined? ','Calories are the amount of energy released when your body breaks down (digests and absorbs) food. Your calorie track goal is determined based on these information of yours: age, sex, height, weight, physical activity level. ')")
conn.execute("INSERT INTO help_gettingStarted(quesID, question, answer) VALUES ('A008','What is Carbohydrates and How is my Carbohydrate Track Goal Determined? ','Carbohydrates are a nutrient that provides energy and other health benefits. Your carbohydrate track goal is determined still with your profile information: age, sex, height, weight, physical activity level.')")
conn.execute("INSERT INTO help_gettingStarted(quesID, question, answer) VALUES ('A009','Is it safe for users with cardiovascular-related illnesses, diabetes, and pregnant women, to follow themeal plan?','While the pinggang pinoy meal plan is a healty eating guide that is generally considered safe and beneficial for most people ,including those with cardiovascular-related illnesses, diabetes, or gestational diabetes. However, it is important to consult a dietitian or nutritionist for customized meal plan modifications. Pregnant women are also advised to seek the assistance of a dietitian to ensure safety and provide adequate nutrients for the developing fetus.')")
conn.execute("INSERT INTO help_gettingStarted(quesID, question, answer) VALUES ('A010','What if the user is below or above the normal BMI?','The meal plan only serves as a guide and the user  is not required to strictly follow it. But if the user has analarmingly beyond or below normal bmi for their age, They must consult a dietitian for meal plan modification.')")
conn.execute("INSERT INTO help_gettingStarted(quesID, question, answer) VALUES ('A011','In case if I have trouble navigating through the app, or have some concerns, where should I go?','Please click the help button as it contains disclaimers and guidelines about the Digital Food Weighing Scale with Analytics device.')")


cursor.execute('''CREATE TABLE IF NOT EXISTS help_goalSetting
                (
                    quesID TEXT PRIMARY KEY,
                    question TEXT,
                    answer TEXT
                )''')


conn.execute("INSERT INTO help_goalSetting(quesID, question, answer) VALUES ('B001','How do I change incorrect user weight entries?','You can edit your weight in the Profile Page by clicking Profile >  Edit. The program will prompt you to update the information.')")
conn.execute("INSERT INTO help_goalSetting(quesID, question, answer) VALUES ('B002','How is the recommended daily intake of calories and carbohydrates for a healthy diet calculated?','They will get automatically generated based on the sex, age, height, weight and level of physical activity and will be displayed in the profile page.')")
conn.execute("INSERT INTO help_goalSetting(quesID, question, answer) VALUES ('B003','Can I customize my calorie/carbohydrate goal?','To adjust your objective, you can click on the edit button next to the calorie/carbohydrate tracker and modify it according to your preferred calorie/carbohydrate value. However, if you want to switch the type of tracking from calorie to carbohydrates or vice versa, you need to go to your profile and click on the edit button to update your information.')")
conn.execute("INSERT INTO help_goalSetting(quesID, question, answer) VALUES ('B004','How to add a weighed food item to my calorie/carbohydrate intake tracker?','When setting up your profile, users may choose to track either calorie or carbohydrate intake, depending on their individual goals and preferences. To track food intake, users can simply navigate to the homepage and select the appropriate food category for the item they wish to log. Once the food has been selected and weighed, it can be saved to update the food history and calorie/carbohydrate intake tracker.')")
conn.execute("INSERT INTO help_goalSetting(quesID, question, answer) VALUES ('B005','How do I view my food intake?','It tracks the progress of the number of calories and carbohydrates consumed by the user based on the food chosen as percentage.')")


cursor.execute('''CREATE TABLE IF NOT EXISTS help_foodHistory
                (
                    quesID TEXT PRIMARY KEY,
                    question TEXT,
                    answer TEXT
                )''')

conn.execute("INSERT INTO help_foodHistory(quesID, question, answer) VALUES ('C001','Where does the Digital Food Weighing Scale obtain the nutritional data for the food items?','The information provided is based on the Philppine Food Composition Tables Online Database (PhilFCT) containing over 1500 commonly consumed food items in the Philippines')")
conn.execute("INSERT INTO help_foodHistory(quesID, question, answer) VALUES ('C002','How do I figure out the nutritional facts of the food that I weighed?','Find the food amongst the food categories to where the weighed food belongs and once found, click the food and the nutritional information will appear.')")
conn.execute("INSERT INTO help_foodHistory(quesID, question, answer) VALUES ('C003','How can I select a food that I weighed and save it my food history.','You just choose among the 17 food categories of foods to which the weighed food belongs and find it there. Once you found the food, click it and the nutritional facts will be displayed then afterwards click save.')")


# commit the changes and close the connection
conn.commit()
conn.close()
