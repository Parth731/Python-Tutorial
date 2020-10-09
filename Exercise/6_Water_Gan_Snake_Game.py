
# water gan sanke game

import random

lst = ["snake","water","gan"]

chance = 10
no_of_chance = 0
computerPoint = 0
humanPoint = 0

print("water gan snake game\n")

while no_of_chance <  chance:

    inp = input("choose one\n1. snake\n2. water\n3. gan\n")
    inp = inp.lower()
    rand = random.choice(lst)

    if inp == rand:
        print("match Tie both 0 point\n")

    # if user enter snake


    elif inp == "snake" and rand == "water":
        computerPoint = computerPoint + 1
        print(f"your guess {inp} and computer guess {rand}\n")
        print("computer win 1 points\n")
        print(f"your point is {humanPoint} and computer point is {computerPoint}\n")
    elif inp == "snake" and rand == "gan":
        humanPoint = humanPoint + 1
        print(f"your guess {inp} and computer guess {rand}\n")
        print("human win 1 points\n")
        print(f"your point is {humanPoint} and computer point is {computerPoint}\n")

    # if user enter water

    elif inp == "water" and rand == "snake":
        computerPoint = computerPoint + 1
        print(f"your guess {inp} and computer guess {rand}\n")
        print("computer win 1 points\n")
        print(f"your point is {humanPoint} and computer point is {computerPoint}\n")
    elif inp == "water" and rand == "gan":
        humanPoint = humanPoint + 1
        print(f"your guess {inp} and computer guess {rand}\n")
        print("human win 1 points\n")
        print(f"your point is {humanPoint} and computer point is {computerPoint}\n")

# if user enter gan

    elif inp == "gan" and rand == "water":
        computerPoint = computerPoint + 1
        print(f"your guess {inp} and computer guess {rand}\n")
        print("computer win 1 points\n")
        print(f"your point is {humanPoint} and computer point is {computerPoint}\n")
    elif inp == "gan" and rand == "snake":
        humanPoint = humanPoint + 1
        print(f"your guess {inp} and computer guess {rand}\n")
        print("human win 1 points\n")
        print(f"your point is {humanPoint} and computer point is {computerPoint}\n")
    else:
        print("you have wrong input")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance}\n")

print("game over")

if computerPoint == humanPoint:
    print("match is Tie")
elif computerPoint > humanPoint:
    print("you loose\n")
elif computerPoint < humanPoint:
    print("you win")