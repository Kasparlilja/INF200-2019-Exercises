# -*- coding: utf-8 -*-

__author__ = ''
__email__ = '@nmbu.no'

import random

class Walker:

    def __init__(self, initialpos, homepos):
        self.initalpos = initialpos
        self.homepos = homepos
        self.steps = 0


    def move(self):
        self.initalpos += random.choice([-1, 1])
        self.steps += 1


    def is_at_home(self):
        if self.homepos == self.initalpos:
            return True
        else:
            return False


    def get_position(self):
        return self.initalpos


    def get_steps(self):
        return self.steps


def walking(distance):

    startpos = 0
    the_walker = Walker(startpos, distance)

    while the_walker.is_at_home() == False:
        the_walker.move()

    return the_walker.get_steps()


if __name__ == "__main__":

    distances = [1, 2, 5, 10, 20, 50, 100]
    for distance in distances:
        path = []
        for i in range(5):
            path.append(walking(distance))
        print('Distance: {0} -> Path lengths: {1}'.format(distance, path))


