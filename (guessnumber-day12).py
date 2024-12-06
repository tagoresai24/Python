
#    simple game to guess the number 

import random

Easy_chances = 10
Hard_chances = 5



def check_answer(aswer, guess):
    if answer>guess:
        print("Too low")
    elif answer<guess:
        print("Too High")   
    else:
        print("Right answer")     


def set_dificulty():
    level = input("Select dificulty , Type 'easy' or 'hard'").lower()
    if level == "easy":
        return Easy_chances
    else:
        return Hard_chances
            
    
    
    




print("Welcome to the NUMBER GUESSING game")
print("Guess a number form 0 to 100")
answer = random.randint(0,100)
guess = int(input())  
turns = set_dificulty()

print(f"You have {turns} to Guess the answer")