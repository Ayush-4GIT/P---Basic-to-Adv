print(r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
""")

import random
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 to 100")
number = random.choice(range(1,100))
choice = input("Choose your difficulty: Type 'easy' or 'hard': ").lower()

if choice == "easy":
    chance = int(10)
else:
    chance = int(5)
def calculate(attemtps):
    while attemtps > 0:
        print(f"You have {attemtps} attempts remaining to guess the number.")
        user_choice = int(input("Make a guess: "))
        if user_choice > number:
            print("Too High!!")
            print("Guess Again!!")
        elif user_choice < number:
            print("Too Low!!")
            print("Guess Again!!")
        else:
            print(f"You got it! The answer was {number}.")
            return
        attemtps -= 1
    if attemtps == 0:
        print("You've run out of guesses. Refresh the page to run again.")
            
calculate(chance)

