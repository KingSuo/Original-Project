# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: MagnifyProcess.py                                                                
# @Time: 2017/11/14                                  
# @Contact: 648230502@qq.com
# @blog: http://blog.csdn.net/
# @Description: 放大处理函数
"""
import numpy as np

def magnify_process(dataArray1, dataArray2):
    """
    
    :param dataArray1:未被缩放的数据 
    :param dataArray2: 被缩放的数据
    :return: 放大后的数据
    """

    #注意：row_original - row_compression与column_original - column_compression的值必须是偶数
    row_original, column_original = dataArray1.shape
    row_compression, column_compression = dataArray2.shape
    row_bias = int((row_original - row_compression) / 2)
    column_bias = int((column_original - column_compression) / 2)

    emptyArray = np.zeros((row_original, column_original))
    emptyArray[row_bias:(row_original - row_bias), column_bias:(column_original - column_bias)] = np.array(dataArray2)

    return emptyArray