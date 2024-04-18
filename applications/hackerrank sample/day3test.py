#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def isPal(s, l ,r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def palindromeIndex(s):
    l = 0
    r = len(s) -1

    if isPal(s, l, r):
        return -1
    
    while l < r:
        if isPal(s, l+1, r):
            return l
        if isPal(s, l, r-1):
            return r
    return -1        
                
    # Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
