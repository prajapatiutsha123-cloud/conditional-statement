#qno4
username= input("Enter your username: ")
password= input("Enter your password: ")
if username == "admin" and password =="ad123":
      print("Access Granted: Faculty Dashboard.")
elif username == "student" and password =="st2026":
      print("Access Granted: Notes and Practice Questions.")
else:
      print("Invalid Credentials. Please try again.")

#qno5
total = float(input("Enter total purchase amount: "))

if total > 5000:
    has_card = input("Is membership card present? (yes/no): ").lower()
    if has_card == "yes":
        discount = total * 0.30
        final_price = total - discount
        print(f"Total Saved: {discount}")
        print(f"Final: {final_price}")
    else:
        print(f"Total: {total}")
        print("Discount: 0")
else:
    print(f"Total: {total}")
    print("Discount: 0")


#qno6
print("Welcome to the Magic Forest")
choice1 = input("Go NORTH or SOUTH? ").upper()

if choice1 == "NORTH":
    choice2 = input("CROSS THE RIVER or FOLLOW THE PATH? ").upper()
    if choice2 == "FOLLOW THE PATH":
        choice3 = input("CHOOSE: FAIRY, OGRE, or ELF? ").upper()
        if choice3 == "ELF":
            print("YOU WIN")
        else:
            print("GAME OVER")
    else:
        print("CROSS THE RIVER. END.")
else:
    print("GAME OVER")


#qno7
light = input("Enter light color: ").lower()
if light == "red": print("Stop")
elif light == "yellow": print("Slow down")
elif light == "green": print("Go")
else: print("Error: Invalid color")

#qno8
season_num = int(input("Enter number (1-4): "))
match season_num:
    case 1: print("Spring")
    case 2: print("Summer")
    case 3: print("Autumn")
    case 4: print("Winter")
    case _: print("Unknown")

#qno9
age = int(input("Age: "))
income = float(input("Monthly Income: "))
credit = int(input("Credit Score: "))

if age < 21 or age > 60: print("Failed: Age requirement")
elif income < 30000: print("Failed: Income requirement")
elif credit < 700: print("Failed: Credit score requirement")
else: print("Loan Approved!")

#qno10
weight = float(input("Weight: "))
height = float(input("Height: "))
bmi = weight / (height ** 2)

if bmi < 18.5: status = "Underweight"
elif 18.5 <= bmi <= 25: status = "Normal weight"
elif 25 < bmi <= 30: status = "Overweight"
else: status = "Obese"

print(f"Weight: {weight}\nHeight: {height}\nBMI: {bmi:.1f} {status}")

#qno11
age = int(input("Enter age: "))
if age < 12:
    print("Ticket is free")
elif 12 <= age <= 60:
    card = input("Membership card? (y/n): ")
    price = 150 if card == 'y' else 200
    print(f"Price: Rs. {price}")
else:
    print("Price: Rs. 100")

#qno12
salary = float(input("Enter your salary: "))
in_this_company = int(input("how many years has it been ?"))
if in_this_company >=5 :
      print("You are eligible for a raise")
      salary_bonus = (salary * 5)/100
      print(f"your bonus is {salary_bonus}")
else:
        print("You are not eligible for a raise")


#qno13
radius= float(input("Enter the radius of the circle: "))
area= 3.14 * radius ** 2
print(f"The area of the circle is: {area}")

#qno14
age = int(input("Enter your age: "))
gender = int(input("Enter your gender : 0 = male or 1 = female "))
num_days= int(input("Enter the number of days you have worked: "))
if age >= 18 and age <30:
      if gender == 0:
            wage= num_days *700
            print(f"Your wage is {wage}")
      elif gender == 1:
            wage= num_days *750
            print(f"Your wage is {wage}")
elif age >=30 and age <40:
      if gender == 0:
            wage= num_days *800
            print(f"Your wage is {wage}")
      elif gender == 1:
            wage= num_days *850
            print(f"Your wage is {wage}")


#qno15
num = int(input("Enter a number: "))
if num % 3 ==0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0:
    print("Fizz")
else:
    print(num)


#qno16
usage = int(input("Enter your electricity usage in kWh: "))
if usage < 100 and usage >= 0:
      cost= usage *5
      print(f"Your electricity bill is: {cost}")
elif usage >= 100 and usage < 300:
      first_100= 100 * 5
      usage_cost = (usage -100) *8
      print(f"The total cost {first_100 + usage_cost}")
else:
      first_100= 100 * 5
      next_200= 200 *8
      usage_cost = (usage -300) *10
      print(f"The total cost {first_100 + next_200 + usage_cost}")


#qno17
choice=int(input("Choose between rock, paper or scissors: 0 for rock, 1 for paper, 2 for scissors: "))
import random
if choice>=0 and choice<=2:
     computer_choice= random.randint(0,2)

print(f"Computer choice: {computer_choice}")

if choice>=3 or choice<0:
     print("Invalid number, you lose")

elif choice==0 and computer_choice==2:
     print("You win")

elif computer_choice ==0 and choice ==2:
     print("you lose")

elif computer_choice> choice:
     print("you lose")

elif choice>computer_choice:
     print("you win")

elif computer_choice==choice:
     print("it's a draw")


#qno18
num = int(input("Enter a number: "))
if not num > 0:
    print("The number is negative: Invalid")
else:
      if num % 2 == 0:
            print("The number is even")
      else:
            print("the number is odd")


#qno19
total_amount= float(input("Enter the purchase amount: "))
is_member= input("Are you a member? (yes/no): ").lower().startswith("y")
if (total_amount > 1000 and is_member == True):
      after_discount= total_amount + total_amount * 0.2
      print(f"Your total amount is {after_discount})")
elif (total_amount > 1000 and is_member == False):
        after_discount= total_amount + total_amount * 0.1
        print(f"Your total amount is {after_discount})")
else:
      print(f"Your total amount is {total_amount}, there is no discount for you)")



#qno20
weight = float(input("Enter your weight in kg: "))
planet_num = int(input("Enter the planet number (1-7): "))
      
match planet_num:
      case 1:
            print(f"Your Destination weight is {weight*0.38}")
      case 2:
            print(f"Your Destination weight is {weight*0.91}")
      case 3:
            print(f"Your Destination weight is {weight*0.38}")
      case 4:
            print(f"Your Destination weight is {weight*2.53}")
      case 5:
            print(f"Your Destination weight is {weight*1.07}")
      case 6:
            print(f"Your Destination weight is {weight*0.89}")
      case 7:
            print(f"Your Destination weight is {weight*1.14}")
      case _:
            print(f"Invalid Planet Number")


#qno21
sub1= float(input("Enter your marks of subject 1"))
sub2= float(input("Enter your marks of subject 2"))
sub3= float(input("Enter your marks of subject 3"))
sub4= float(input("Enter your marks of subject 4"))
total_marks = sub1+sub2+sub3+sub4
percentage= (total_marks / 400)*100
print(f"The total Marks is {total_marks} and percentage is {percentage} ")
if percentage > 70:
      print("Distinction")
elif percentage >60 and percentage <= 70:
      print("First")
elif percentage > 40 and percentage <=60:
      print("Pass")
else:
      print("Fail")


#qno22
is_valid = True
pin = int(input("Enter your PIN"))
ini_balance=5000
if pin == 123 and is_valid == True:
      num = int(input("Enter [1 : Withdraw, 2 : Checking Balance and 3 : Exit]"))
      if num == 1:
            take= int(input("Enter the withdrawing amount:"))
            if take > 5000:
                  print("Invalid amount")
            else:
                  print(f"Here is your{take}")
                  final_balance = ini_balance - take
                  print(f"Remaining balance is {final_balance}")
      elif num ==2:
            print(f"Balance amount is {ini_balance}")
      elif num ==3:
            print("Thank You for Visiting")
else:
      print("PIN is incorrect or Card isn't fully inserted")


#qno23
floor= int(input("Enter the floor number: "))
weight= int(input("Enter the weight: "))
is_door_closed = True
floor_list= [0,1,2,3,4,5,6,7,8,9,10]
if floor in floor_list:
     if weight <= 500:
          if is_door_closed:
               print("Elevator is moving")
          else:
                print("Please close the door")
     else: 
            print("Weight limit exceeded")
else:
        print("Invalid floor number")
      

#qno24
first_name = input ( "ENter your first name")
if  not first_name:
    print ("first name mustn't be empty")
elif not first_name.isalpha():
        print("first name should be alphabet")
else:    print ("valid name")

last_name = input ("enter your last name ")

if  not last_name:
    print ("last name mustn't be empty")
elif not last_name.isalpha():
        print("last name should be alphabet")
else:    print ("valid name")

email = input("Enter your email")

if not email:
    print ( "email cant be empty")
elif "@" not in email and "." not in email:
    print ("email is not correct")
else:
     print ("valid email")

re_email = input ("enter your email again")

if re_email != email:
    print ("email doesnt match")
else:
        print ("email match")

password = input ("enetr your password")

if len(password) < 6:
    print("Password must be at least 6 characters")
else:
     print("Valid")
