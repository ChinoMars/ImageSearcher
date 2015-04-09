# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 19:31:45 2015

@author: Chino
"""

import Image

def imgRead(path):
    return Image.open(path)
    
    
def imgRegProc(img, size = (512, 512)):
    return img.resize(size).convert('RGB')
    
    
def imgToGrey(img, size = (512, 512)):
    return img.resize(size).convert('LA')

    