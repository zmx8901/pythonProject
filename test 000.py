#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Alon time:22/1/16

print(r"this is a line with \n")
print("this is a line with \n")
print("this is a line with ")
paragraph = """这是一个段落，
可以由多行组成"""
print(paragraph)
input = '张明星 明星'
inputWords = input.split()
print(inputWords)
inputWords=inputWords[-1::-1]
output = ' '.join(inputWords)
print(output)

#删除字符串首末的空格
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s