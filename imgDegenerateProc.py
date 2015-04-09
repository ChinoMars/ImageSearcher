# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 19:42:57 2015

@author: Chino
"""

from PIL import Image

def makeRegularsize(img, size = (512, 512)):
    return img.resize(size).convert('RGB')

def imgRead():
    filepath = './imgSample/'
    for idx in range(1,74):
        img = Image.open(filepath+'test ('+str(idx)+').jpg')
        newImg = makeRegularsize(img,size = (512, 512))
        newImg.save(filepath+'sample'+str(idx)+'.jpg')


if __name__ == "__main__":
    imgRead()