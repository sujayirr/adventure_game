import time
import random


def print_pause(string):
    print(string)
    time.sleep(2)


def intro():
    location = random.choice(['garage', 'space ship', 'planet',
                              'Alien warehouse', 'NASA secret hideout'])

    print_pause(f"You find yourself at the entrance of a {location} with lots "
                "of tools laying around.")

    print_pause("You suddenly remember that you were in a horrible crash "
                "and you need to get back to your planet.")

    print_pause("Next to you is a file with some strange "
                "papers and some more items in it.")

    print_pause("In front of you is a rocket ship which seems "
                "to be broken.")

    print_pause("Behind you is a door which says DO NOT ENTER")


def check_box(list):
    print_pause("You walk over to the file and check out the box")
    if 'ToolsAndPapers' in list:
        print_pause("You already searched this place. You return to where "
                    "you once were")
        check_area(list)
    else:
        print_pause("You find some amazing tools and blueprints in the "
                    "box which you know will be able to help you fix the ship")
        list.append('ToolsAndPapers')
        check_area(list)


def find_tools(list):
    if 'ToolsAndPapers' in list:
        print_pause("You found the magical tools and blueprints, you "
                    "get started with repairing the ship so you can go home.")
        print_pause("YOU WIN!")
        list = []
        while True:
            play_again = input("Would You like to play again?\n"
                               "Please Enter 'yes' or 'no': ")
            if play_again == 'yes':
                print_pause("You find yourself waking up..")
                check_area(list)
                break
            elif play_again == 'no':
                print_pause("Goodbye for now")
                break
            else:
                print_pause("Please Answer yes or no")

    else:
        print_pause("You check out the rocket ship but you don't "
                    "find anything to fix it with")
        print_pause("You return to the spot you woke up in")
        check_area(list)


def lose():
    print_pause("You walk to the door.")
    print_pause("You walk up to the door the door, stare at the DO "
                "NOT ENTER sign, but open it anyways...")
    print_pause("A huge monster leaps at you!")
    print_pause("YOU LOSE!")
    list = []
    while True:
        play_again = input("Would You like to play again?\n"
                           "Please Enter 'yes' or 'no': ").lower()
        if play_again == 'yes':
            print_pause("You find yourself waking up..")
            check_area(list)
            break
        elif play_again == 'no':
            print_pause("Goodbye for now")
            break
        else:
            print_pause("Please Answer yes or no")


def check_area(list):
    action = input("Enter 1 to go check the files of strange papers\n"
                   "Enter 2 to go to the rocket ship\n"
                   "Enter 3 to enter the door behind you\n"
                   "Please enter 1 2 or 3: ")

    if action == '1':
        check_box(list)
    elif action == '2':
        find_tools(list)
    elif action == '3':
        lose()
    else:
        check_area(list)


def start_game():
    list = []
    intro()
    check_area(list)


start_game()
