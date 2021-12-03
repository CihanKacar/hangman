#!/usr/bin/env python3


import os
import random
import platform

def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def main():
    words  = ["Cihan", "Ibo", "Murat", "Ali"]
    word = random.choice(words)
    guess_me =  list(word)
    guessed = ['?' for _ in range(len(guess_me))]
    MAXLP = 10
    lp = MAXLP



    while ('?' in guessed and lp>0):
        print(f"{' '.join(guessed).capitalize()} {lp}")
        guess = input(">>> ")[0].upper()
        correct = False

        for i in range(len(guess_me)):
            if guess == guess_me[i].upper():
                guessed[i] = guess
                correct = True
        if correct == False:
            lp = lp - 1


        clear()

    print("You {}! The word was {}".format('won' if lp > 0 else 'lost', word))




if __name__ == '__main__':
    main()
