
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

import time
import playsound 

# reference for multiple variable write: https://stackoverflow.com/questions/16822016/write-multiple-variables-to-a-file

# reference for file operation: https://www.digitalocean.com/community/tutorials/python-read-file-open-write-delete-copy
# ‘r’: This mode indicates that the file will be open for reading only
# ‘w’: This mode indicates that the file will be open for writing only. If the file containing that name does not exists, it will create a new one
# ‘a’: This mode indicates that the output of that program will be appended to the previous output of that file
# ‘r+’: This mode indicates that the file will be open for both reading and writing

# called by qah.py at the end of the game
# received two variables, which are username and score\
# write the username and score into scoreboard.txt
def save_score(username, score):
    with open("scoreboard.txt", "a") as file:
        file.write(f"{username}: {score}\n")

def view_scoreboard():

    # readlines() is to read all the lines in the file and return them as a list of strings
    # reference: https://www.freecodecamp.org/news/how-to-read-a-file-line-by-line-in-python/

    # read the scoreboard.txt file
    # if there's no scoreboard.txt, FileNotFoundError will be raised and the program will handle it
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

    # tuple of sorted_scores used to store the key-value pair
    # sort the score, highest score at the top
    # reference: https://stackoverflow.com/questions/3766633/how-to-sort-with-lambda-in-python
    # reverse=True is to sort the score in descending order
    # key=lambda x: x[1] is to sort the score based on the second item in the tuple, which is the score
    sorted_scores = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)

    # clear screen
    print("\u001b[2J")

    # stop previous music
    playsound.music_stop()

    # play sound of pink panther music
    # source: https://www2.cs.uic.edu/~i101/SoundFiles/PinkPanther60.wav
    playsound.music_play("PinkPanther60.wav")
    
    # display the scoreboard
    # set background colour : Green
    print("\u001b[42m")
    print("\n"*5)

    # print the title
    print("\n                 \u001b[1m\u001b[42mScoreboard:\u001b[0m\u001b[42m")

    print("")
    count_sorted_score = 1

    # if there's no score recorded, print the message
    if not sorted_scores:
        print("                 \u001b[1mThere are no score recorded.\u001b[0m\u001b[42m")

    # if there's score recorded, print the top player's name and score in bold
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
    
    # animation for the 5 seconds sleep
    for i in range(5, 0, -1):
        # \r is to return the cursor to the beginning of the line for the next print
        # end="" is to prevent the print() function from printing a new line
        print(f"\r                 Returning to main menu in {i} seconds...", end="")
        time.sleep(1)
    
    # screen set to default state
    print("\u001b[0m")

    # clear screen
    print("\u001b[2J")

def reset_scoreboard():
    
    # reset screen
    print("\u001b[2J")

    # stop previous music
    playsound.music_stop()

    # play sound of pink panther music
    # source: https://www2.cs.uic.edu/~i101/SoundFiles/PinkPanther60.wav
    playsound.music_play("PinkPanther60.wav")
    
    # display the scoreboard
    # set background colour : Green
    print("\u001b[42m")
    print("\n"*5)
    print("\n                 \u001b[1m\u001b[4mLeaderboard:\u001b[0m\u001b[42m")
    print("")

    # clear the scoreboard.txt file
    open("scoreboard.txt", "w").close()
    print("                 Scoreboard cleared.")
    print("\n"*5)

    # animation for the 5 seconds sleep
    for i in range(5, 0, -1):
        # \r is to return the cursor to the beginning of the line for the next print
        # end="" is to prevent the print() function from printing a new line
        print(f"\r                 Returning to main menu in {i} seconds...", end="")
        time.sleep(1)

    # screen set to default state
    print("\u001b[0m")

    # clear screen
    print("\u001b[2J")