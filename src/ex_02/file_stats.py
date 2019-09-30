# -*- coding: utf-8 -*-

__author__ = 'kaspar lilja'
__email__ = 'kalilja@nmbu.no'


def char_counts(textfilename):
    file_name = open(textfilename)
    str_text = file_name.read()
    file_name.close()
    count_ = {}

    for key_value in range(256):
        count_[key_value] = 0

    for index, char in enumerate(str_text):
        if ord(char) in count_.keys():
            count_[ord(char)] += 1
        else:
            count_[ord(char)] = 1
    return count_


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
