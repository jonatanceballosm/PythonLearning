print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
win = True
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
decision = input("You're at a crossroad. Where do you want go? Type \"left\" or \"right\"\n")
if decision == "right":
    win = False
elif decision == "left":
    decision = input("You walk down the corridor and find yourself in fron of an ocean.\nDo you swim or wait? Type \"swim\" or \"wait\"\n")
    if decision == "swim":
        win = False
    elif decision == "wait":
        decision = input("Three colored doors suddenly rise from the floor.\nWhich do you choose? Type \"Red\", \"Blue\" or \"Yellow\"\n")
        if decision == "Red":
            win = False
        elif decision == "Blue":
            win = False
        elif decision == "Yellow":
            print("Congrats!")
else:
    win = False
    print("You did not enter a correct input.")

if win:
    print("You discovered the treasure!")
else:
    print("You died, try again.")
