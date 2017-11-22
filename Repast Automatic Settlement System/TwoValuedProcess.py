# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: TwoValueProcess.py                                                                
# @Time: 2017/11/14                                  
# @Contact: 648230502@qq.com
# @blog: http://blog.csdn.net/
# @Description: 
"""
import numpy as np

def two_value_process(dataArray):
    """
    
    :param dataArray:传入被缩放的frame数据 
    :return: 经过二值化、翻转的frame数据
    """
    dataArrayTemp = np.array(dataArray)

    for i in range(len(dataArrayTemp)):
        line = dataArrayTemp[i]
        if line.sum() <= 1550:    #255*6,即此行只有6个点
            dataArrayTemp[i] = 255    #将此行数值全部写为255
        else:
            for j in range(len(line)):
                if line[j] != 0:
                    break
                else:
                    dataArrayTemp[i, j] = 255
            for j in range(len(line) - 1, -1, -1):
                if line[j] != 0:
                    break
                else:
                    dataArrayTemp[i, j] = 255

    # 返回的数据与原数据相反，且由0，1构成，即若原数据为[[0, 255, 0, 255], [255, 255, 0, 0]],返回[[1, 0, 1, 0], [0, 0, 1, 1]]
    return (255 - dataArrayTemp) / 255