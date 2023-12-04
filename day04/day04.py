import numpy as np
from collections import defaultdict


def read_file(filename='input.txt'):
    clean = dict()
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(':')

            tmp1 = list()
            for i in line[1].split(' | ')[0].split(' '):
                if i != '':
                    tmp1.append(int(i))

            tmp2 = list()
            for i in line[1].split(' | ')[1].split(' '):
                if i != '':
                    tmp2.append(int(i))

            clean[line[0].split(' ')[-1]] = [tmp1, tmp2, 1]

    return clean


def day04_1(input):
    result = 0
    for i in input:
        match = 0
        for c in input[i][0]:
            if c in input[i][1]:
                match += 1
        if match != 0:
            result += (2 ** (match - 1))

    print(f'DAY04_1: {int(result)}')


def day04_2(input):
    result = 0
    for index, i in enumerate(input):
        match = 0
        for c in input[i][0]:
            if c in input[i][1]:
                match += 1
        for c in range(index + 2, index + 2 + match):
            input[f'{c}'][-1] += input[i][-1]

    for i in input:
        result += input[i][-1]

    print(f'DAY04_2: {result}')


if __name__ == "__main__":
    clean_input = read_file()
    day04_1(clean_input)
    day04_2(clean_input)