import math
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
                if line[0][-1] == 'A':
                    starting.append(line[0])
    return command, clean, starting


def day08_1(command, input):
    result = 0
    counter = 0
    pos = 'AAA'
    while True:
        pick = 0 if command[counter] == 'L' else 1
        pos = input[pos][pick]
        result += 1
        counter += 1
        counter = counter % len(command)
        if pos == 'ZZZ':
            break

    print(f'DAY08_1: {result}')

# def day08_2(command, input, starting):
#     result = 0
#     counter = 0
#
#     size_start = len(starting)
#     size_com = len(command)
#     prev = 0
#     while True:
#         print(result)
#         pick = 0 if command[counter] == 'L' else 1
#
#         stop = 0
#         for index, pos in enumerate(starting):
#             starting[index] = input[pos][pick]
#             if starting[index][-1] == 'Z':
#                 stop += 1
#
#         if stop == size_start:
#             result += 1
#             break
#         elif prev < stop:
#             prev = stop
#             result += result
#             counter += counter
#             counter %= size_com
#         else:
#             result += 1
#             counter += 1
#             counter %= size_com
#
#
#     print(f'DAY08_2: {result}')


def compute(command, input, pos):
    result = 0
    counter = 0
    pos = pos
    while True:
        pick = 0 if command[counter] == 'L' else 1
        pos = input[pos][pick]
        result += 1
        counter += 1
        counter = counter % len(command)
        if pos[-1] == 'Z':
            break

    return result


def day08_2(command, input, starting):
    result = 1
    for pos in starting:
        result = math.lcm(result, compute(command, input, pos))

    print(f'DAY08_2: {result}')


if __name__ == "__main__":
    command, clean_input, starting = read_file()
    day08_1(command, clean_input)
    day08_2(command, clean_input, starting)