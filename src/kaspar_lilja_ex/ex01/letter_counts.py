# -*- coding: utf-8 -*-

import collections


def letter_freq(txt):
    string = txt.lower()
    alphabetic_string = ''.join(sorted(string))
    new_dict = collections.OrderedDict()
    for symbol in alphabetic_string:
        if symbol in new_dict:
            new_dict[symbol] += 1
        else:
            new_dict[symbol] = 1
    return new_dict


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
