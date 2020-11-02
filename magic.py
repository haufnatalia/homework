import random
random_number = random.randint(1, 1000)

choice = "y"
i = 0

while choice == "y":
    print("Hello! Let's play! Guess the number from 1 to 1000!")
    a = int(input( ))
    i += 1
    if a > random_number:
        print("Less")
    if a < random_number:
        print("More")
    if a == random_number:
        print("Congratulations! You guessed it is", a,"Number of attempts", i,"Continue? y/n")

        choice = input( )
        if choice == "n":
            print("Bye")
            break
