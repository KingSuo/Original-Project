# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: HoughFunction.py                                                                
# @Time: 2017/11/18                               
# @Contact: 648230502@qq.com
# @blog: 
# @Description: 
"""

from CalculateBGRMeans import calculate_bgr_means
import cv2
import numpy as np

def hough_circles(frame_small, method=cv2.HOUGH_GRADIENT, dp=1, minDist=120,\
                  param1=250, param2=30, minRadius=75, maxRadius=90):
    """
    
    :param frame_small: 尺寸缩小的视频帧(array)
    :param method: 霍夫检测方式
    :param dp: 
    :param minDist: 最小圆心距
    :param param1: 传给canny边缘检测的阈值上限
    :param param2: 
    :param minRadius: 最小半径
    :param maxRadius: 最大半径
    :return: cimg, circles_array[0], bgr_means_list，分别为被检测圆的二值frame；圆信息list；bgr均值list（其中单个元素由bgr均值构成）
    """
    gray_frame = cv2.cvtColor(frame_small, cv2.COLOR_BGR2GRAY)
    #circles_array.shape = (1, n, 3),n为霍夫检测到的圆的个数
    circles_array = cv2.HoughCircles(image=gray_frame, method=method, dp=dp, minDist=minDist, param1=param1,\
                               param2=param2, minRadius=minRadius, maxRadius=maxRadius)
    cimg = np.zeros(gray_frame.shape, dtype='uint8')    #后面必须加上dtype='uint8'
    if circles_array is None:
        return cimg, None, None
    else:
        circles_array = np.uint16(np.around(circles_array))
        bgr_means_list = []
        for i in circles_array[0, :]:
            cv2.circle(cimg, (i[0], i[1]), i[2]-4, 255, 4)  #i[0], i[1], i[2]分别表示的是圆的圆心及半径；255表示填充颜色；4表示填充厚度
            hough_detect_frame = cv2.bitwise_and(frame_small, frame_small, mask=cimg)
            #获得一个圆的bgr均值list
            bgr_mean_list = calculate_bgr_means(hough_detect_frame)
            #加上该圆半径信息
            bgr_mean_list.append(i[2])
            #将所有圆bgr均值及半径信息存入一个list中
            bgr_means_list.append(bgr_mean_list)
            cv2.circle(cimg, (i[0], i[1]), 1, 255, 1)

        return cimg, circles_array[0], bgr_means_list

# Test1:
# filename = r'F:\Python Study\Opencv\2017_11_14\project_1\CaptureImage_1.png'
# img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
# cv2.imshow('img', img)
# cir, temp = hough_circles(img, minRadius=150, maxRadius=200)
# cv2.imshow('cir', cir)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # Test1

# # Test2:
# # 检测大圆
# for i in range(1, 17):
#     filename = r'F:\Python Study\Opencv\2017_11_14\project_1\CaptureImage_%d.png'%i
#     img = cv2.imread(filename)
#     frame_small = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
#     # gray = cv2.cvtColor(frame_small, cv2.COLOR_BGR2GRAY)
#     cir, temp, bgr_list = hough_circles(frame_small, method=cv2.HOUGH_GRADIENT, dp=1, minDist=120,\
#                   param1=181, param2=26, minRadius=75, maxRadius=90)
#     img_cir = cv2.bitwise_and(frame_small, frame_small, mask=cir)
#     cv2.imshow('Detect Circles', np.hstack([frame_small, img_cir]))
#     print(bgr_list)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# # Test2

# # Test3:
# 检测小圆
# for i in range(1, 17):
#     filename = r'F:\Python Study\Opencv\2017_11_14\project_1\CaptureImage_%d.png'%i
#     img = cv2.imread(filename)
#     frame_small = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
#     # gray = cv2.cvtColor(frame_small, cv2.COLOR_BGR2GRAY)
#     cir, temp, bgr_list = hough_circles(frame_small, method=cv2.HOUGH_GRADIENT, dp=1, minDist=120,\
#                   param1=285, param2=30, minRadius=50, maxRadius=61)
#     img_cir = cv2.bitwise_and(frame_small, frame_small, mask=cir)
#     cv2.imshow('Detect Circle', np.hstack([frame_small, img_cir]))
#     # cv2.imshow('img_cir', img_cir)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# # Test3