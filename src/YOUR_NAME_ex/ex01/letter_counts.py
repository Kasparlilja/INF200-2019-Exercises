import collections

def letter_freq(txt):
    streng = txt.lower()
    streng = ''.join(sorted(streng))
    tekst = collections.OrderedDict()
    for symbol in streng:
        if symbol in tekst:
            tekst[symbol] += 1
        else:
            tekst[symbol] = 1
    return tekst


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))