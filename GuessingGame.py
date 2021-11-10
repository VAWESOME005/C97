import random
randomNum = random.randint(0,10)
chances = 5
while(chances > 0):
    guess = int(input("Enter your guess: "))

    if(guess == randomNum):
        print("CONGRATULATIONS! YOU GUESSED CORRECTLY WITH", chances, "CHANCES LEFT!")
        break

    elif(guess > randomNum):
        print("Try Again! The number is less than", guess)
        chances = chances - 1
    else:
        print("Try Again! The number is greater than", guess)
        chances = chances - 1

if(chances < 1):
    print("OH NO! YOU'VE LOST! THE NUMBER WAS...", randomNum, "GET BETTER AT GUESSING!")

