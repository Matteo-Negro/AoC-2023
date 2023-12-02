import numpy as np
from collections import defaultdict

def read_file(filename='input.txt'):
    clean = dict()
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(': ')
            clean[line[0].split(' ')[-1]] = list()
            for el in line[1].split('; '):
                dic = defaultdict(int)
                for n in el.split(', '):
                    tmp = n.split(' ')
                    dic[tmp[1]] += int(tmp[0])
                clean[line[0].split(' ')[-1]].append(dic)
    return clean


def day02_1(input):
    result = 0
    check = {'red': 12, 'green': 13, 'blue': 14}
    for i in input:
        control = True
        for set in input[i]:
            if set['red'] > check['red'] or set['green'] > check['green'] or set['blue'] > check['blue']:
                control = False
                break
        if control:
            result += int(i)
    print(f'DAY02_1: {result}')


def day02_2(input):
    result = 0
    for i in input:
        maxRed = 0
        maxBlue = 0
        maxGreen = 0

        for set in input[i]:
            if set['red'] > maxRed:
                maxRed = set['red']
            if set['blue'] > maxBlue:
                maxBlue = set['blue']
            if set['green'] > maxGreen:
                maxGreen = set['green']

        result += (maxRed * maxBlue * maxGreen)

    print(f'DAY02_2: {result}')


if __name__ == "__main__":
    clean_input = read_file()
    day02_1(clean_input)
    day02_2(clean_input)