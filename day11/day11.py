import math
import numpy as np
from collections import defaultdict
from itertools import combinations


def read_file(filename='input.txt'):
    galaxies = dict()
    emptyRow = set()

    with open(filename, 'r') as f:
        lines = f.readlines()
        emptyCol = set(range(len(lines)))

        counter = 0
        for row, line in enumerate(lines):
            line = line.strip()

            if line.count('#') == 0:
                emptyRow.add(row)
                continue

            for col, c in enumerate(line):
                if c == '#':
                    galaxies[counter] = [row, col]
                    if col in emptyCol:
                        emptyCol.remove(col)
                    counter += 1

    return galaxies, emptyRow, emptyCol


def day11_1(galaxies, emptyRow, emptyCol):
    result = 0
    for couple in combinations(galaxies.keys(), 2):
        gal1, gal2 = couple
        distance = abs(galaxies[gal1][0] - galaxies[gal2][0]) + abs(galaxies[gal1][1] - galaxies[gal2][1])

        for r in emptyRow:
            if r in range(min(galaxies[gal1][0], galaxies[gal2][0]), max(galaxies[gal1][0], galaxies[gal2][0])):
                distance += 1

        for c in emptyCol:
            if c in range(min(galaxies[gal1][1], galaxies[gal2][1]), max(galaxies[gal1][1], galaxies[gal2][1])):
                distance += 1

        result += distance

    print(f'DAY11_1: {result}')


def day11_2(galaxies, emptyRow, emptyCol):
    result = 0
    for couple in combinations(galaxies.keys(), 2):
        gal1, gal2 = couple
        distance = abs(galaxies[gal1][0] - galaxies[gal2][0]) + abs(galaxies[gal1][1] - galaxies[gal2][1])

        for r in emptyRow:
            if r in range(min(galaxies[gal1][0], galaxies[gal2][0]), max(galaxies[gal1][0], galaxies[gal2][0])):
                distance += (1000000 - 1)

        for c in emptyCol:
            if c in range(min(galaxies[gal1][1], galaxies[gal2][1]), max(galaxies[gal1][1], galaxies[gal2][1])):
                distance += (1000000 - 1)

        result += distance

    print(f'DAY11_2: {result}')


if __name__ == "__main__":
    galaxies, emptyRow, emptyCol = read_file()
    day11_1(galaxies, emptyRow, emptyCol)
    day11_2(galaxies, emptyRow, emptyCol)
