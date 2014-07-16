# -*- coding: utf-8 -*-
"""
    Generates password using  random words from ~10 000 most common english words taken from wiki
    dictionary.

     It should be safe --- at least xkcd says it is safe. And xkcd is right always ;)

"""
from __future__ import print_function

from random import SystemRandom

import os

DIRNAME = os.path.dirname(__file__)

RAND = SystemRandom()


def load():
    result = set()
    with open(os.path.join(DIRNAME, "data.txt")) as f:
        for row in f:
            if row:
                result.add(row.strip().lower())
    return list(result)

DATA = load()


def random_pass(word_count=5):
    words = []
    for ii in range(word_count):
        words.append(RAND.choice(DATA))
    return "-".join(words)
