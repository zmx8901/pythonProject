'# # 求阶乘'
# num = int(input('请输入一个整数：'))
# jc=1
# if num < 0:
#     print('输入数字不能小于0！')
# elif num == 0:
#     print('0的阶乘是0！')
# else:
#     for i in range(1, num + 1):
#         jc= jc * i
#     # print('{}的阶乘是{}'.format(num,jc))
#     print('%d的阶乘是%d'%(num,jc))

'# #输出九九乘法表'
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}*{}={}".format(i,j,i*j),end=' ')
#     print()

'# # fibo数列'
# num = int(input('你需要几项(请输入一个大于0的整数)：'))
# a,b = 1,1
# print(0,1,end=' ')
# for i in range(1, num):
#     a, b = b, a + b
#     print(a, end=' ')

'''获取指定期间内的阿姆斯特朗数
水仙花数/阿姆斯特朗数（Armstrong number
如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153
'''
# num = int(input('你需要多少范围内(请输入一个大于0的整数)：'))
# arms =[]
# for i in range(1, num + 1):
#     length = len(str(i))
#     num1 = 0
#     temp = i
#     while temp > 0:
#         num1 += (temp % 10) ** length
#         temp = temp // 10
#     if num1 == i:
#         # print('{}是阿姆斯特朗数'.format(i))
#         arms.append(i)
# print(list(arms))

'ASCII码与字符相互转换'
# for i in range(1,101):
#     print(ord(i))

'求两个数的最大公约数'
# def maxgy(a, b):
#     i = 1
#     j = max(a, b)
#     maxgys = 0
#     while i < j:
#         i += 1
#         if (a % i == 0) and (b % i == 0):
#             maxgys = i
#     return maxgys
#
#
# mylist = [30, 50]  # 只能输入两个数
# print('{}最大公约数是{}'.format(mylist, maxgy(mylist[0], mylist[1])))

'''
求多个数的最大公约数
需要能输入不定个数，需要注意函数的参数
'''

# # 这个程序还有点问题，可以参考点示例中的笔记，可以求出所有的公约数，再取大值
# def maxgy(list):
#     a = min(list)
#     b = len((list))
#     gys = []
#     maxgys = 0
#     for i in range(0, b):
#         for j in range(1, a + 1):
#             if list[i] % j != 0:
#                 continue
#             else:
#                 gys.append(j)
#             j += 1
#     print(gys)  #输出几个数各自全部的公约数
#     maxgys = max(gys)
#     return maxgys  #这里还有点不对，不应该是对序列取最大值，应该是出现2次的数取大值，可以试试用集合解决问题。
#
#
# mylist = [30, 50]
# print('{}最大公约数是{}'.format(mylist, maxgy(mylist)))

'计算数组元素之和'
# n =[1,2,3]
# sum=0
# for i in range(0, len(n)):
#     sum += n[i]
# print('n 个自然数的立方和是{}'.format(sum))

# import math
# print('The value of PI is approximately {0:2f}.'.format(math.pi))

import glob
print(glob.glob('*.py'))