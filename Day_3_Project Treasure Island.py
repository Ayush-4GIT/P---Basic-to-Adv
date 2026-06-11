print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You wake up stranded on a mysterious island. Your goal is to find the hidden treasure and escape.")
print("You hear strange noises in the jungle.")
Choice_1 = input("Choose which path - Left (L) or Right (R): ")
if Choice_1 == "L":
    print("You discover an old path leading toward the coast.")
    print("Following the path, you reach a beach.")
    Choice_2 = input("What will you  - Get in the Boat (A) or Swim (B): ")
    if Choice_2 == "A":
        print("The boat safely carries you to a nearby island where an ancient temple stands.")
        print("Inside the temple are three glowing doors..")
        Choice_3 = input("Choose a door to open - Red (R) or Green (G) or Yellow(Y): ")
        if Choice_3 == "Y":
            print("CONGRATULATIONS YOU FOUND THE TREASURE!")
        elif Choice_3 == "R":
            print("A trap activates and arrows fly from the walls. GAME OVER!")
        else:
            print("The floor collapses beneath you into a deep pit.. GAME OVER!")
    else:
        print("A strong current pulls you away from shore..GAME OVER!")
else:
    print("You stumble into quicksand and sink. GAME OVER!")


