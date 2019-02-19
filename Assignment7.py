# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 17:27:26 2019

@author: psarka
"""
import numpy as np

def moving_avg(in_array, window):
    n=in_array.size
    k=window
    out_seq=n-k+1
    outlist=list([])
    for i in range(0,out_seq):
        arr=in_array[i:i+k]
        av=np.sum(arr)/k
        outlist.insert(i,av)
    return(outlist)