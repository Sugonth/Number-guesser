import random
from os import system as sys
from os import environ as env

def clear(): sys('clear')

username = env["REPL_OWNER"]

print("Hello, " + str(username))
mode = str(input("Choose your difficulty(hard/easy)\n").lower())

number = random.randint(1, 100)

def easy_mode():
    tries = 10
    print("You have " + str(tries) + " tries")
    while True:
        
        guess = int(input("Guess the number"+ "\n"))
        
        if guess > number and tries >= 0:
            tries -= 1
            clear()
            print("The number is lower")
            print("You have " + str(tries) + " tries")
        elif guess < number and tries >= 0:
            tries -= 1
            clear()
            print("The number is higher")
            print("You have " + str(tries) + " tries")
        elif guess == number:
            print("You got the number!!!!!")
            break
        if tries <= 0:
            print("You have ran out of tries")
            print("The number was " + str(number))
            break
        else:
            continue


def hard_mode():
    tries = 5
    print("You have " + str(tries) + " tries")
    while True:
       
        guess = int(input("Guess the number"+ "\n"))
        
        if guess > number and tries >= 0:
            tries -= 1
            clear()
            print("The number is lower")
            print("You have " + str(tries) + " tries")
        elif guess < number and tries >= 0:
            tries -= 1
            clear()
            print("The number is higher")
            print("You have " + str(tries) + " tries")
        elif guess == number:
            print("You got the number!!!!!")
            break
        if tries <= 0:
            print("You have ran out of tries")
            print("The number was " + str(number))
            break
        else:
            continue

if mode == "easy":
    easy_mode()
elif mode == "hard":
    hard_mode()
else:
    print("That is not a valid option")
