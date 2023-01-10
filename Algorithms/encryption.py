import math
import os
import random
import re
import sys


def encryption(s):
    s_nosp = s.replace(" ", "")
    
    s_len = len(s_nosp)
    
    len_sqrt = math.sqrt(s_len)
    num_rows = math.floor(len_sqrt)
    num_cols = math.ceil(len_sqrt)
    
    if num_rows * num_cols < s_len:
        num_rows += 1
    
    string_list = [['']*num_cols for i in range(num_rows)]

    for i in range(num_rows*num_cols):
        if i >= len(s_nosp):
            break
        string_list[i//num_cols][i%num_cols] = s_nosp[i]

    cypher_text = []
    for j in range(num_cols):
        word = ''
        for i in range(num_rows):
            word += string_list[i][j]
        cypher_text.append(word)

    return(" ".join(cypher_text))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
