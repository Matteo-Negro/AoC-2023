import numpy as np
from collections import defaultdict


def read_file(filename='input.txt'):
    clean = dict()
    starting = list()
    with open(filename, 'r') as f:
        lines = f.readlines()
        for index, line in enumerate(lines):
            line = line.strip()
            if index == 0:
                command = [i for i in line]
            elif line != '':
                line = line.replace(' = (', ' ').replace(',', '').replace(')', '').split(' ')
                clean[line[0]] = [line[1], line[2]]
                if ()
    return command, clean, starting


def day08_1(command, input):
    result = 0
    counter = 0
    print(command)
    print(input)
    pos = 'AAA'
    while True:
        pick = 0 if command[counter] == 'L' else 1
        pos = input[pos][pick]
        result += 1
        counter += 1
        counter = counter % len(command)
        if pos == 'ZZZ':
            break

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
    command, clean_input = read_file()
    day08_1(command, clean_input)
    # day04_2(clean_input)