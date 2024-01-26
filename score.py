# *********************************************************
# Program: score.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL11-13
# Year: 2023/2024 Trimester 1
# Name: AMIRAH NAILOFAR BINTI MUHAMAD HAFIDZ
# ID: 1231102231
# Email: 1231102231@student.mmu.edu.my
# Phone: 011-1001-8080
# *********************************************************

# called by qah.py at the end of the game
# received two variables, which are username and score

import time

# reference for multiple variable write: https://stackoverflow.com/questions/16822016/write-multiple-variables-to-a-file

# reference for file operation: https://www.digitalocean.com/community/tutorials/python-read-file-open-write-delete-copy
# ‘r’: This mode indicates that the file will be open for reading only
# ‘w’: This mode indicates that the file will be open for writing only. If the file containing that name does not exists, it will create a new one
# ‘a’: This mode indicates that the output of that program will be appended to the previous output of that file
# ‘r+’: This mode indicates that the file will be open for both reading and writing

def save_score(username, score):
    with open("scoreboard.txt", "a") as file:
        file.write(f"{username}: {score}\n")

# reference for readline: https://www.freecodecamp.org/news/how-to-read-a-file-line-by-line-in-python/
# reference for try & except: https://stackoverflow.com/questions/34554332/under-which-circumstances-will-the-python-f-readlines-method-fail

def view_scoreboard():
    #
    try:
        with open("scoreboard.txt", "r") as file:
            scores = file.readlines()

    # situation where there's no one played the puzzle yet, hence no scoreboard.txt
    except FileNotFoundError:
        print("No scores recorded yet.")
        return

    # Process the scores
    score_dict = {}
    for line in scores:
        # name and score are two strings that will receive value from each of the line item in scoreboard.txt
        # strip is to remove leading or trailing whitespace if any
        # split is to seperate the line into the two strings, first the name, second the score
        # reference: https://www.freecodecamp.org/news/the-string-strip-method-in-python-explained/
        name, score = line.strip().split(': ')

        # Retrieves the current score for the player "name", otherwise gives 0
        # The score in the text file which is in string, is converted to int
        # score is added effectively cummulate the value of the usernames
        score_dict[name] = score_dict.get(name, 0) + int(score)

    # Sort the score, highest score at the top
    # reference: https://stackoverflow.com/questions/3766633/how-to-sort-with-lambda-in-python
    sorted_scores = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)

    # clear screen
    print("\u001b[2J")
    
    # Display the leaderboard
    # set background colour : Green
    print("\u001b[42m")
    print("\n"*5)
    print("\n                 \u001b[1m\u001b[4mLeaderboard:\u001b[0m\u001b[42m")
    print("")
    count_sorted_score = 1

    # if there's no score recorded, print the message
    if not sorted_scores:
        print("                 \u001b[1mThere are no score recorded.\u001b[0m\u001b[42m")

    for name, score in sorted_scores:
        # set the top player's name and score to be bold)
        if count_sorted_score == 1: 
            print(f"                 \u001b[1m{count_sorted_score}. {name}: {score}\u001b[0m\u001b[42m")
            top_player_name = name
            top_player_score = score
        else: 
            print(f"                 {count_sorted_score}. {name}: {score}")
        count_sorted_score += 1
    print("\n"*5)
    
    # sleep for 5 seconds, then go back to main menu
    print("\n                 Returning to main menu...")
    time.sleep(5.0)
    
    # screen set to default state
    print("\u001b[0m")

    # clear screen
    print("\u001b[2J")

def clear_scoreboard():
    
    # clear screen
    print("\u001b[2J")
    
    # Display the leaderboard
    # set background colour : Green
    print("\u001b[42m")
    print("\n"*5)
    print("\n                 \u001b[1m\u001b[4mLeaderboard:\u001b[0m\u001b[42m")
    print("")
    open("scoreboard.txt", "w").close()
    print("                 Scoreboard cleared.")

    # sleep for 5 seconds, then go back to main menu
    print("\n                 Returning to main menu...")
    time.sleep(5.0)

    # screen set to default state
    print("\u001b[0m")

    # clear screen
    print("\u001b[2J")