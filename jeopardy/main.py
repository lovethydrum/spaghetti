import random

answer = random.randint(0,100)
lives = 10
continue_game = True


def live_change():
    return lives - 1


while continue_game:
    guess = input("Guess a number between 1 and 100:  ")
    if guess == isinstance((int)):
        continue
    else:
        print("This is not a number!  Try again")