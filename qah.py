# *********************************************************
# Program: qah.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL??
# Year: 2023/24 Trimester 1
# Names: MEMBER_NAME_1 | MEMBER_NAME_2 | MEMBER_NAME_3
# IDs: MEMBER_ID_1 | MEMBER_ID_2 | MEMBER_ID_3
# Emails: MEMBER_EMAIL_1 | MEMBER_EMAIL_2 | MEMBER_EMAIL_3
# Phones: MEMBER_PHONE_1 | MEMBER_PHONE_2 | MEMBER_PHONE_3
# *********************************************************

import random
import user
import score
import screen

# dictionary of key-value pair

# questions = {
#     """ASCII Art Representing a Subject""": {
#         "answer": "Correct Answer",
#         "hint": "Helpful Hint for the Question"
#     },
#     # Other Question...
# }

# source of ascii arts: https://www.asciiart.eu/

questions = {
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

def start_game():
    username = user.register_user()
    user_score = 0

    # Select 4 random questions
    # reference for random sample: https://www.geeksforgeeks.org/python-random-sample-function/
    selected_questions = random.sample(list(questions.items()), 4)

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

    print(f"\nYour score: {user_score}")
    score.save_score(username, user_score)