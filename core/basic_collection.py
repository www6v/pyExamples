####### 不可变数据类型
# 整型

# 字符串

# tuple元组
def tupleFunc():
    # tup
    tup = (3, 2, 3, 7, 8, 1)
    tup.count(3)
    tup.index(7)
    reversed(tup)
    # list()
    sorted(tup)   


####### 可变数据类型
# 列表
def listFunc():
    ##
    x = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6]
    y = [1, 2, 3, 4, 5]
    print(all_unique(x))
    print(all_unique(y))

    ## list
    l = [3, 2, 3, 7, 8, 1]
    print(l[1:2])
    l.count(3)
    l.index(7)
    l.reverse()
    l.sort()





# dict
def dictFunc():
    ##
    d = {'name': 'jason', 'age': 20}

    d['gender'] = 'male'
    d['dob'] = '1999-02-01'
    d['dob'] = '1998-01-01'
    d.pop('dob')
    print(d)

    d = {'b': 1, 'a': 2, 'c': 10}
    d_sorted_by_key = sorted(d.items(), key=lambda s: s[0])
    d_sorted_by_value = sorted(d.items(), key=lambda s: s[1])
    print(d_sorted_by_key)
    print(d_sorted_by_value)

# set
def setFunc():
    ##
    s = {1, 2, 3}
    s.add(4)
    s.remove(4)
    print(s)     


def enumerateFunc():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index, item in enumerate(a):
        print(index, item)

        
# def shallowCopy():
#     l1 = [1, 2, 3]
#     l2 = list(l1)
#     print( l1 == l2 )
#     print( l1 is l2 )

# # 浅拷贝通常会带来一些副作用
# def  shallowCopy1():
#     l1 = [[1, 2], (30, 40)]
#     l2 = list(l1)
#     l1.append(100)
#     l1[0].append(3)
#     print(l1)
#     print(l2)
#     l1[1] += (50, 60)
#     print(l1)
#     print(l2)


# def deepcopy():
#     import copy
#     l1 = [[1, 2], (30, 40)]
#     l2 = copy.deepcopy(l1)
#     l1.append(100)
#     l1[0].append(3)
#     print(l1)
#     print(l2)



def all_unique(lst):
        return len(lst) == len(set(lst))


from collections import deque
from typing import Callable, Deque, Dict, Iterable, List, Optional
class Scheduler:
    def __init__(self)-> None:
        print()  
        self.waiting: Deque[str] = deque()
        self.running: Deque[str] = deque()        
        self.swapped: Deque[str] = deque()

        self.waiting.insert(1, 'abc')
        self.waiting.insert(1, '111')
        self.running.insert(2, 'def')
        self.running.insert(2, '222')
        self.swapped.insert(3, 'ghi')            

    def abort_seq_group(self) -> None:
        for state_queue in [self.waiting, self.running, self.swapped]:
            print(state_queue)               

            for seq_group in state_queue:    
                print(seq_group, " ",seq_group.isnumeric())