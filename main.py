# *********************************************************
# Program: main.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL11-13
# Year: 2023/24 Trimester 1
# Names: AMIRAH NAILOFAR
# IDs: ID
# Emails: EMAIL
# Phones: PHONE
# *********************************************************

import user
import score
import qah

def main_menu():
    while True:
        # clear screen
        print("\u001b[2J")
        # set background colour : Red
        print("\u001b[41m")
        print("""
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                ~       ____  ____  ______    _   __    ______~
                ~      / / / / /  |/  /   |  / | / /   / /  _/~
                ~ __  / / / / / /|_/ / /| | /  |/ /_  / // /  ~
                ~/ /_/ / /_/ / /  / / ___ |/ /|  / /_/ // /   ~
                ~\____/\____/_/  /_/_/  |_/_/ |_/\____/___/   ~
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
        print("\n"*2)        
        print("                 \u001b[1m\u001b[4mWELCOME TO JUMANJI\u001b[0m\u001b[41m")
        print("")
        print("                 1. Start New Short Answer Game")
        print("                 2. Start New Multiple Choice Game")
        print("                 3. Start New True False Game")
        print("                 4. View Scoreboard")
        print("                 5. Exit")
        print("\n"*2)
        choice = input("                 Enter your choice: ")
        print("\u001b[0m")

        if choice == '1':
            qah.start_game(choice)
        elif choice == '2':
            qah.start_game(choice)
        elif choice == '3':
            qah.start_game(choice)
        elif choice == '4':
            score.view_scoreboard()
        elif choice == '5':
            print("Thanks for playing. Goodbye.")
            print("=============================================================================\n")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
