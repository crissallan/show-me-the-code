#-*- coding: UTF-8 -*-
__author__ = 'fansly'

import os
from PIL import Image

s = '/home/hallucigenia/圖片'
s2 = os.path.join('s', 'output')

def processImage(filesource, destsource, name):
    im = Image.open(name)
    w, h = im.size
    im.thumbnail(w / h * 640, 640)
    im.save(name, 'jpg')

def run():
    os.chdir(s)
    for i in os.listdir(s):
            processImage(s, s2, i)

if __name__ == '__main__':
    run()
