
print("What is Your age ?")
age = int(input())

if age < 18 or age < 7 or age > 70:
    print("You can not drive")
elif age == 18 or age < 7 or age > 70:
    print("You come RTO, we give vehicle test")
elif age > 18 or age < 7 or age > 70:
    print("You can drive")

