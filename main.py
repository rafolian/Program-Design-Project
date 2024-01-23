# *********************************************************
# Program: main.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL??
# Year: 2023/24 Trimester 1
# Names: MEMBER_NAME_1 | MEMBER_NAME_2 | MEMBER_NAME_3
# IDs: MEMBER_ID_1 | MEMBER_ID_2 | MEMBER_ID_3
# Emails: MEMBER_EMAIL_1 | MEMBER_EMAIL_2 | MEMBER_EMAIL_3
# Phones: MEMBER_PHONE_1 | MEMBER_PHONE_2 | MEMBER_PHONE_3
# *********************************************************

import user
import score
import qah

def main_menu():
    while True:
        print("=============================================================================")
        print("Welcome to the Mind Puzzler")
        print("1. Start New Game")
        print("2. View Scoreboard")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            qah.start_game()
        elif choice == '2':
            score.view_scoreboard()
        elif choice == '3':
            print("Thanks for playing. Goodbye.")
            print("=============================================================================\n")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
