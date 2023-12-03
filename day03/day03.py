import numpy as np
from collections import defaultdict


def read_file(filename='input.txt'):
    clean = list()
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            clean.append(line)

    return clean


def day03_1(input):
    result = 0
    for r in range(0, len(input)):
        find = False
        val = 0
        for c in range(0, len(input[r])):
            if input[r][c].isdigit():
                val *= 10
                val += int(input[r][c])

                if r - 1 > -1 and not input[r - 1][c].isdigit() and input[r - 1][c] != '.':
                    find = True
                elif r - 1 > -1 and c + 1 < len(input[r - 1]) and not input[r - 1][c + 1].isdigit() and input[r - 1][c + 1] != '.':
                    find = True
                elif c + 1 < len(input[r]) and not input[r][c + 1].isdigit() and input[r][c + 1] != '.':
                    find = True
                elif r + 1 < len(input) and c + 1 < len(input[r + 1]) and not input[r + 1][c + 1].isdigit() and input[r + 1][c + 1] != '.':
                    find = True
                elif r + 1 < len(input) and not input[r + 1][c].isdigit() and input[r + 1][c] != '.':
                    find = True
                elif r + 1 < len(input) and c - 1 > -1 and not input[r + 1][c - 1].isdigit() and input[r + 1][c - 1] != '.':
                    find = True
                elif c - 1 > -1 and not input[r][c - 1].isdigit() and input[r][c - 1] != '.':
                    find = True
                elif r - 1 > -1 and c - 1 > -1 and not input[r - 1][c - 1].isdigit() and input[r - 1][c - 1] != '.':
                    find = True
            else:
                if find:
                    result += val

                val = 0
                find = False

        if find:
            result += val

    print(f'DAY03_1: {result}')


def day03_2(input):
    result = 0
    pos = defaultdict(list)
    for r in range(0, len(input)):
        find = False
        val = 0
        tmp = set()
        for c in range(0, len(input[r])):
            if input[r][c].isdigit():
                val *= 10
                val += int(input[r][c])

                if r - 1 > -1 and not input[r - 1][c].isdigit() and input[r - 1][c] != '.':
                    find = True
                    if input[r - 1][c] == '*':
                        tmp.add(f'{r - 1}-{c}')
                elif r - 1 > -1 and c + 1 < len(input[r - 1]) and not input[r - 1][c + 1].isdigit() and input[r - 1][
                    c + 1] != '.':
                    find = True
                    if input[r - 1][c + 1] == '*':
                        tmp.add(f'{r - 1}-{c + 1}')
                elif c + 1 < len(input[r]) and not input[r][c + 1].isdigit() and input[r][c + 1] != '.':
                    find = True
                    if input[r][c + 1] == '*':
                        tmp.add(f'{r}-{c + 1}')
                elif r + 1 < len(input) and c + 1 < len(input[r + 1]) and not input[r + 1][c + 1].isdigit() and \
                        input[r + 1][c + 1] != '.':
                    find = True
                    if input[r + 1][c + 1] == '*':
                        tmp.add(f'{r + 1}-{c + 1}')
                elif r + 1 < len(input) and not input[r + 1][c].isdigit() and input[r + 1][c] != '.':
                    find = True
                    if input[r + 1][c] == '*':
                        tmp.add(f'{r + 1}-{c}')
                elif r + 1 < len(input) and c - 1 > -1 and not input[r + 1][c - 1].isdigit() and input[r + 1][
                    c - 1] != '.':
                    find = True
                    if input[r + 1][c - 1] == '*':
                        tmp.add(f'{r + 1}-{c - 1}')
                elif c - 1 > -1 and not input[r][c - 1].isdigit() and input[r][c - 1] != '.':
                    find = True
                    if input[r][c - 1] == '*':
                        tmp.add(f'{r}-{c - 1}')
                elif r - 1 > -1 and c - 1 > -1 and not input[r - 1][c - 1].isdigit() and input[r - 1][c - 1] != '.':
                    find = True
                    if input[r - 1][c - 1] == '*':
                        tmp.add(f'{r - 1}-{c - 1}')
            else:
                if find:
                    for t in tmp:
                        pos[t].append(val)

                val = 0
                find = False
                tmp = set()

        if find:
            for t in tmp:
                pos[t].append(val)

    for p in pos:
        if len(pos[p]) == 2:
            result += (pos[p][0] * pos[p][1])

    print(f'DAY03_2: {result}')


if __name__ == "__main__":
    clean_input = read_file()
    day03_1(clean_input)
    day03_2(clean_input)