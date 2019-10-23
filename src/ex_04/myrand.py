# -*- coding: utf-8 -*-

__author__ = ''
__email__ = '@nmbu.no'

import random

class LCGRand:
    def __init__(self):
        self.a = 16807
        self.b = 2**31-1
        r[n + 1] = a * r[n] % m

    def rand(self):
