import math
import copy
import numpy as np
from collections import defaultdict
from itertools import combinations


def read_file(filename='input.txt'):
    notes = list()
    page = list()

    with open(filename, 'r') as f:
        lines = f.readlines()

        for row, line in enumerate(lines):
            line = line.strip()

            if line == '':
                notes.append(page)
                page = list()
                continue
            tmp = list()
            for col, c in enumerate(line):
                tmp.append(c)
            page.append(tmp)
        notes.append(page)

    return notes


def find_mirror_1(matrix):
    result = -1

    for pos in range(1, (matrix.shape[1])):
        find = True
        size = matrix[:, :pos].shape[1]
        for c in range(size):
            if (2 * size - c - 1) < matrix.shape[1] and not np.array_equal(matrix[:, c], matrix[:, (2 * size - c - 1)]):
                # print(f"Mat1: {c}-{matrix[:, c]}\nMat2: {2 * size - c - 1}-{matrix[:, 2 * size - c - 1]}")
                find = False
                break
        if find:
            result = pos
            break

    return result


def find_mirror_2(matrix):
    result = -1

    for pos in range(1, (matrix.shape[1])):
        smudge = 1
        size = matrix[:, :pos].shape[1]
        for c in range(size):
            if (2 * size - c - 1) < matrix.shape[1]:
                mask1 = matrix[:, c] == '#'
                mask2 = matrix[:, (2 * size - c - 1)] == '#'
                res = np.sum(np.logical_xor(mask2, mask1))
                smudge -= res
                if res > 1:
                    break


        if smudge == 0:
            result = pos
            break

    return result


def day13_1(notes):
    result = 0
    for n in notes:
        n = np.array(n)
        tmp = find_mirror_1(n)
        if tmp == -1:
            tmp = find_mirror_1(n.T) * 100
        result += tmp

    print(f'DAY13_1: {result}')


def day13_2(notes):
    result = 0
    for n in notes:
        n = np.array(n)
        tmp = find_mirror_2(n)
        if tmp == -1:
            tmp = find_mirror_2(n.T) * 100
        result += tmp

    print(f'DAY13_2: {result}')


if __name__ == "__main__":
    nodes = read_file()
    day13_1(nodes)
    day13_2(nodes)
