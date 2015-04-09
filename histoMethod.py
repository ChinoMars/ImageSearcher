# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 20:30:02 2015

@author: Chino
"""
import math
import operator
import matplotlib.pyplot as plt

def histoMethod(img1, img2):

#    image1 = get_thumbnail(img1)
#    image2 = get_thumbnail(img2)

    h1 = img1.histogram()
    h2 = img2.histogram()
    #histPlot(h1,h2)

    rms = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    return rms
    
    
def histPlot(x,y):
    plt.figure(figsize=(8,4))
    plt.plot(x,":",label="Target img histogram",color="red",linewidth=2)
    plt.plot(y,label="DataBase img histogram",color="blue")
    plt.xlabel("Color")
    plt.ylabel("Pixels")
    plt.title("The histogram figure of the target images")
    plt.xlim(1,len(x))
    plt.legend()
    plt.show()
        
    
    
    
if __name__ == "__main__":
    from imgImport import *    
    filepath = './imgIntest/sample11.jpg'
    sourcepath = './imgSample/sample31.jpg'
    img = imgRead(filepath)
    imgSearch = imgRegProc(img)
    imgSource = imgRead(sourcepath)
    
    imgH1 = imgSearch.histogram()
    imgH2 = imgSource.histogram()
    
    histPlot(imgH1,imgH2)