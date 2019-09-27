def char_counts(textfilename):
    file_name = open(textfilename)
    str_text = file_name.read()
    file_name.close()
    count = {}

    for key_value in range(256):
        count{key_value} = 0

    for index, chr in enumerate(str_text):
        if ord(chr) in count.keys():
            count[ord(chr)] += 1]
        else:
            count[ord(chr)] = 1]
    return count


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