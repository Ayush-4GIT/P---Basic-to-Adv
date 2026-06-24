from Datasets.Day_13 import data
import random 

choice_A = random.choice(data)
print(f"Compare A: {choice_A['name']}, a {choice_A['description']}, from {choice_A['country']}")

choice_B = random.choice(data)
print(f"Compare B: {choice_B['name']}, a {choice_B['description']}, from {choice_B['country']}")

user_input = input("Who has more followers? Type 'A' or 'B': ").upper()

