# -*- coding: utf-8 -*-
"""
Created on Thu Apr 09 14:09:01 2015

@author: Chino
"""

def makeDataFile(filename, data):
    datafile = open(filename,'a')
    if type(data) is str:
        datafile.write(data+'\n')
    else:
        datafile.write(str(data)+'\n')
    datafile.close()
    
    
    
if __name__ == "__main__":
    a = [1,2,3,4,5,6]
    makeDataFile('./test1.txt',a)