#!/bin/python3

import os
import sys
import itertools

def getMoneySpent(keyboards, drives, b):
    max_price = -1
    for keyboard, drive in itertools.product(keyboards, drives):
        k_dr_sum = keyboard + drive
        if k_dr_sum <= b:
            max_price = max(max_price, k_dr_sum)
    return max_price
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
