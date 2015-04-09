# -*- coding: utf-8 -*-
"""
Created on Thu Apr 09 00:00:41 2015

@author: Chino
"""

import sys,os

def fileCountIn(dir):
    return sum([len(files) for root,dirs,files in os.walk(dir)])

#os.walk(dir)会返回一个三元组：（当前目录，子目录列表，文件列表）
#所以len(files)就是获取当前目录下的文件数，然后每个目录下的文件数求和即可

if __name__=='__main__':
    if len(sys.argv)==2:
	dir=sys.argv[1]
	print 'Total files in %s is:%d' %(dir,fileCountIn(dir))
    else:
	print 'usage:filecount.py dirname'

 
#print fileCountIn('E:/Dropbox/WorkFiles/ImageSimilarityMeasurement/ProjectFile/imgSample')