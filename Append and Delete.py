# -*- coding: utf-8 -*-
"""
Created on March 2018

@author: Salman
"""

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    # If k is big enough than everything is possible.
    if len(s) + len(t) <= k:
        return 'Yes'

    # Find how big is the difference.
    idx = 0
    while idx < len(s) and idx < len(t):
        if s[idx] != t[idx]:
            break
        idx += 1
 
    # If the difference size is smaller than k and both are
    # even or odd, then it is possible.
    diff_size = len(s[idx:]) + len(t[idx:])
    if diff_size <= k and diff_size % 2 == k % 2:
        return 'Yes'

    return 'No'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    t = raw_input()

    k = int(raw_input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
