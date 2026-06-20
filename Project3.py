import random

print("Welcome to guessing the number game from 1 to 100!!")

while True:
    gs = random.randint(1, 100)
    ch = 7
    guess = 0
    history = []
    #print(gs)  # Cheat code just remove "#" before print.
    while guess < ch:
        try:
            call = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if call < 1 or call > 100:
            print("Enter a number between 1 and 100")
            continue

        history.append(call)
        print("Previous guesses:", history)

        if abs(gs - call) <= 3 and gs != call:
            print("Very close!")

        if gs == call:
            print("Your guess is correct", gs, "is the right number.")
            print("Attempts used:", guess + 1)

            if guess <= 2:
                print("Amazing!")
            elif guess <= 4:
                print("Great job!")
            else:
                print("Good job!")
            break

        elif gs < call:
            if call - gs <= 10:
                print("Slightly high, try low")
            else:
                print("Too high")
            guess += 1

        elif gs > call:
            if gs - call <= 10:
                print("Slightly low, try high")
            else:
                print("Too low")
            guess += 1

        if guess == 3:
            if gs % 2 == 0:
                print("Hint: The number is even.")
            else:
                print("Hint: The number is odd.")

        print("Chances left:", ch - guess)

        if guess == ch:
            print("GAME OVER\nThe answer is", gs, ".")
    restart=input("Do you want to play again? (y/n): ").lower()
    if restart != "y":
        print("Thank you for playing!")
        break
