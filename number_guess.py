import random
import os
secret_number = random.randint(0,100)
tries_remaining = 10
last_guess = -1
guessed_correctly = False

while(guessed_correctly == False or tries_remaining > 0):
    os.system('cls' if os.name == 'nt' else 'clear')

    print("=== [Guess the Number] ===")
    if(last_guess == -1):
         print("",end='')
    elif (last_guess > secret_number):
        print(f"Last guess {last_guess} was higher than the secret number!")
    else:
        print(f"Last guess {last_guess} was lower than the secret number!")
    inputValue = input("What is your guess?!\n")
    try:
        guess = int(inputValue)
        if(guess == secret_number):
            guessed_correctly = True
            break
        last_guess = guess
         
        tries_remaining -= 1
    except ValueError:
        print("Unknown action...")

os.system('cls' if os.name == 'nt' else 'clear')
print("=== [Guess the Number] ===")
if(guessed_correctly):
    print(f"You guessed the number! {secret_number}")
else:
    print(f"Uh oh! You didn't get the secret number... {secret_number}")