# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: PriceClass.py                                                                
# @Time: 2017/11/18                               
# @Contact: 648230502@qq.com
# @blog: 
# @Description: 
"""

import numpy as np

class PriceClass:
    def __init__(self):
        self.color_size_list = ['Small White:    ', 'Medium White:  ', 'Medium Red:   ', 'Big White:      ', 'Medium Yellow: ']
        self.price_list = [0.6, 2.5, 4.5, 4.5, 5.0]
        self.price_dict = {
            0: [[143, 206, 222, 50], [251, 253, 256, 62]],   # 小碗白米饭 0.6元
            1: [[143, 206, 222, 70], [251, 253, 256, 81]],   # 中碗白餐盘 2.5元
            2: [[30, 127, 213, 70], [181, 195, 243, 81]],         # 中碗红餐盘 4.5元
            3: [[143, 206, 222, 80], [251, 253, 256, 90]],   # 大碗白餐盘 4.5元
            4: [[12, 194, 240, 70], [183, 237, 256, 81]]       # 中碗黄餐盘 5  元
        }
        self.lower_attribute = []
        self.upper_attribute = []

    def get_price_dict(self, color_size_str=None, price=None):
        """
        
        :param color_size_str:颜色尺寸（string） 
        :param price: 价格（一位float）
        :return: 
        """
        if color_size_str is not None:
            index = self.color_size_list.index(color_size_str)
            print(color_size_str + 'Info:')
            print('Price: %d' % self.price_list[index])
            print('Attribute: [lower, upper] ', self.price_dict[index])

        if price is not None:
            print('Price: %d' % price)
            for i in range(len(self.price_list)):
                if price == self.price_list[i]:
                    print('Color Size %d: ' % (i + 1), self.color_size_list[i])
                    print('Attribute: [lower, upper] ', self.price_dict[i])

    def set_price(self, color_size, price=None, price_attribute=None):
        """
        :param color_size: 已有颜色和尺寸或新增颜色和尺寸
        :param price: 调整价格或新增价格
        :param price_attribute:价格属性，即对应的餐盘颜色、尺寸等。当仅仅是调整价格时，可以不给定。 
        :return: 更新后的price_dict
        """
        if color_size in self.color_size_list:
            index = self.color_size_list.index(color_size)
            #如果需要对价格进行调整，则需要修改相应的价格值
            if price is not None:
                self.price_list[index] = price
            #如果需要对价格属性进行调整，则需要修改相应的价格属性值
            if price_attribute is not None:
                self.price_dict[index] = price_attribute
        else:
            index = len(self.color_size_list)
            self.color_size_list.append(color_size)
            self.price_list[index] = price
            self.price_dict[index] = price_attribute

        return self.price_dict

    def get_attribute_array(self):
        """
        
        :return:PriceClass类的 lower_attribute及upper_attribute成员
        """
        for i in self.price_dict.keys():
            self.lower_attribute.append(self.price_dict[i][0])
            self.upper_attribute.append(self.price_dict[i][1])

        return np.array(self.lower_attribute), np.array(self.upper_attribute)