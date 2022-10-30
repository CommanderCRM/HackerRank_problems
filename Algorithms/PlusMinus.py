#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos_arr = [x for x in arr if x > 0]
    neg_arr = [x for x in arr if x < 0]
    zer_arr = [x for x in arr if x == 0]
    pos_ratio = len(pos_arr)/n
    neg_ratio = len(neg_arr)/n
    zer_ratio = len(zer_arr)/n
    return print(pos_ratio,"\n",neg_ratio,"\n",zer_ratio)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
