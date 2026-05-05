# #qno 1
# age = int(input("Enter your age: "))
# height = int(input("Enter your height in cm: "))
# if age >=12 and height >=140:
#     print("You cannot ride the roller coaster:")

# #qno 2
# light = input('enter the traffic ligit color "red", "yellow" or "green":')
# light = light.lower()
# if light == "red":
#    print("Stop")
# elif light == "yellow":
#      print("ready")
# elif light == "green":
#      print("Go")
# else:
#     print("Invalid traffic light color with error message")

# #qno 3
# number = int(input("Enter a number between 1 and 4: "))
# match number:
#     case 1:
#         print("spring")
#     case 2:
#         print("summer")
#     case 3:
#         print("autumn")
#     case 4:
#         print("winter")
#     case _:
#         print("Unknown")

#qno 4
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username == "admin":
#     print("Access Granted")
#     if password == "pass123":
#         print("Access Granted")
#     else:
#         print("password incorrect")
# else:
#     print("username incorrect")      

#qno 5
# age= int(input("Enter your age: "))
# income= int(input("Enter your income: "))
# credit = int(input("Enter your credit score: "))
# if age >= 21 and income >= 30000 and credit >= 700:
#     print("you are eligible for loan")
# elif age >= 21 or age > 60 and income >= 30000 and credit <= 700:
#     print("you are too young for loan.")
# elif age >= 21 and age <= 60 and income < 30000 and credit <= 700:
#     print("your income is too low for loan.")
# elif age >= 21 and age <= 60 and income >= 30000 and credit <= 700:
#     print("your credit score is too low for loan.")
# elif age <= 21 and age <=60 and income <= 30000 and credit >=700:
#     print("your credit score is low for loan.")
# else:
#     print("you are not eligible for loan")

# #qno 6
# age = int(input("Enter your age: "))
# membership_card = input("Do you have a membership card? (yes/no): ")
# if age >= 18 and membership_card.lower() == "yes":
#     print("Your ticket is free.")
# elif age >= 12 and age <=60 and  membership_card =="yes":
#     print("the cost of your ticket is Rs 150.")
# elif age >= 12 and age < 60 and membership_card =="no":
#     print("the cost of your ticket is Rs 200.")
# elif age < 12 and membership_card =="yes":
#     print("the cost of your ticket is Rs 100.")
# else:
#     print("please enter valid input for age and membership card status.")

#qno 7
# salary = int(input("Enter your salary: "))
# services = int(input("Enter your years of service: "))
# bonous = 5/100
# if services >= 5:
#     print(f"you are eligible for a bonous of {bonous * salary}")
# else:
#     print("you are not eligible for bonous")

#qno 8
# radius = float(input("Enter the radius of the circle: "))
# area = 3.14 * radius ** 2
# print(f"The area of the circle is: {area}")

#qno 9
# age = int(input("Enter your age: "))
# gender = input("Enter your gender (male/female): ")
# days = int(input("Enter the number of days you have worked: "))
# if age >= 18 and age <= 30 and gender == "male":
#     wage_per_day = 700
#     print(f"Your wage per day is: {wage_per_day}")
# elif age >= 18 and age <= 30 and gender == "female":
#     wage_per_day = 750
#     print(f"Your wage per day is: {wage_per_day}")
# elif age > 30 and age <= 40 and gender == "male":
#     wage_per_day = 800
#     print(f"Your wage per day is: {wage_per_day}")
# elif age > 30 and age <= 40 and gender == "female":
#     wage_per_day = 850
# else:
#     print("Your given information is wrong.")

#qno 10
# number = int(input("Enter a number: "))
# if number % 2 == 0 and number % 5 == 0:
#     print("FIZZBUZZ")
# elif number % 3 == 0:
#     print("FIZZ")
# elif number % 5 == 0:
#     print("BUZZ")
# else:
#     print(number)

