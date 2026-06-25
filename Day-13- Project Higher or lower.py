from Datasets.Day_13 import data
from Datasets.Day_13_logo import logo, vs 
import random 

print(logo)
choice_A = random.choice(data)

score = 0
chance = True

while chance:
    
    print(f"Compare A: {choice_A['name']}, a {choice_A['description']}, from {choice_A['country']}")
    print(vs)
    choice_B = random.choice(data)
    print(f"Compare B: {choice_B['name']}, a {choice_B['description']}, from {choice_B['country']}")

    user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
    if user_input == "A":
        if choice_A['follower_count'] > choice_B['follower_count']:
            score += 1
            print(f"You are right!! Current score {score}")
            print("\n" * 10)
            choice_A = choice_B
        else:
            print(f"Sorry, that's wrong. Final score {score}")
            chance = False
    elif user_input == "B":
        if choice_B['follower_count'] > choice_A['follower_count']:
            score += 1
            print(f"You are right!! Current score {score}")
            print("\n" * 10)
            choice_A = choice_B
        else:
            print(f"Sorry, that's wrong. Final score {score}")
            chance = False
    else:
        print("Invalid input. Try again")


