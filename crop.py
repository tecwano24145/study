#!/usr/bin/env python

from PIL import Image

c_w=100
c_h=60

im = Image.open(r'img/123.jpg')

w,h = im.size

if( (w/h) < (c_w/c_h) ):

    true_height = w / c_w * c_h
    cut_height = (h-true_height)/2
    print(cut_height)
    y1 = h -cut_height
    print(y1)
    cropImg = im.crop((0,cut_height,w,y1))
    cropImg.save(r'img/000.jpg')

    img = Image.open(r'img/000.jpg')
    img.thumbnail((100,60),Image.ANTIALIAS)
    img.save(r'img/000.jpg')
else:
    true_height = w / c_w * c_h
    cut_height = (h - true_height) / 2
    print(cut_height)
    y1 = h - cut_height
    print(y1)
    cropImg = im.crop((0, cut_height, w, y1))
    cropImg.save(r'img/000.jpg')

    img = Image.open(r'img/000.jpg')
    img.thumbnail((100, 60), Image.ANTIALIAS)
    img.save(r'img/000.jpg')


