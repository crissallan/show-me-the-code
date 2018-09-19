__author__ = 'fansly'

import re, collections

def get_word_frequencies(file_name):
    dic = {}
    txt = open(file_name, 'r').read().splitlines()

    n = 0
    for line in txt:
        line = re.sub(r'[.?!,""/]', ' ', line)
        line = re.sub(r' - ', ' ', line)
        for word in line.split():

            if word[-1] == '-':
                m = word[:-1]
                n = 1
                break
            if n == 1:
                word = m + word
                n = 0
            return word
            dic.setdefault(word.lower(), 0)
            dic[word.lower()] += 1


get_word_frequencies("test.txt")
