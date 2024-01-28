# *********************************************************
# Program: user.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL11-13
# Year: 2023/2024 Trimester 1
# Name: AMIRAH NAILOFAR BINTI MUHAMAD HAFIDZ
# ID: 1231102231
# Email: 1231102231@student.mmu.edu.my
# Phone: 011-1001-8080
# *********************************************************

def register_user(choice):
    # clear screen
    print("\u001b[2J")

    if choice == '1':
        print("""\u001b[44m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~   _____ __               __      ___                                     ______                   ~
~  / ___// /_  ____  _____/ /_    /   |  ____  ______      _____  _____   / ____/___ _____ ___  ___ ~
~  \__ \/ __ \/ __ \/ ___/ __/   / /| | / __ \/ ___/ | /| / / _ \/ ___/  / / __/ __ `/ __ `__ \/ _ \~
~ ___/ / / / / /_/ / /  / /_    / ___ |/ / / (__  )| |/ |/ /  __/ /     / /_/ / /_/ / / / / / /  __/~
~/____/_/ /_/\____/_/   \__/   /_/  |_/_/ /_/____/ |__/|__/\___/_/      \____/\__,_/_/ /_/ /_/\___/ ~ 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\u001b[0m""")
        print("\n"*5)
    elif choice == '2':
        print("""\u001b[44m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~    __  ___      ____  _       __         ________          _               ______                   ~
~   /  |/  /_  __/ / /_(_)___  / /__      / ____/ /_  ____  (_)_______      / ____/___ _____ ___  ___ ~
~  / /|_/ / / / / / __/ / __ \/ / _ \    / /   / __ \/ __ \/ / ___/ _ \    / / __/ __ `/ __ `__ \/ _ \~
~ / /  / / /_/ / / /_/ / /_/ / /  __/   / /___/ / / / /_/ / / /__/  __/   / /_/ / /_/ / / / / / /  __/~
~/_/  /_/\__,_/_/\__/_/ .___/_/\___/    \____/_/ /_/\____/_/\___/\___/    \____/\__,_/_/ /_/ /_/\___/ ~
~                    /_/                                                                              ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\u001b[0m""")
        print("\n"*5)
    elif choice == '3':
        print("""\u001b[44m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~  ______                     ______      __              ______                   ~
~ /_  __/______  _____       / ____/___ _/ /_______      / ____/___ _____ ___  ___ ~
~  / / / ___/ / / / _ \     / /_  / __ `/ / ___/ _ \    / / __/ __ `/ __ `__ \/ _ \~
~ / / / /  / /_/ /  __/    / __/ / /_/ / (__  )  __/   / /_/ / /_/ / / / / / /  __/~
~/_/ /_/   \__,_/\___/    /_/    \__,_/_/____/\___/    \____/\__,_/_/ /_/ /_/\___/ ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\u001b[0m""")
        print("\n"*5)
    username = input("Enter your username: ")
    print(f"Welcome {username}! Let's go Jumanji!!")
    return username