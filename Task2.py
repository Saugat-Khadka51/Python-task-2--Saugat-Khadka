#A theme park has these rules: You can ride the roller coaster if you are at least 12 years old AND at least 140 cm tall.
#Write the if-else code for this.

age = int(input("Enter your age: "))
height = int(input("Enter your height in cm: "))
if age>=12 and height >= 140:
    print("You can ride the rollercoaster.")
else:
    print("You can't ride the rollercoaster.")





#Design a Traffic Light System. Given a variable light that can be "red", "yellow", or "green", print the correct instruction. Also handle an invalid color with an error message.

1 == "Red"
2 == 'Yellow'
3 == 'Green'
light = int(input("Enter the traffic light(1-3): "))
match light:
    case 1:
        print("Stop")
    case 2:
        print("Get Ready")
    case 3:
        print("Go")
    case _: print("Write Valid Traffic Light.")





#Write a match statement that takes a number 1–4 and prints the corresponding season:
#1 = spring, 2 = summer, 3 = autumn, 4 = winter.
#Default: "unknown".

number = int(input("Enter the number between 1 to 4: "))
match number:
    case 1:
        print("Spring")
    case 2:
        print("Summer")
    case 3:
        print("Autumn")
    case 4:
        print("Winter")
    case _: print("Invalid month number")





#Write a login system using nested if. Check:
#If username equals "admin"
#Inside that, if password equals "pass123"
#Print appropriate messages for: valid login, wrong password, wrong username.

username = "admin"
password = "pass123"
user = input("Enter the username: ")
new_password = input("Enter the password:")
if user == username and new_password == password:
    print("Valid login")
elif user != username and new_password == password:
    print("Wrong username")
elif user == username and new_password != password:
    print("Wrong password")
else:
    print("Provide correct username and password.")





#Design a Bank Loan Approval System. Approve a loan only if ALL three conditions are met:
#Age is between 21 and 60 (inclusive)
#Monthly income is at least 30,000
#Credit score is at least 700
#If not approved, print which condition failed. If multiple fail, pick the most important one to report.

age = int(input("Enter your age: "))
monthly_income = int(input("Enter your monthly income: "))
credit_score = int(input("Enter your credit score: "))
if age >= 21 and age <= 60 and monthly_income >= 30000 and credit_score >= 700:
    print ("You are eligible for loan.")
elif age < 21 and age > 60 and monthly_income >= 30000 and credit_score >= 700:
    print("You are too young for loan.")
elif age >= 21 and age <= 60 and monthly_income < 30000 and credit_score >= 700:
    print("Your monthly income is too low for loan.")
elif age >= 21 and age <= 60 and monthly_income >= 30000 and credit_score < 700:
    print("Your credit score is too low for loan.")
else:
    print("You do not meet any criteria for loan.")





#You are developing a simple ticket booking system for a movie theatre. The ticket price depends on the age of the person and whether they have a membership card.
#If the person is under 12, the ticket is free.
#If the person is between 12 and 60:
#If they have a membership card, the ticket costs Rs. 150
#If not, the ticket costs Rs. 200
#If the person is above 60, they get a senior citizen discount, and the ticket costs Rs. 100
#Write a Python program using nested if-else to calculate and print the ticket price based on the user's age and membership status.

age = int(input("Enter your age: "))
membership_card = input("Do you have membership card? (yes/no?): ")
if age < 12 and membership_card == "yes" or membership_card == "no":
    print("Your ticket is free.")
elif age >=12 and age <= 60 and membership_card == "yes":
    print("The cost of ticket is Rs. 150.")
elif age >=12 and age <= 60 and membership_card == "no":
    print("The cost of ticket is Rs. 200.")
elif age > 60:
    print("You are qualified for senior citizen discount.")
    print("Your ticket costs Rs. 100.")
else:
    print("Please input your correct data.")






#A company decided to give a bonus of 5% to an employee if his/her years of service is more than 5 years.
#Ask the user for their salary and years of service and print the net bonus amount.

service = int(input("Enter your year of service: "))

if service > 5:
    print("You are eligible for bonus.")
    salary = float(input("Enter your salary: "))
    bonus = 5/100
    net_bonus = salary * bonus
    print(f'Your net bonus is: {net_bonus}')
else:
    print("You are not qualified for bonus.")






#Write a Python program which accepts the radius of a circle from the user and computes the area.

import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius * radius
print(f'The area of the circle is {area}')






#Accept the age, gender ('M', 'F'), and number of days, and display the wages accordingly:
#If age >= 18 and < 30:
#M → 700 per day
#F → 750 per day
#If age >= 30 and <= 40:
#M → 800 per day
#F → 850 per day

age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
days = int(input("Enter number of days you have worked: "))
wage_per_day = 0

if age >= 18 and age < 30 and gender == 'male':
    wage_per_day = 700
    
elif age >= 18 and age < 30 and gender == 'female':
    wage_per_day = 750
   
elif age >= 30 and age <= 40 and gender == 'male':
    wage_per_day = 800

elif age >= 30 and age <= 40 and gender == 'female':
    wage_per_day = 850
   
else:
    print("You are not allowed to work.")

if wage_per_day > 0:
    total_wage = wage_per_day * days
    print(f'Total Wages for {days} days: {total_wage}')






#Accept a number from the user:
#If the number is a multiple of both 3 and 5, print "Fizz Buzz"
#If the number is a multiple of 3 but not 5, print "Fizz"
#If the number is a multiple of 5 but not 3, print "Buzz"
#If the number is not a multiple of 3 or 5, print the number as it is
#number = int(input('Enter a number: '))

if number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
elif number % 5 == 0 and not number%3==0:
    print("Buzz")
elif number % 3 == 0 and not number % 5 ==0:
    print("Fizz")
else:
    print(number)






