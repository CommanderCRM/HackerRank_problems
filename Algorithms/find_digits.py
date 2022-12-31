import math
import os
import random
import re
import sys

def findDigits(n):
    digits = [int(d) for d in str(n)]
    divisor_count = sum([1 for d in digits if d != 0 and n % d == 0])
    return divisor_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
