__author__ = 'fansly'

import redis


def code2redis():
    f = open('Code.txt', 'r')
    r = redis.Redis(host='localhost', port=6379, db=0)
    i = 0
    for line in f.readlines():
        r.zadd('codes', line.strip(), i)
        i += 1

if __name__ =='__main__':
    code2redis()
