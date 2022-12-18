import math
import os
import random
import re
import sys


def compareTriplets(a, b):
    points = [0, 0]
    for i in range(3):
        if a[i] > b[i]:
            points[0] += 1
        elif a[i] < b[i]:
            points[1] += 1
    return points

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
    
