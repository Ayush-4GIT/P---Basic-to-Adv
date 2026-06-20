import random
print(r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
number = 0
lets_go = input("Do you want to play the blackjack? (y/n): ").lower()
if lets_go == "y":
    def user():
        user_card1 = random.choice(cards)
        user_cards.append(user_card1)
        user_card2 = random.choice(cards)
        user_cards.append(user_card2)

    user()
    print(user_cards)
    for total in user_cards:
        number += total
    print(f"Your Total is {number}.")

    if number == 21:
        print("BLACKJACK!!!!You win!")
    elif number < 21:
        choice = input("Do you want to 'hit' or 'stand': ").lower()
        if choice == "hit":
            user_card3 = random.choice(cards)
            user_cards.append(user_card3)
            number += user_card3
            print(f"Your New Total is {number}.")
            if number == 21:
                print("BLACKJACK!!!!You win!")
        elif choice == "stand":
            print(f"Your number was {number}")
        else:
            print("Wrong Input!!")

