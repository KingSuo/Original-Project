# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: ColorDetect.py                                                                
# @Time: 2017/11/14                                  
# @Contact: 648230502@qq.com
# @blog: 
# @Description: 
"""

from ReduceNoise import reduce_noise
import cv2
import numpy as np

def color_detect(frame_small, bgr_value_range):
    """
    
    :param frame_small:尺寸缩小的视频帧(array) 
    :param bgr_value_range: bgr值变化范围（list），第一个值为变化下限，第二个值为上限
    :return: 目标颜色检测结果（frame），除目标颜色外，其余为黑色（0， 0， 0）
    """
    frame_small_temp = np.array(frame_small)
    mask = cv2.inRange(frame_small_temp, np.array(bgr_value_range[0]), np.array(bgr_value_range[1]))
    mask_reduce_noise = reduce_noise(mask, thresholdX=500, thresholdY=500)
    result = cv2.bitwise_and(frame_small_temp, frame_small_temp, mask=mask_reduce_noise)
    del frame_small_temp

    return result

# def color_detect(frame_small, hsv_frame_small, bgr_range_array):
#     frame_small_temp = np.array(frame_small)
#     mask = cv2.inRange(hsv_frame_small, np.array(bgr_range_array[0]), np.array(bgr_range_array[1]))
#     detect_result_frame = cv2.bitwise_and(frame_small_temp, frame_small_temp, mask=mask)
#     del frame_small_temp
#
#     return detect_result_frame
