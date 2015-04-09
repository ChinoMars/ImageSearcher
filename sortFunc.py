# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 20:55:13 2015

@author: Chino
"""

def swap(a1,a2):
    tmp = a1
    a1 = a2
    a2 = tmp

def maxnid(s):
    numnid = [0,0]
    if len(s) == 1:
        numnid[0] = s[0]
        numnid[1] = 0
        return numnid
    else:
        numnid[0] = s[0]
        numnid[1] = 0
        for idx in range(1,len(s)):
            if s[idx] > numnid[0]:
                numnid[0] = s[idx]
                numnid[1] = idx
        return numnid

def synDouSort(sdata,sidx):
    for j in range(len(sdata)-1,-1,-1):
        for i in range(j):
            if sdata[i]>sdata[i+1]:
                sdata[i],sdata[i+1] = sdata[i+1],sdata[i]
                sidx[i],sidx[i+1] = sidx[i+1],sidx[i]

def sqsort(s):
    if s == []:
        return []
    else:
        pivot = s[0]
        lesser = sqsort([x for x in s[1:] if x<pivot])
        larger = sqsort([x for x in s[1:] if x>=pivot])
        return lesser+[pivot]+larger
