#qno 1
number= int(input("Enter a number: "))
if number >= 0 and number <= 100:
    print("it belongs between 1 and 100")
else:
    print("it does not belongs between 1 and 100")

#qno 2
number = int(input("Enter a numnber:"))
if number % 2== 0:
    print("it is even number")
else:
    print("it is an odd number")

#qno 3
month_number=1
months={1:"January", 2:"February"}
if month_number in months:
    print(months[month_number])
else:
    print("Invalid month number")

#qno 4
marks = int(input('Enter a marks: '))
if marks >= 80:
   print('Grade: A')
elif marks >60 and marks <=80:
    print('Grade": B')
elif marks >=50 and marks <=60:
     print('Grade: C')
elif marks >=45 and marks <50:
    print('Grade: D')
elif marks >=25 and marks <45:
    print('Grade: E')
else:
    print('Grade: F')

#qno 5
num = int(input("Enter a number:"))
if num % 7 == 0:
 print("It is divisible by 7")
else:
    print("It is not divisible by 7")

#qno 6
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
operator = input('Enter an operator (+, -, *, /:) ')
if operator == '+':
    result = num1 +num2
    print(f'Sum: {result}')
elif operator == '-':
     print(f'Subtraction: {num1 - num2}')
elif operator == '*':
    print(f'Multiplication: {num1 * num2}')
elif operator == '/':
    if num2 !=0:
       print(f'Division {num1 / num2}')
    else:
        print("Error: Division by zero is not allowed.")
else:
    print ("Please input the given instruction.")

#qno7
salary = float(input("Enter your salary"))
Credit_score = int(input('Enter your credit score: '))
if salary >=50000 and Credit_score >=700:
    print("Eligible")
else:
    print("Not Eligible")

#qno 8
number = int(input('Enter a number:')
if number % 3 == 0 and number % 5 == 0:
   print("FrizzBuzz")
elif number % 5 == 0:
     print("Buzz")
elif number % 3 == 0:
     print("Frizz")
 else:
 print(number)

 #qno 9
 ch = input("enter a character:")

 if ch in "aeiouAEIOU":
    print("Vowel")
else:
print("Consonant")


#qno 10
mark = int(input("enter your mark:"))
if mark>=100 and mark<=100:
   #print("a")
elif mark>=80 and mark<=89:
     print("b")
elif mark>=70 and mark<=79:
     print("c")
elif mark<70:
     print("fail")

#qno 11
age = int(input("Enter your age: "))
if age<13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
elif age>19:
    print( "Adult")

#qno 12
a=input ("enter a character or digit:")
if a.isupper():
    print("the given character is in uppercase")
elif a.islower():
     print("the given character is in lowercase")
elif a.isdigit():
      print("it is digital")

#qno 13
action("stop","get ready","go")
color=input("enter red or yellow or green color:")
if color == "red":
   print("stop".capitalized())
elif color == "yellow":
     print("get ready".title())
elif color == "green":
     print("go".capitalized())

#qno 14
age=int(input("enter your age:"))
experience=int(input("enter your experience:"))
if age>18 and experience >=2
    print("eligible")
else:
     print("not eligible")

#qno 15
temperature=input("enter the degree of temperature:")
if temperature>"30°C":
    print("it's hot,stay hydrated!")
elif temperature>"15°C" AND temperature <"30°C":
      print("enjoy weather!")
elif temperature<"15°C":
     print("it is cold,wear warm clothes!")

#qno 16
order=input("enter a dish you want to eat pizza, burger, pasta:")
if order =="pizza:"
   print("the price of pizza is $10")
elif order == "burger":
     print("the price of burger is $7")
elif order == "pasta":
     print("the price of pasta is $8")

#qno 17
height = float(input("enter height in feet:"))

if height >= 6:
    print("selected")
else:
     print("not selected")

#qno 18
age=int(input("enter your age:"))
if age >=18:
    print("you are allowed to watch movie")
elif age<18:
      print("you are not allowed to watch movie")

#qno 19
username = input("enter your username:")
password = input("enter your password:")
if username == "admin" and password == "password123":
  print("Access Granted")
else:
      print("Access Denied")

#qno 20
month = int(input("enter month number (1-12):"))

if month == 12 or month == 1 or month == 2:
   print("Winter")
elif month == 3 or month == 4 or month == 5:
   print("Spring")
elif month == 6 or month == 7 or month == 8:
   print("Summer")
elif month == 9 or month == 10 or month == 11:
   print("Autumn")
else:
   print("Invalid month number")












     

     








