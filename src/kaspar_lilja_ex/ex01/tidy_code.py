# -*- coding: utf-8 -*-
# This program makes you guess the sum of two dices.
# You have 3 tries to guess the right answer.

from random import randint as a


def players_guess():
    c = 0
    while c < 1:
        c = int(input('Your guess: '))
    return c


def dices_sum():
    return a(1, 6) + a(1, 6)


def if_correct_answer(f, g):
    return f == g


if __name__ == '__main__':

    checking_if_guess_is_correct = False
    number_of_tries = 3
    right_answer = dices_sum()

    while not checking_if_guess_is_correct and number_of_tries > 0:

        guess_of_player = players_guess()
        checking_if_guess_is_correct = if_correct_answer(right_answer, guess_of_player)

        if not checking_if_guess_is_correct:
            print('Wrong, try again!')
            number_of_tries -= 1

    if number_of_tries > 0:
        print('You won {} points.'.format(number_of_tries))
    else:
        print('You lost. Correct answer: {}.'.format(right_answer))
