from functools import reduce

def annoyFunc():
    l = [(1, 20), (3, 0), (9, 10), (2, -1)]
    l.sort(key=lambda x: x[1])  # 按列表中元祖的第二个元素排序
    print(l)
    l.sort(key=lambda x: x[0])
    print(l)

def multiply_2_pure(l):
    new_list = []
    for item in l:
        new_list.append(item * 2)
    return new_list

def pureFunc():
    l = [1, 2, 3, 4, 5]
    new_list = map(lambda x: x * 2, l)              # [2， 4， 6， 8， 10]
    print(new_list)
    ##
    new_list = filter(lambda x: x % 2 == 0, l)      # [2, 4]
    ##
    product = reduce(lambda x, y: x * y, l)         # 1*2*3*4*5 = 120


# https://zhuanlan.zhihu.com/p/47124891
# 偏函数
from functools import partial

def add(*args):
    return sum(args)

add_100 = partial(add, 100)
print(add_100(1, 2, 3))  # 106

add_101 = partial(add, 101)
print(add_101(1, 2, 3))  # 107    