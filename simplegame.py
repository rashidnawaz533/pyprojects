name = input("Hey type your name\n")
print("Welcome"+ name + "to the game")

game_play = input("do you want to play game enter? yes/no").lower()

if game_play == "yes" or gameplay == "y":
    print("we are going to play")
    direction = input("Do you want to go left or right? ").lower()
    if direction == 'left':
        print("you fell off the cliff game over")
    elif direction == 'right':
        choice = input("ok now u are bridge u want to cross it or dive through water (swim/cross)").lower()
        if choice == "swim":
            print("you were drowned game over")
        else:
            print("You found the gold u won")
    else:
        print("Not a valid reply")
else:
    print("we are not playing")
