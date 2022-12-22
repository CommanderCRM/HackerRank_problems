import math
import os
import random
import re
import sys


def hourglassSum(arr):
    max_sum = -2147483648
    for i in range(4):
        for j in range(4):
             hourglass_sum = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
             max_sum = max(max_sum, hourglass_sum)
    return max_sum
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
