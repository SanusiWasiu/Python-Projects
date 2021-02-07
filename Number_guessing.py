"""
Number Guessing Game
"""
import random

attempts_list = []
def score():
    if len(attempts_list) <= 0:
        print("There's no high score yet, its your for the taking")
    else:
        print(f"The current high score is {min(attempts_list)} attempts")

def start_game():
    wanna_play = input("do you wanna play (enter yes or no): ")
    if wanna_play.lower() != "yes" and wanna_play.lower() != "no":
        print("invalid answer, enter yes or no")
        wanna_play
    else:
        number = random.randint(1, 10)
        score()
    attempts = 0
    while wanna_play.lower() == "yes":
        try:
            guess = int(input("guess a number from one to ten: "))
            if guess <=0 or guess >10:
                raise ValueError("only numbers from one to ten are valid")
            if guess == number:
                print("correct, you are a champion")
                attempts += 1
                attempts_list.append(attempts)
                print(f"you got it after {attempts} attempts")
                play_more = input("do you want to play again, (enter yes or no): ")
                attempts = 0
                score()
                number = random.randint(1, 10)
                
                if play_more.lower() == "no":
                    print("Alright, Adios")
                    break
                if play_more.lower() != "yes" and play_more.lower() != "no":
                    print("what do you mean, give a clear answer")
                    play_more
                    
            elif guess < number:
                attempts += 1
                print("try again, its higher")
            elif guess > number:
                attempts += 1
                print("try again, its lower")
        except ValueError as e:
            print(f"invalid input, {e}")
    else:
        print("Adios Amigo")
start_game()


        

    