#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    # Write your code here
    lrsum = 0
    rlsum = 0
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                lrsum += arr[i][j]
            if i == n - j - 1:
                rlsum += arr[i][j]

    ad = abs(lrsum-rlsum)
    return ad


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
