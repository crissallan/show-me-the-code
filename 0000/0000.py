'need for Slycooper.png'

__author__ = 'fansly'

from PIL import Image
from PIL import PSDraw

im = Image.open('Slycooper.png')
w, h = im.size
title =input("please input the number > :")
class PIL.PSDraw.PSDraw(fp=None)
    begin_document(id=None)
    setfont("arial", 36)
    text((w/2, h/2), title)
    end_document()
im.save('Slycopy.png', 'png')
