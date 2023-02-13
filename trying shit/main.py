from hangmanlibrary import logo
from hangmanlibrary import HANGMANPICS
from hangmanlibrary import words
from random import randint


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


lives = 7


def gallows():
    print(HANGMANPICS[7 - lives])


print(logo)
answer = (words[randint(0, 63)])
hidden_answer = answer
for letters in hidden_answer:
    hidden_answer = hidden_answer.replace(letters, "_ ")
print(answer)
print(hidden_answer)


def guess():
    userinput = input("Please choose a letter: ")
    userinput = userinput.lower()
    if userinput == answer:
        print("Holy Cow!  You nailed it!")
    elif len(userinput) > 1:
        print("Please only input 1 letter at a time.")
    elif is_number(userinput):
        print("Alphabet only please.")
    else:
        for element in answer:
            if guess == element:
                print("wow")
            else:
                print("whiff")