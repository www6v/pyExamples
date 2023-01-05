import os
import psutil

def is_iterable(param):
    try:
        iter(param)
        return True
    except TypeError:
        return False


def iter_test():
    params = [
        1234,
        '1234',
        [1, 2, 3, 4],
        set([1, 2, 3, 4]),
        {1: 1, 2: 2, 3: 3, 4: 4},
        (1, 2, 3, 4)
    ]

    for param in params:
        print('{} is iterable? {}'.format(param, is_iterable(param)))


# 显示当前 python 程序占用的内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))

def test_iterator():
     show_memory_info('initing iterator')
     list_1 = [i for i in range(100000000)]   ## 迭代器会占用大量内存
     show_memory_info('after iterator initiated')
     print(sum(list_1))
     show_memory_info('after sum called')

def test_generator():
     show_memory_info('initing generator')
     list_2 = (i for i in range(100000000))   ## 生成器并不会像迭代器一样占用大量内存，只有在被使用的时候才会调用
     show_memory_info('after generator initiated')
     print(sum(list_2))
     show_memory_info('after sum called')