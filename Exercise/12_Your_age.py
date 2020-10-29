
'''

Practice Problem 1 (Easy)
The task you have to perform is “Your Age In 2090”.

Problem Statement:-
Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).

Here are a few instructions that you must have to follow:


You are not yet born
You seem to be the oldest person alive
You can also handle any other errors, if possible!

'''

# parth code
#
# yearage = int(input("Enter the age or birth of year\n"))
#
#
#
# if len(str(yearage)) == 4 and (yearage > 1900  and yearage < 2021):
#     current_year = yearage
#     current_age = 2021 - yearage
#     print("You are enter the birth of year")
#     print(f"Your birth of year is {current_year} and age is {current_age}")
#     hundred_year = current_year + 100
#     print(f"you will be hundred in year {hundred_year} old")
# elif len(str(yearage)) <= 3 and (int(yearage)<=100 and int(yearage)>=0):
#     print("You are enter the age")
#     current_age = int(2020) - int(yearage)
#     print(f"Your year is {current_age}")
#     hundred_age = current_age + 100
#     print(f"your age will be hundred in {hundred_age}")
# else:
#     print("your input is incorrect")


# code with harry code

yearAge = int(input("What is your Age/Year of birth\n"))
isAge = False
isYear = False

if len(str(yearAge)) == 4:
    isYear = True

else:
    isAge = True

if(yearAge<1900 and isYear):
    print("You seem to be the oldest person alive")
    exit()

if(yearAge>2019):
    print("You are not yet born")
    exit()

if isAge:
    yearAge = 2019 - yearAge

print(f"You will be 100 years old in {yearAge + 100}")

interestedYear = int(input("Enter the year you want to know your age in\n"))

print(f"You will be {interestedYear - yearAge} years old in {interestedYear}")
