#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    highest_score,lowest_score = scores[0],scores[0]
    high_count,low_count = 0,0
    output = []
    for i in range(len(scores)):
        if scores[i] > highest_score:
            highest_score = scores[i]
            high_count += 1
        if scores[i] < lowest_score:
            lowest_score = scores[i]
            low_count += 1
    output.extend([high_count,low_count])
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
