# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 15:01:23 2022

@author: amar.gadipudi
"""

import sys

file_name = sys.argv[1]

text_file = open(file_name)

for line in text_file:
    line = line.strip("\n")
    print(line)