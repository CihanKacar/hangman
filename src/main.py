#!/usr/bin/env python3


import os
import random
import platform
from types import FrameType
from typing import Tuple


def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def read_file(path: str) -> list[str]:
    with open(path, mode='r') as file_handler:
        return[line.strip('\n') for line in file_handler.readlines()]

def load_game():
    ...

def main_menu():
    ...

def main(words: list) -> Tuple[int, str]:
    print("Lets play Hangman")
    word = random.choice(words)
    guess_me =  list(word)
    guessed = ['?' for _ in range(len(guess_me))]
    MAXLP = 10
    lp = MAXLP



    while ('?' in guessed and lp>0):
        print(f"{' '.join(guessed).capitalize()} {lp}")
        print('\n'.join(read_file(f'src/{MAXLP - lp}.txt')))
        guess = input(">>> ")[0].upper()
        correct = False

        for i in range(len(guess_me)):
            if guess == guess_me[i].upper():
                guessed[i] = guess
                correct = True
        if correct == False:
            lp = lp - 1


        clear()

    return(lp, word)

def credits(lp: int, word: str) -> None:
    print("You {}! The word was {}".format('won' if lp > 0 else 'lost', word))

if __name__ == '__main__':
    load_game()
    main_menu()
    words = read_file("src/words.txt")
    game_data = main(words)
    credits(lp=game_data[0], word=game_data[1])
