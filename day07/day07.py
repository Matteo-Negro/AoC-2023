import numpy as np
from collections import defaultdict
import operator


def read_file_01(filename='input.txt'):
    clean = list()
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            count = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
            tmp = list()
            hand, bid = line.strip().split(' ')
            for c in hand:
                if c == 'T':
                    c = 10
                elif c == 'J':
                    c = 11
                elif c == 'Q':
                    c = 12
                elif c == 'K':
                    c = 13
                elif c == 'A':
                    c = 14
                else:
                    c = int(c)

                count[c] += 1
                tmp.append(c)
            if 5 in list(count.values()):
                clean.append([tmp, 6, int(bid)])
            elif 4 in list(count.values()):
                clean.append([tmp, 5, int(bid)])
            elif 3 in list(count.values()) and 2 in list(count.values()):
                clean.append([tmp, 4, int(bid)])
            elif 3 in list(count.values()):
                clean.append([tmp, 3, int(bid)])
            elif list(count.values()).count(2) == 2:
                clean.append([tmp, 2, int(bid)])
            elif 2 in list(count.values()):
                clean.append([tmp, 1, int(bid)])
            else:
                clean.append([tmp, 0, int(bid)])

    return clean


def read_file_02(filename='input.txt'):
    clean = list()
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            count = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, -1: 0, 12: 0, 13: 0, 14: 0}
            tmp = list()
            hand, bid = line.strip().split(' ')
            for c in hand:
                if c == 'T':
                    c = 10
                elif c == 'J':
                    # c = 11
                    c = -1
                elif c == 'Q':
                    c = 12
                elif c == 'K':
                    c = 13
                elif c == 'A':
                    c = 14
                else:
                    c = int(c)

                count[c] += 1
                tmp.append(c)
            if 5 in list(count.values()) or (4 in list(count.values()) and tmp.count(-1) == 1) or (3 in list(count.values()) and tmp.count(-1) == 2) or (2 in list(count.values()) and tmp.count(-1) == 3) or (tmp.count(-1) == 4):
                clean.append([tmp, 6, int(bid)])
            elif 4 in list(count.values()) or (3 in list(count.values()) and tmp.count(-1) == 1) or (list(count.values()).count(2) == 2 and tmp.count(-1) == 2) or (tmp.count(-1) == 3):
                clean.append([tmp, 5, int(bid)])
            elif 3 in list(count.values()) and 2 in list(count.values()) or (list(count.values()).count(2) == 2 and tmp.count(-1) == 1):
                clean.append([tmp, 4, int(bid)])
            elif 3 in list(count.values()) or (2 in list(count.values()) and tmp.count(-1) == 1) or (tmp.count(-1) == 2):
                clean.append([tmp, 3, int(bid)])
            elif list(count.values()).count(2) == 2:
                clean.append([tmp, 2, int(bid)])
            elif 2 in list(count.values()) or (tmp.count(-1) == 1):
                clean.append([tmp, 1, int(bid)])
            else:
                clean.append([tmp, 0, int(bid)])

    return clean


def day07(input):
    result = 0
    test = sorted(input, key=lambda hand: (hand[1], hand[0]), reverse=True)
    max_rank = len(test)
    for index, t in enumerate(test):
        result += ((max_rank - index) * t[2])

    print(f'DAY07: {result}')


if __name__ == "__main__":
    day07(read_file_01())
    day07(read_file_02())
