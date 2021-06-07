#!/usr/bin/env python

from PIL import Image
import os

dir_ = os.listdir(r'img/')

def cut_img(img_item):

    c_w=100
    c_h=60

    im = Image.open(r'img/'+img_item)

    w,h = im.size

    if( (w/h) < (c_w/c_h) ):

        true_height = w / c_w * c_h
        cut_height = (h-true_height)/2
        y1 = h -cut_height
        cropImg = im.crop((0,cut_height,w,y1))
        cropImg.save(r'img/small_'+img_item,'JPEG',quality = 100)

        img = Image.open(r'img/small_'+img_item)
        img.thumbnail((100,60),Image.ANTIALIAS)
        img.save(r'img/small_'+img_item,'JPEG',quality = 100)
    else:
        true_width = h / c_h * c_w
        cut_width = (w - true_width) / 2
        x1 = w - cut_width
        cropImg = im.crop((cut_width, 0,x1 , h))
        cropImg.save(r'img/small_'+img_item,'JPEG',quality = 100)

        img = Image.open(r'img/small_'+img_item)
        img.thumbnail((100, 60), Image.ANTIALIAS)
        img.save(r'img/small_'+img_item,'JPEG',quality = 100)

for item in dir_:
    cut_img(item)