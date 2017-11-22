# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: ShowInfo.py                                                                
# @Time: 2017/11/18                               
# @Contact: 648230502@qq.com
# @blog: 
# @Description: 
"""

import cv2

def show_info(frame_small, show_info_list):
    """
    
    :param frame_small:尺寸缩小的视频帧(array) 
    :param show_info_list: 显示信息（list）
    :return:包含显示信息的frame 
    """
    total_price = sum([info_temp[1] for info_temp in show_info_list])
    # total_price = np.array(show_info_list).sum(axis=0)[1]   #show_info_list中的元素含有字符串类型，不可进行sum运算
    cv2.putText(frame_small, 'Total Price: %s' % total_price, (0, 26), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 2)
    for i in range(len(show_info_list)):
        info = show_info_list[i]
        cv2.putText(frame_small, '%d. %s %s yuan' % ((i + 1), info[0], info[1]), (0, 26 * (i + 2)), 0, 0.5, (255, 0, 0), 2)

    # cv2.imshow('Automatic Charging System', frame_small)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return frame_small