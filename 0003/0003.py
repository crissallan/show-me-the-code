__author__ = 'fansly'

import random, string, redis

base = string.ascii_letters + string.digits
def getRandom():
    return " ".join(random.sample(base, 4))
def concatenate(group):
    return "-".join([getRandom() for i in range(group)])
def generate(n):
    return [concatenate(4) for i in range(n)]

if __name__ == '__main__':
    print (generate(200))

def redis_init()
    r = redis.Redis(host='localhost', port=6379, db=0, decode_response=True)
    for key in generate(200):
        code = key.strip()
        r.lpush('code', code)

if __name__ =='__main__':
    store_redis('ActivationCode.txt')

