# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 10:17:04 2020

@author: sigar
"""
import re
para = input()

pattern = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s')

for sentence in re.split(pattern,para):
    print(sentence)

