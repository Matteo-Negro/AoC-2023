import numpy as np
from collections import defaultdict


def day06(input):
    result = 1
    for i in range(0, len(input[0])):
        count = 0
        for j in range(input[0][i] - 1, -1, -1):
            time = input[0][i] - j
            if time * j > input[1][i]:
                count += 1

        result *= count

    print(f'DAY06: {result}')


if __name__ == "__main__":
    day06([[46, 80, 78, 66], [214, 1177, 1402, 1024]])
    day06([[46807866], [214117714021024]])
