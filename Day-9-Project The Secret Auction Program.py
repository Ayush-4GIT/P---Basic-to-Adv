print(r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

name_price = {}
total_bid = False

while not total_bid:
    # TODO-1: Ask the user for input
    name = input("Please enter your name: ")
    bid_amt = int(input("Please enter your bidding amount: $"))
    # TODO-2: Save data into dictionary {name: price}
    name_price[name] = bid_amt

    # TODO-3: Whether if new bids need to be added
    user_input = input("If any new bidder write 'yes' or else write 'no': ").lower()
    if user_input == "yes":
        print("\n" *20)
    else:
        total_bid = True
    # TODO-4: Compare bids in dictionary

compare = 0
winner = ""
for value in name_price:
    if name_price[value] > compare:
        compare = name_price[value]
        winner = value
print(f"\nThe winner is {winner} with a bid of ${name_price[winner]}")