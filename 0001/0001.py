__author__ = 'fansly'

import random, string

def get_code(num):
    base = string.ascii_letters + string.digits
    f = open('Code.txt', 'w')
    for i in range(num):
        code =  " "
        for s in range(20):
            code +=random.choice(base)
        f.write(code+'\n')
    f.close()

if __name__ == '__main__':
    get_code(200)
