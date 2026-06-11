rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
signs = [rock, paper, scissors]
user_input = int(input("What will you choose? 0 = Rock, 1 = Paper, 2 = Scissors: \n"))
if user_input > 2:
    print("Invalid input. Pleases enter a number between 0 and 2")
else:
    print(signs[user_input])
    comp_choice = random.randint(0,2)
    print(f"Computer chose {comp_choice}")
    print(signs[comp_choice])
    if user_input == comp_choice:
        print("It's a tie!")
    elif user_input == 0 and comp_choice == 2:
        print("You Won!!")
    elif user_input == 2 and comp_choice == 0:
        print("Computer Won!!")
    elif user_input > comp_choice:
        print("You Won!!")
    elif user_input < comp_choice:
        print("Computer Won!!")


