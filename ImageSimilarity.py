# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 19:09:35 2015

@author: Chino
"""
import Image
from imgImport import *
from histoMethod import *
from sortFunc import *
from fileCounter import *
from fileSave import *

if __name__ == "__main__":
    idx = 11     # can be changed for test
    filepath = './imgIntest/sample'+str(idx)+'.jpg'

    img = imgRead(filepath)
    imgSearch = imgRegProc(img)
    dataBasePath = './imgSample'
    
    # histoMethod
    rmsResult = []
    rankIdx = []
    dataBaseLen = fileCountIn(dataBasePath)
    for index in range(1,dataBaseLen+1):
        path = './imgSample/sample'+str(index)+'.jpg'
        imgData = imgRead(path)
        imgMatch = imgData
        #rmsResult.append(histoMethod(imgSearch,imgMatch))
        rmsTmp = histoMethod(imgSearch,imgMatch)
        rmsTmp = round(rmsTmp, 5)
        if len(rmsResult) < 10:
            rmsResult.append(rmsTmp)
            rankIdx.append(index)
        else:
            maxer = maxnid(rmsResult)
            if rmsTmp < maxer[0]:
                rmsResult[maxer[1]] = rmsTmp
                rankIdx[maxer[1]] = index
    
    #print rmsResult,'\n',rankIdx
    synDouSort(rmsResult,rankIdx)
    print rmsResult,'\n',rankIdx
    resultpath = './imgSample/sample'+str(rankIdx[0])+'.jpg'      
    #print resultpath
    
    makeDataFile('./tst1MatchResult.txt',zip(rmsResult,rankIdx))
    searchRes = Image.open(resultpath)
    searchRes.show()
'''
    import time
    time.sleep(3)
    for i in range(len(rankIdx)-1,-1,-1):
        resultpath = './imgSample/sample'+str(rankIdx[i])+'.jpg'
        searchRes = Image.open(resultpath)
        time.sleep(0.5)
        searchRes.show()
'''