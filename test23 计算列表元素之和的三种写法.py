def countX(lst):  # 使用for语句
    count = 0
    for j in lst:
        count += j
    return count


def sum_lst(lst):  # 使用while语句
    sum = 0
    i = 0
    while i < len(lst):
        sum += lst[i]  '注意这是不是 +i,是加列表中的元素'
        i += 1
    return sum


def sumOfList(list, size):  # 使用递归
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)


lst = [8, 6, 8, 10, 8, 20, 10, 20, 10]
total = sumOfList(lst, len(lst))
print(countX(lst))
print(sum_lst(lst))
print("列表元素之和为: ", total)
