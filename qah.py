# *********************************************************
# Program: qah.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL11-13
# Year: 2023/2024 Trimester 1
# Name: AMIRAH NAILOFAR BINTI MUHAMAD HAFIDZ
# ID: 1231102231
# Email: 1231102231@student.mmu.edu.my
# Phone: 011-1001-8080
# *********************************************************

import random
import user
import score
import time
import playsound

# nested dictionary of key-value pair

# question = {
#     """ASCII Art Representing a Subject""": {
#         "answer": "Correct Answer",
#         "hint": "Helpful Hint for the Question"
#     },
#     # Other Question...
# }

# references on nested dictionary: https://www.w3schools.com/python/python_dictionaries_nested.asp
# source of ascii arts: https://www.asciiart.eu/

# short answer questions, answers and hints
question_group1 = {

        """What is this?
            __,__
   .--.  .-"     "-.  .--.
  / .. \/  .-. .-.  \/ .. 
 | |  '|  /   Y   \  |'  | |
 | \   \  \ 0 | 0 /  /   / |
  \ '- ,\.-"`` ``"-./, -' /
   `'-' /_   ^ ^   _\ '-'`
       |  \._   _./  |
       \   \ `~` /   /
        '._ '-=-' _.'
           '~---~'

    """: {"answer": "Monkey", "hint": "Likes to eat bananas."}, 

    """What is this?

       /      \ 
    \  \  ,,  /  / 
     '-.`\()/`.-' 
    .--_'(  )'_--. 
   / /` /`""`\ `\ \ 
    |  |  ><  |  | 
    \  \      /  / 
   _    '.__.'    _\(O)/_ 
_\( )/_            /(_)\  
 /(O)\  //  \\         _ 
       _\\()//_     _\(_)/_ 
      / //  \\ \     /(o)\ 
       | \__/ |

    """: {"answer": "Spider", "hint": "It is an insect, some can be found in homes."}, 
    """What is this?
__                 
'. \                
 '- \               
  / /_         .---.
 / | \\,.\/--.//    )
 |  \//        )/  / 
  \  ' ^ ^    /    )____.----..  6
   '.____.    .___/            \._) 
      .\/.                      )
       '\                       /
       _/ \/    ).        )    (
      /#  .!    |        /\    /
      \  C// #  /'-----''/ #  / 
   .   'C/ |    |    |   |    |     ,
   \), .. .'OOO-'. ..'OOO'OOO-'. ..\(,

    """: {"answer": "Elephant", "hint": "It is the largest animal found on land."},    
    """What is this?
 
       .
      ":"
    ___:____     |"\/"|
  ,'        `.    \  /
  |  O        \___/  |
~^~^~^~^~^~^~^~^~^~^~^~^~

    """: {"answer": "Whale", "hint": "It can swim in the ocean. One of the largest mammal."},    
    """What is this?

          /`·.¸
     /¸...¸`:·
 ¸.·´  ¸   `·.¸.·´)
: © ):´;      ¸  {
 `·.¸ `·  ¸.·´\`·¸)
     `\\´´\¸.·´

    """: {"answer": "Fish", "hint": "It can swim in the ocean."}
}

# MCQ, answers and hints
question_group2 = {
    """What is the main plot device that drives the story in "Jumanji"?
    A. A magical board game
    B. A haunted house
    C. A time-traveling machine
    D. An enchanted forest""": {
        "answer": "A",
        "hint": "Think about the object that causes all the chaos and adventure in the movie. It's something the characters interact with throughout the film."
    }, 

    """Who plays the character Alan Parrish in "Jumanji"?
    A. Tom Hanks
    B. Robin Williams
    C. Brad Pitt
    D. Johnny Depp""": {
        "answer": "B",
        "hint": "The actor known for his comedic roles and heartwarming performances in family movies, particularly in the 1990s."
    },

    """What must the players do to end the game's jungle-themed chaos?
    A. Destroy the game
    B. Find a hidden treasure
    C. Finish the game
    D. Say a magic word""": {
        "answer": "C",
        "hint": "The solution to their problems is directly related to the game itself. What would typically end a board game?."
    },

    """Who directed the first "Jumanji" movie?
    A. Steven Spielberg
    B. Joe Johnston
    C. Tim Burton
    D. George Lucas""": {
        "answer": "B",
        "hint": "The director is not as widely known as Spielberg or Lucas but has directed several other well-known films, including a famous Marvel character's movie."
    },

        """How long was Alan Parrish trapped in the Jumanji game?
    A. 10 years
    B. 26 years
    C. 30 years
    D. 15 years""": {
        "answer": "B",
        "hint": "The number of years he was trapped is a little more than a quarter of a century."
    }
}

# True or False questions, answers and hints
question_group3 = {
    """The first "Jumanji" movie was released in the year 1995. True or False?""": {
        "answer": "True",
        "hint": "Think about the era in which Robin Williams was at the peak of his career in family-oriented films."
    },
    """In the movie, every time the dice is rolled, players are transported into a jungle. True or False?""": {
        "answer": "False",
        "hint": "Consider the setting of the film. Does the setting change with each roll, or does the game bring the jungle elements to the players?"
    },
     """The movie ends with Alan and Sarah throwing the Jumanji board game into a river. True or False?""": {
        "answer": "True",
        "hint": " Consider how the characters might deal with such a dangerous game at the film's conclusion. Would disposing of it in a river make sense?"
    },
    """One of the challenges faced by the characters is a destructive monsoon inside the house. True or False?""": {
        "answer": "True",
        "hint": "Think about the variety of jungle-themed hazards that the game brings to life. Does a monsoon seem like a likely challenge?"
    },
    """Robin Williams' character, Alan Parrish, is an astronaut who returns from space. True or False?""": {
        "answer": "False",
        "hint": "Focus on the main theme of the movie. Does it revolve around space travel or something more mystical?"
    },
}

# function for starting the game
def start_game(choice):
    username = user.register_user(choice)
    user_score = 0

    # Select 5 random questions
    # reference for random sample: https://www.geeksforgeeks.org/python-random-sample-function/
    if choice == '1':
        selected_questions = random.sample(list(question_group1.items()), 5)
    elif choice == '2':
        selected_questions = random.sample(list(question_group2.items()), 5)
    elif choice == '3':
        selected_questions = random.sample(list(question_group3.items()), 5) 
    
    # clear screen 
    print("\u001b[2J")

    # stop previous music
    playsound.music_stop()

    # play sound of pink panther music
    # source: https://www2.cs.uic.edu/~i101/SoundFiles/PinkPanther60.wav
    playsound.music_play("PinkPanther60.wav")

    # print welcome message
    print("=============================================================================\n")
    print("Welcome to the JUMANJI!")
    print("Answer the following questions correctly to score points.")
    print("If you get the answer wrong, you will be given a hint.")
    print("You have to answer correctly on the second try to score points.")
    print("Good luck!\n")
    print("=============================================================================\n")

    # loop through the selected questions
    for question, data in selected_questions:
        print(f"\n{question}")
        user_answer = input("Your answer: ")

        # check if user's answer is correct and give +1 points
        if user_answer.lower() == data["answer"].lower():
            print("Correct!")
            user_score += 1
        
        # if user's answer is wrong, give hint and ask for answer again
        else:
            print("That's not correct.")
            print(f"Hint: {data['hint']}")
            user_answer = input("Try again: ")
            # check if user's answer is correct and give +1 points
            # if user's answer is still wrong, give correct answer
            if user_answer.lower() == data["answer"].lower():
                print("Correct!")
                user_score += 1
            else:
                print("Wrong again. The correct answer was:", data["answer"])

    # save user's score
    score.save_score(username, user_score)
    print(f"\nYour score: {user_score}")

    # sleep for 5 seconds, then go back to main menu
    print("\nReturning to main menu...")
    time.sleep(5.0)