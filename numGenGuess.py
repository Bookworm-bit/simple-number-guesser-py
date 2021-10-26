import random

parameterSmall = random.randint(0, 10)
parameterLarge = random.randint(11, 50)
number = random.randint(parameterSmall, parameterLarge)
print("Welcome to guess my number! My number is between", parameterSmall, "and", parameterLarge, "Your guess is:")
guess = input("\n")

while(guess == ""):
    print("That is an invalid input!")
    guess = input("Try Again!:\n")

while (int(guess) != number):
    if (int(guess) < number):
        print("Too small!")
        guess = input("Try Again!:\n")
    if (int(guess) > number):
        print("Too big!")
        guess = input("Try Again!:\n")
    
if (int(guess) == number):
    print("You are correct! You win!" )
