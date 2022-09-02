#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:20/2/16
def is_palindrome(n):
    s = str(n)  # 用str()将整数转化成字符串
    return s == s[::-1]  # 将字符串反转，和原字符串进行比较,相同时返回


print(list(filter(is_palindrome, range(1, 200))))  # filter()进行筛选，返回一个Iterator，是惰性序列；再用list()函数获得所有结果并返回。

#以下为测试语句
T=[1,2,3]
print(T[::-1],"将字符串反转后原数列不变",T)# 将字符串反转
print(T.reverse(),"T.reverse()不返回参数，仅将数列反转",T)
