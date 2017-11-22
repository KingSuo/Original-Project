# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: LoadVideo.py                                                                
# @Time: 2017/11/14                                  
# @Contact: 648230502@qq.com
# @blog: 
# @Description: 
"""

from WipeOff import wipe_off
from TwoValuedProcess import two_value_process
from MagnifyProcess import magnify_process
from ShowInfo import show_info
from CalculatePrice import calculate_price
from PriceClass import PriceClass
from HoughFunction import hough_circles
from ColorDetect import color_detect
from ShowPower import show_power
from ReduceNoise import reduce_noise
import cv2
import numpy as np

def load_video(filename):
    cap = cv2.VideoCapture(filename)

    price_class = PriceClass()
    lower_attribute_array, upper_attribute_array = price_class.get_attribute_array()
    number = 0  #记录当前帧所在位置
    actionFlag = 0  #检测到完整对象时记为0，否则为1
    times = 35   #表示从检测到完整对象的那一帧开始，取其后第35个的帧
    k = 0   #表示第k个保留图
    show_flag = 0   #调用霍夫函数标志位
    Y_BGR_value_range = [[0, 200, 220], [60, 255, 255]]  # 黄色对应BGR变化下限和上限
    W_BGR_value_range = [[210, 240, 230], [255, 255, 255]]  # 白色对应BGR变化下限和上限
    R_BGR_value_range = [[0, 0, 180], [60, 50, 244]]  # 红色对应BGR变化下限和上限

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret is False:
            break
        gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)     #shape = (720, 1280)
        gray2 = cv2.resize(gray1, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)  #shape = (360, 640)
        # gray3 = cv2.resize(gray1, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
        gray3 = np.array(gray2)
        gray4 = cv2.resize(gray1, (638, 358), interpolation=cv2.INTER_CUBIC)  #shape = (356, 636)
        frame_small = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
        frame_small_for_color_detect = frame_small
        cv2.putText(frame_small, 'Designed by KingSuo', (450, 350), cv2.FONT_HERSHEY_COMPLEX, 0.4, (150, 255, 255), 1)
        cv2.putText(frame_small, 'Repast Automatic Settlement System', (130, 16), cv2.FONT_HERSHEY_COMPLEX, 0.6, (200, 255, 255), 1)
        # hsv_frame_small = cv2.cvtColor(frame_small, cv2.COLOR_BGR2HSV)  # shape = (720, 1280)

        edges2Frame = cv2.Canny(gray2, 100, 200, edges=True, apertureSize=3, L2gradient=True)
        # edges3Frame = cv2.Canny(gray3, 100, 200, edges=True, apertureSize=3, L2gradient=True)
        edges3Frame = np.array(edges2Frame)
        edges4Frame = cv2.Canny(gray4, 100, 200, edges=True, apertureSize=3, L2gradient=True)

        edges2ReduceNoiseFrame = reduce_noise(edges2Frame, thresholdX=2000, thresholdY=1000)
        edges3ReduceNoiseFrame = reduce_noise(edges3Frame, thresholdX=2200, thresholdY=3000)
        edges4ReduceNoiseFrame = reduce_noise(edges4Frame, thresholdX=1600, thresholdY=800)

        if show_flag == 1:  #每1+1帧执行一次
            show_flag = 0
            # 检测大圆
            Big_circles_frame, Big_circles_array, Big_bgr_means_list = hough_circles(frame_small, param1=181, param2=26, minRadius=75, maxRadius=90)
            # 检测小圆
            Small_circles_frame, Small_circles_array, Small_bgr_means_list = hough_circles(frame_small, param1=285, param2=30, minRadius=50, maxRadius=61)
            bgr_means_list = []
            if Big_bgr_means_list is None and Small_bgr_means_list is None:
                cv2.putText(frame_small, 'Wait to Detect...', (0, 26), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 2)
            elif Big_bgr_means_list is None and Small_bgr_means_list is not None:
                bgr_means_list = Small_bgr_means_list
                #circles_array_list用于存储检测到的圆的信息，包括圆心坐标及半径大小
                circles_array_list = [circles_info for circles_info in Small_circles_array]
                circles_frame = Small_circles_frame
                show_info_list = calculate_price(price_class, bgr_means_list, lower_attribute_array, upper_attribute_array)
                frame_small = show_info(frame_small, show_info_list)
                # 标记圆
                for i in range(len(circles_array_list)):
                    circle_info = circles_array_list[i]
                    cv2.circle(frame_small, (circle_info[0], circle_info[1]), circle_info[2], (0, 255, 0), 4)
                    cv2.putText(frame_small, '%s' % (i + 1), (circle_info[0], circle_info[1]), 0, 1, (255, 0, 0), 6)
            elif Small_bgr_means_list is None and Big_bgr_means_list is not None:
                bgr_means_list = Big_bgr_means_list
                # circles_array_list用于存储检测到的圆的信息，包括圆心坐标及半径大小
                circles_array_list = [circles_info for circles_info in Big_circles_array]
                circles_frame = Big_circles_frame
                show_info_list = calculate_price(price_class, bgr_means_list, lower_attribute_array, upper_attribute_array)
                frame_small = show_info(frame_small, show_info_list)
                # 标记圆
                for i in range(len(circles_array_list)):
                    circle_info = circles_array_list[i]
                    cv2.circle(frame_small, (circle_info[0], circle_info[1]), circle_info[2], (0, 255, 0), 4)
                    cv2.putText(frame_small, '%s' % (i + 1), (circle_info[0], circle_info[1]), 0, 1, (255, 0, 0), 6)
            else:
                bgr_means_list = Big_bgr_means_list + Small_bgr_means_list
                # circles_array_list用于存储检测到的圆的信息，包括圆心坐标及半径大小
                circles_array_list = [circles_info for circles_info in Big_circles_array] + [circles_info for circles_info in Small_circles_array]
                circles_frame = cv2.bitwise_or(Small_circles_frame, Big_circles_frame)
                show_info_list = calculate_price(price_class, bgr_means_list, lower_attribute_array, upper_attribute_array)
                frame_small = show_info(frame_small, show_info_list)
                # 标记圆
                for i in range(len(circles_array_list)):
                    circle_info = circles_array_list[i]
                    cv2.circle(frame_small, (circle_info[0], circle_info[1]), circle_info[2], (0, 255, 0), 4)
                    cv2.putText(frame_small, '%s' % (i + 1), (circle_info[0], circle_info[1]), 0, 1, (255, 0, 0), 6)


        # twoValueFrame = two_value_process(edges4ReduceNoiseFrame)
        # magnifyValueFrame = magnify_process(edges2ReduceNoiseFrame, twoValueFrame)
        # wipeOffFrame = wipe_off(edges2ReduceNoiseFrame, magnifyValueFrame)

        # cv2.imshow('Circles Detect', circles_frame)
        cv2.imshow('Edges Detect', edges2ReduceNoiseFrame)
        cv2.imshow('Result', frame_small)
        # cv2.imshow('TwoValue:', twoValueFrame)
        # cv2.imshow('Magnify', magnifyValueFrame)
        # cv2.imshow('WipeOff', wipeOffFrame)

        powerValue = show_power(edges3ReduceNoiseFrame)
        if powerValue <= 400000 and actionFlag == 0:  #没有完整的对象被检测到
            actionFlag = 1
        elif powerValue >= 700000 and actionFlag == 1:  #检测到完整的对象
            times -= 1
            if times <= 0:
                times = 35
                k += 1
                actionFlag = 0

                y_result = color_detect(frame_small, Y_BGR_value_range)
                w_result = color_detect(frame_small, W_BGR_value_range)
                r_result = color_detect(frame_small, R_BGR_value_range)
                combination_0 = cv2.bitwise_or(y_result, w_result)
                combination_1 = cv2.bitwise_or(combination_0, r_result)
                cv2.imshow('Color Detect', combination_1)
                cv2.imwrite('./CaptureImage_%d.png'% k, frame)
                cv2.imwrite('./EdgeImage_%d.png' % k, edges2ReduceNoiseFrame)
                cv2.imwrite('./ColorDetect_%d.png' % k, combination_1)
                cv2.imwrite('./Calculate Price_%d.png' % k, frame_small)
                cv2.imwrite('./Circles Frame_%d.png' % k, circles_frame)
                circles_detect = cv2.bitwise_and(frame_small, frame_small, mask=circles_frame)
                cv2.imwrite('./Circles Detect_%d.png' % k, circles_detect)

                print('k: ', k)
                print('powerValue: ', powerValue)
                print('number: ', number)
                print('bgr_means_list: ', bgr_means_list)
        number += 1
        show_flag +=1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        del gray1, gray2, gray3, gray4, edges2Frame, edges3Frame, edges4Frame, edges2ReduceNoiseFrame, \
            edges3ReduceNoiseFrame, edges4ReduceNoiseFrame

    cap.release()
    cv2.destroyAllWindows()