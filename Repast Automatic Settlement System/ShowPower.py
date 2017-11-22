# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: ShowPower.py                                                                
# @Time: 2017/11/14                                  
# @Contact: 648230502@qq.com
# @blog: http://blog.csdn.net/
# @Description: 
"""

import cv2
import numpy as np

def show_power(grayArray):
    grayArrayTemp = np.array(grayArray)
    row, column = grayArrayTemp.shape
    powerValue = grayArrayTemp.sum()
    grayArrayTempX = grayArrayTemp.sum(axis=0)
    emptyFrame = np.zeros((row, column, 3), np.uint8)
    # grayArrayTempX_min = min(grayArrayTempX)
    # grayArrayTempX_max = max(grayArrayTempX)
    grayArrayTempX_min = 0
    grayArrayTempX_max = 255 * row
    for i in range(column):
        cv2.rectangle(emptyFrame, (i, row), (i, row - int(
            (grayArrayTempX[i] - grayArrayTempX_min) * grayArrayTempX[i] / (
            grayArrayTempX_max - grayArrayTempX_min + 1))), (0, 255, 0), 2)
    cv2.putText(emptyFrame, 'Power Value: %d'%powerValue, (0, 12), 0, 0.5, (0, 0, 255), 2)
    cv2.imshow('Power', emptyFrame)

    return powerValue
