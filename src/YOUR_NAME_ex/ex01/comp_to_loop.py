def squares_by_comp(n):
    return [k ** 2 for k in range(n) if k % 3 == 1]


def comp_to_loop(n):
    square = []
    for number in range(n):
        if number % 3 == 1:
            square.append(number ** 2)
    return square


if __name__ == '__main__':
    if squares_by_comp(5) != comp_to_loop(5):
        print('ERROR!')
