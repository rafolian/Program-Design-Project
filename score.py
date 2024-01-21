# *********************************************************
# Program: score.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL??
# Year: 2023/24 Trimester 1
# Names: MEMBER_NAME_1 | MEMBER_NAME_2 | MEMBER_NAME_3
# IDs: MEMBER_ID_1 | MEMBER_ID_2 | MEMBER_ID_3
# Emails: MEMBER_EMAIL_1 | MEMBER_EMAIL_2 | MEMBER_EMAIL_3
# Phones: MEMBER_PHONE_1 | MEMBER_PHONE_2 | MEMBER_PHONE_3
# *********************************************************

# called by qah.py at the end of the game
# received two variables, which are username and score

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
        name, score = line.strip().split(': ')

        # Retrieves the current score for the player "name", otherwise gives 0
        # The score in the text file which is in string, is converted to int
        # score is added effectively cummulate the value
        score_dict[name] = score_dict.get(name, 0) + int(score)

    # Sort the score, highest score at the top
    # reference: https://stackoverflow.com/questions/3766633/how-to-sort-with-lambda-in-python
    sorted_scores = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)

    # Display the leaderboard
    print("\nLeaderboard:")
    for name, score in sorted_scores:
        print(f"{name}: {score}")

def clear_scoreboard():
    open("scoreboard.txt", "w").close()
    print("Scoreboard cleared.")