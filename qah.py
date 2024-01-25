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

import random
import user
import score
import time

# nested dictionary of key-value pair

# questions = {
#     """ASCII Art Representing a Subject""": {
#         "answer": "Correct Answer",
#         "hint": "Helpful Hint for the Question"
#     },
#     # Other Question...
# }

# references on nested dictionary: https://www.w3schools.com/python/python_dictionaries_nested.asp
# source of ascii arts: https://www.asciiart.eu/

questions = {

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
   .   'C/ |    |    |   |    |abc  ,
   \), .. .'OOO-'. ..'OOO'OOO-'. ..\(,

    """: {"answer": "Keyboard", "hint": "It has many letters."}, 

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
 jgs  / //  \\ \     /(o)\ 
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
   .   'C/ |    |    |   |    |mrf  ,
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

def start_game(choice):
    username = user.register_user(choice)
    user_score = 0

    # Select 5 random questions
    # reference for random sample: https://www.geeksforgeeks.org/python-random-sample-function/
    selected_questions = random.sample(list(questions.items()), 5)

    print("=============================================================================\n")

    for question, data in selected_questions:
        print(f"\n{question}")
        user_answer = input("Your answer: ")

        if user_answer.lower() == data["answer"].lower():
            print("Correct!")
            user_score += 1
        else:
            print("That's not correct.")
            print(f"Hint: {data['hint']}")
            user_answer = input("Try again: ")
            if user_answer.lower() == data["answer"].lower():
                print("Correct!")
                user_score += 1
            else:
                print("Wrong again. The correct answer was:", data["answer"])

    score.save_score(username, user_score)
    print(f"\nYour score: {user_score}")
    time.sleep(5.0)