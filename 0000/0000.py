'need for Slycooper.png'

__author__ = 'fansly'

from PIL import Image, ImageDraw, ImageFont

img = Image.open('Slycooper.png')
draw = ImageDraw.Draw(img)
textfont = ImageFont.truetype('Ubuntu-B.ttf', 128)
w, h = img.size
draw.text((w-256, 50), '99+', font=textfont, fill = 'red')
img.save('Slycopy.png', 'png')
