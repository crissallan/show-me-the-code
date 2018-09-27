__author__ = 'fansly'

import os
import collections
from string import punctuation

with open('test.txt', 'r') as ef:
    str1 = ef.read().split(' ')
b = collections.Counter(str1)
with open('result.txt', 'w') as result_file:
    for key,value in b.items():
        result_file.write(key+':'+str(value)+'\n')
