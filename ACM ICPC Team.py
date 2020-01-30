# -*- coding: utf-8 -*-
"""
Created on March 2018

@author: Salman
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
# Complete the acmTeam function below.
def acmTeam(topics):
    comb = combinations(topics,2)
    m = 0
    count = 0
    for i in comb:
        n = str(bin(((int(i[0],2) | int(i[1],2)))))[2:].count('1')
        if n > m:            
            m = n
            count = 1
        elif n == m:
            count += 1
    return (m, count)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
