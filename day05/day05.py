import numpy as np
from collections import defaultdict


def read_file(filename='input.txt'):
    clean = list()
    seeds = list()
    tmp = list()
    with open(filename, 'r') as f:
        lines = f.readlines()
        for index, line in enumerate(lines):
            line = line.strip()
            if index == 0:
                line = line.split(' ')
                for s in line[1:]:
                    seeds.append(int(s))
            elif ':' in line and len(tmp) != 0:
                clean.append(tmp)
                tmp = list()
            elif ':' not in line and line != '':
                t = [int(i) for i in line.split(' ')]
                tmp.append(t)
        clean.append(tmp)

    return seeds, clean


def day05_1(input, seeds):
    min = np.inf
    for s in seeds:
        pos = s
        for m in input:
            for l in m:
                dest, start, size = l
                # print(list(range(start, start + size)))
                if pos in range(start, start + size):
                    pos = (dest + pos - start)
                    break

        if pos < min:
            min = pos

    print(f'DAY05_1: {min}')


def day05_2(input, seeds):
    min = np.inf
    ranges = list()
    for c in range(0, len(seeds), 2):
        ranges.append([seeds[c], seeds[c + 1], 0])

    while len(ranges) != 0:
        # print('#################')
        # print(f'{ranges}')
        ran = ranges.pop(0)
#         print(f'Consider: {ran}')
        if ran[2] == len(input):
            if ran[0] < min:
                min = ran[0]
            continue
        m = input[ran[2]]
        check = True
        for l in m:
            dest, start, size = l

            if (ran[0] + ran[1] - 1 < start) or (ran[0] > start + size - 1):
#                 print(f'{ran[0] + ran[1] - 1} < {start} or {ran[0]} > {start + size - 1}')
#                 print(f'skip # rule: {l}')
                continue
            elif ran[0] >= start:
                # Case A
#                 print(f'CASE A # rule: {l}')
                if ran[0] + ran[1] > start + size:
                    # Update range
#                     print(f'Branch1: ')
                    ranges.append([ran[0] + (dest - start), start + size - ran[0], ran[2] + 1])
                    ranges.append([ran[0] + start + size - ran[0], ran[0] + ran[1] - start - size, ran[2]])
                else:
                    # Update range
#                     print(f'Branch2: ')
                    ranges.append([ran[0] + (dest - start), ran[1], ran[2] + 1])
                check = False
                break
            elif (ran[0] < start) and (ran[0] + ran[1] - 1 > start + size - 1):
                # Case B
#                 print(f'CASE B # rule: {l}')
                ranges.append([ran[0], start - ran[0], ran[2]])
                ranges.append([start, size, ran[2] + 1])
                ranges.append([start + size, ran[0] + ran[1] - start - size, ran[2]])
                check = False
                break
            else:
                # Case C
#                 print(f'CASE C # rule: {l}')
                ranges.append([ran[0], start - ran[0], ran[2]])
                ranges.append([dest, (ran[0] + ran[1]) - start, ran[2] + 1])
                check = False
                break
        if check:
            ranges.append([ran[0], ran[1], ran[2] + 1])

    print(f'DAY05_2: {min}')


if __name__ == "__main__":
    seed, clean_input = read_file()
    day05_1(clean_input, seed)
    day05_2(clean_input, seed)