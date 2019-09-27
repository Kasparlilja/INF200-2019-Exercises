# -*- coding: utf-8 -*-
__author__ = 'kaspar lilja'
__email__ = 'kalilja@nmbu.no'


def bubble_sort(data):
    datalist = list(data)
    for i in range(0, len(datalist) - 1):
        for j in range(0, len(datalist) - 1 - i):
            if datalist[j] > datalist[j + 1]:
                datalist[j], datalist[j + 1] = datalist[j + 1], datalist[j]
    return datalist


if __name__ == "__main__":
    def main():
        for data in ((),
                     (1,),
                     (1, 3, 8, 12),
                     (12, 8, 3, 1),
                     (8, 3, 12, 1)):
            print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
    main()
