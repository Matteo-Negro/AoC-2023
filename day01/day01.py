import numpy as np


def read_file(filename='input.txt'):
    clean = list()
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            clean.append(line)

    return clean


def day01_1(input):
    result = 0
    nums = list()
    for i in input:
        first = True
        tmp = -1

        for c in i:
            if c.isdigit() and first:
                val = int(c)
                first = False
            elif c.isdigit():
                tmp = int(c)
        if tmp != -1:
            res = val * 10
            res += tmp
        else:
            res = val * 10
            res += val
        nums.append(res)

    for i in nums:
        result += i

    print(f'DAY01_1: {result}')


def day01_2(input):
    result = 0
    nums = list()
    for i in input:
        i = i.replace('one', 'one1one')
        i = i.replace('two', 'two2two')
        i = i.replace('three', 'three3three')
        i = i.replace('four', 'four4four')
        i = i.replace('five', 'five5five')
        i = i.replace('six', 'six6six')
        i = i.replace('seven', 'seven7seven')
        i = i.replace('eight', 'eight8eight')
        i = i.replace('nine', 'nine9nine')

        first = True
        tmp = -1
        for c in i:
            if c.isdigit() and first:
                val = int(c)
                first = False
            elif c.isdigit():
                tmp = int(c)
        if tmp != -1:
            res = val * 10
            res += tmp
        else:
            res = val * 10
            res += val
        nums.append(res)

    for n in nums:
        result += n

    print(f'DAY01_2: {result}')


if __name__ == "__main__":
    clean_input = read_file()
    day01_1(clean_input)
    day01_2(clean_input)