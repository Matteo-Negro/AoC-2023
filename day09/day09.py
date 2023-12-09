import math
import numpy as np
from collections import defaultdict


def read_file(filename='input.txt'):
    clean = list()
    with open(filename, 'r') as f:
        lines = f.readlines()
        for index, line in enumerate(lines):
            line = [int(i) for i in line.strip().split(' ')]
            clean.append(line)
    return clean


def day09_1(input):
    result = 0
    for i in input:
        tmp = i
        derivation = [i]
        while True:
            tmp = [tmp[j+1] - tmp[j] for j in range(0, len(tmp) - 1)]
            derivation.append(tmp)
            if tmp.count(0) == len(tmp):
                break

        for j in range(len(derivation) - 1, 0, -1):
            derivation[j - 1].append(derivation[j - 1][-1] + derivation[j][-1])

        result += derivation[0][-1]

    print(f'DAY09_1: {result}')


def day09_2(input):
    result = 0
    for i in input:
        tmp = i
        derivation = [i]
        while True:
            tmp = [tmp[j+1] - tmp[j] for j in range(0, len(tmp) - 1)]
            derivation.append(tmp)
            if tmp.count(0) == len(tmp):
                break

        for j in range(len(derivation) - 1, 0, -1):
            derivation[j - 1].insert(0, derivation[j - 1][0] - derivation[j][0])
        result += derivation[0][0]

    print(f'DAY09_2: {result}')


if __name__ == "__main__":
    clean_input = read_file()
    day09_1(clean_input)
    day09_2(clean_input)
