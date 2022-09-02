# 测试print语句
print('%s' % 3.1415926)
print('Hello, %s,%s,%0.2f' % ('world', 3.1415926, 3.1415926))
# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
print('Age: %s. Gender: %s' % (25, True))

classmates = ['Michael', 'Bob', 'Tracy']
classmates.append('henry')
print(classmates, classmates[:2], classmates[2], ',"len(classmates)="', len(classmates))
classmates.insert(1, 'alon')
print(classmates, classmates[:2], classmates[2], ',"len(classmates)="', len(classmates))
classmates.pop()
print(classmates)
classmates.pop(-2)  # pop:删除list末尾的元素
print(classmates)
classmates[-1] = 'lucky'
print(classmates)
kongmaomao = (1,)
print(kongmaomao)
# kongmaomao[1]=2 元组一旦初始化就不能修改,下一行为元组中的可变性，采用list为元素
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][2], L[0: 2])

num1 = float(input('输入一个数字：'))
num_sqrt = num1 ** 0.5
print('数字%0.2f的方根是%0.2f' % (num1, num_sqrt))
print(f'数字{num1:0.2f}的方根是{num_sqrt:0.2f}')
print('数字{:0.2f}的方根是{:0.2f}'.format(num1, num_sqrt))
print("数字{0:4f}的方根是{1:5f}".format(num1, num_sqrt))

list1 = [10, 20, 4, 45, 99]
list1.sort()
print("最小元素为:", list1[:1])
print("最小元素为:", *list1[:1])
