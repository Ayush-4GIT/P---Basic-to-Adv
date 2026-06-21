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
comp_cards = []
number = 0
number1 = 0
lets_go = input("Do you want to play the blackjack? (y/n): ").lower()
if lets_go == "y":
    def user(two):
        for i in range (two):
            user_card1 = random.choice(cards)
            user_cards.append(user_card1)
    user(2)
    print(f"Your cards are: {user_cards}")
    def computer(two):
        for i in range(two):
            comp_card1 = random.choice(cards)
            comp_cards.append(comp_card1)
    computer(2)
    print(f"Computer cards are [{comp_cards[0]}, ?]")


    for total in user_cards:
        number += total
    print(f"Your Total is {number}.")

    for total1 in comp_cards:
        number1 += total1

    if number == 21 and number1 == 21 :
        print(f"BLACKJACK!!! Computer Won with cards {comp_cards}, You lost with cards!{user_cards}")
    elif number <= 21 and number1 > 21 :
        print(f"BLACKJACK!!! You Won with cards {user_cards}, Computer lost with cards! {comp_cards}")
    elif number > 21 and number1 <= 21 :
        print(f"BLACKJACK!!! Computer Won with cards {comp_cards}, You lost with cards!{user_cards}")
    else:
        choice = input("Draw another card - 'hit' and show cards - 'show': ").lower()
        if choice == "show":
            if number <= number1:
                print(f"Computer Won with cards {comp_cards}, You lost with cards!{user_cards}")
            else:
                print(f"You Won with cards {user_cards}, Computer lost with cards! {comp_cards}")
        elif choice == "hit":
            user_card2 = random.choice(cards)
            user_cards.append(user_card2)
            number += user_card2
            print(user_cards)
            if number == 21:
                print(F"BLACKJACK!!!! You Won with cards {comp_cards}, Computer lost with cards!{user_cards}")
            elif number > 21:
                print(F"BLACKJACK!!!! Computer Won with cards {comp_cards}, You lost with cards!{user_cards}")
            else:
                print("why")

        else:
            print("Wrong Choice")



    # elif number < 21:
    #
    #     chance = True
    #
    #     while chance:
    #         choice = input("Do you want to 'hit' or 'stand': ").lower()
    #
    #         if choice == "hit":
    #             user_card2 = random.choice(cards)
    #             user_cards.append(user_card2)
    #
    #             number += user_card2
    #
    #             print(user_cards)
    #             print("Score:", number)
    #
    #             if number == 21:
    #                 print("BLACKJACK!!!! You win!")
    #                 chance = False
    #
    #             elif number > 21:
    #                 print("You lose! You went over 21.")
    #                 chance = False
    #
    #
    #         elif choice == "stand":
    #             print("You stand with:", number)
    #             chance = False
    #
    #         else:
    #             print("Invalid choice")

        # if choice == "hit":
        #     user_card3 = random.choice(cards)
        #     user_cards.append(user_card3)
        #     number += user_card3
        #     print(f"Your New Total is {number}.")
        #     if number == 21:
        #         print("BLACKJACK!!!!You win!")
        # elif choice == "stand":
        #     print(f"Your number was {number}")
        # else:
        #     print("Wrong Input!!")

