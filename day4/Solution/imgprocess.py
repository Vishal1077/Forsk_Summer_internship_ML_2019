# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:35:32 2019

@author: user
"""


from PIL import Image
img = Image.open('sample1.jpg').convert('LA')
img.save('greyscale.png')
img.show()

img_rotate = img.rotate(90)
img_rotate.show()

width, height = img_rotate.size
hw = width/2
hh = height/2

img_rotate = img_rotate.crop((hw-80,hh-102,hw+80,hh+102))
img.show()

img_rotate.thumbnail((75,75))
img_rotate.show()