import random

number = random.randrange(1, 100)
guesses = 5
chances = [1, 2, 3, 4, 5]

while(guesses > 0) :
    for guesses in chances :
        guess = int(input("Guess the number : "))
        if(guess > number) :
            print(f"Your guess was too high, try guessing a number lower than {guess}")
        elif(guess < number) :
            print(f"Your guess was too low, try guessing a number higher than {guess}")
        else:
            print("Congrats you won")

    print("You lost")
    print(f"The number was : {number}")
    break