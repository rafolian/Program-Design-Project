# *********************************************************
# Program: main.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL11-13
# Year: 2023/2024 Trimester 1
# Name: AMIRAH NAILOFAR BINTI MUHAMAD HAFIDZ
# ID: 1231102231
# Email: 1231102231@student.mmu.edu.my
# Phone: 011-1001-8080
# *********************************************************

import user
import score
import qah
import playsound

# Reference for ANSI escape code for colour and other actions :https://saturncloud.io/blog/how-to-print-colored-text-to-the-terminal/

# Colour codes for text
# Black: \u001b[30m
# Red: \u001b[31m
# Green: \u001b[32m
# Yellow: \u001b[33m
# Blue: \u001b[34m
# Magenta: \u001b[35m
# Cyan: \u001b[36m
# White: \u001b[37m

# Colour codes for background
# Black: \u001b[40m
# Red: \u001b[41m
# Green: \u001b[42m
# Yellow: \u001b[43m
# Blue: \u001b[44m
# Magenta: \u001b[45m
# Cyan: \u001b[46m
# White: \u001b[47m

# Other action codes
# Clear Screen: \u001b[2J
# Bold: \u001b[1m
# Underline: \u001b[4m
# Blink: \u001b[5m
# Reset: \u001b[0m]]

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
        playsound.music_play("StarWars60.wav")
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
