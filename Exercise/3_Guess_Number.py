

hideno = 18
noofguess = 9
totalguess = 9

while True:

    if noofguess:
        inp = int(input("you guess the number\n"))
        if inp < hideno:
            print("You selected number less than hide number\n")
            noofguess = noofguess - 1
            print(noofguess, " no of guesses left")
            continue
        elif inp > hideno:
            print("You selected number greater than hide number\n")
            noofguess = noofguess - 1
            print(noofguess, "no of guesses left")
            continue
        elif inp == hideno:
            print("You selected number and hide number are equal\n")
            print(totalguess - noofguess, " no of guesses he look to finished")
            print(noofguess, "no of guesses left")
            print("you won\n")
            break
    else:
        print("game over ...!!")
        break



