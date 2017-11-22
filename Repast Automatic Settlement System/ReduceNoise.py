# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: ReduceNoise.py                                                                
# @Time: 2017/11/14                                   
# @Contact: 648230502@qq.com
# @blog: http://blog.csdn.net/
# @Description: 
"""
import numpy as np

def reduce_noise(frameArray, thresholdX=3000, thresholdY=2500):
    frameArrayTemp = np.array(frameArray)
    frameArrayTempX = frameArrayTemp.sum(axis=1)

    for i in range(len(frameArrayTempX)):
        if frameArrayTempX[i].sum() <= thresholdX:
            frameArrayTemp[i] = 0

    frameArrayTempT = frameArrayTemp.T
    frameArrayTempY = frameArrayTempT.sum(axis=1)
    for i in range(len(frameArrayTempY)):
        if frameArrayTempY[i].sum() <= thresholdY:
            frameArrayTempT[i] = 0

    return frameArrayTempT.T