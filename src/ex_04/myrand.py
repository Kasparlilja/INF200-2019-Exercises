# -*- coding: utf-8 -*-

__author__ = 'Kaspar Lilja'
__email__ = 'kalilja@nmbu.no'


class LCGRand:

    def __init__(self, seed):
        self.seed = seed

    def rand(self):
        a = 16807
        m = 2 ** 31 - 1
        self.seed = (a * self.seed) % m
        return self.seed


class ListRand:

    def __init__(self, randomlist):
        self.randomlist = randomlist
        self.position = 0

    def rand(self):
        if self.position >= len(self.randomlist):
            raise RuntimeError
        else:
            temp_pos = self.position
            self.position += 1
            return self.randomlist[temp_pos]


if __name__ == "__main__":
    rng1 = LCGRand(1)
    rng2 = LCGRand(2)
    print(rng1.rand(), rng2.rand())

    rng3 = ListRand([1, 4])
    print(rng3.rand())
    print(rng3.rand())
    print(rng3.rand())  # testing if a RuntimeError raises
