#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple_dist = []
    orange_dist = []
    apple_counts = 0
    orange_counts = 0
    for elem in apples:
        adist = a + elem
        apple_dist.append(adist)
    for elem in oranges:
        odist = b + elem
        orange_dist.append(odist)
    for elem in apple_dist:
        if elem in range(s, t+1):
            apple_counts += 1
    for elem in orange_dist:
        if elem in range(s, t+1):
            orange_counts += 1
    return print(apple_counts, orange_counts, sep='\n')


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
