"""
Rock Paper Scissors
"""

import re
import random

def play_game():
    while (2<3):
        print("\n")
        print("welcome, ready to rock, roll, and cut..")
        print("R for rock, S for scissor or P for paper")
        user_input = input("make your choice: ")
        if not re.match("[RrSsPp]", user_input):
            print("Enter a valid option, (R, S or P)")
            continue
        print("your input is " + user_input)
        choices = ["R", "P", "S"]
        random_choice = random.choice(choices)
        if user_input.upper() == random_choice:
            print("Its a tie")
        elif user_input.upper() == "S" and random_choice == "R":
            print ("rock beats scissors, I win! ")
            continue
        elif user_input.upper() == "P" and random_choice == "S":
            print ("Scissors beats paper, I win! ")
            continue
        elif user_input.upper() == "R" and random_choice == "P":
            print ("paper beats rock, I win! ")
            continue
        else:
            print("you win")
play_game()
