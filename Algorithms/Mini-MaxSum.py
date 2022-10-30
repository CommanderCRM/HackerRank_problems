#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sums = []
    sum1 = arr[0]+arr[2]+arr[3]+arr[4]
    sum2 = arr[1]+arr[2]+arr[3]+arr[4]
    sum3 = arr[0]+arr[1]+arr[2]+arr[3]
    sum4 = arr[0]+arr[1]+arr[3]+arr[4]
    sum5 = arr[0]+arr[1]+arr[2]+arr[4]
    sums.extend((sum1,sum2,sum3,sum4,sum5))
    min_el = min(sums)
    max_el = max(sums)
    return print(min_el, max_el)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
