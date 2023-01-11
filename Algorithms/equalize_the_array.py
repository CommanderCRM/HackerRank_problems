import math
import os
import random
import re
import sys


def equalizeArray(arr):
    count = {}
    for elem in arr:
        if elem in count:
            count[elem] += 1
        else:
            count[elem] = 1
    max_occurrences = max(count.values())
    return len(arr) - max_occurrences

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
