#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour = s[0:2]
    meridiem = s[8:10]
    min_sec = s[2:8]
    hour_min_sec = s[0:8]
    
    if meridiem == "AM":
        if hour == "12":
            return "00" + min_sec
        return hour_min_sec
    if hour == "12":
        return hour_min_sec
    return str(int(hour) + 12) + min_sec
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
