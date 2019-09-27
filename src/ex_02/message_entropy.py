# -*- coding: utf-8 -*-

from collections import Counter
from math import log2


def letter_freqs(txt):
    # best soulution
    return Counter(txt.lower())


def entropy(message):
    ent = 0
    n = len(message)
    letter_count = letter_freqs(message)
    for values in letter_count.values():
        if values > 0:
            ent -= (values / n*log2(values/n))
    return ent


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
