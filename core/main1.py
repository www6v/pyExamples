import json
from functools import reduce

import pandas as pd

from core.obj import Doc
from core.obj1 import Video, Document


def jsonHandler():
    with open('abc.json', 'r') as f:
        data = json.loads(f.read())
    df_nested_list = pd.json_normalize(data, record_path=['students'])  # 指定输出 student 项目下的内容
    print(df_nested_list)

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


def objFunc():
    empty_book = Doc.create_empty_book('What Every Man Thinks About Apart from Sex', 'Professor Sheridan Simove')
    print(empty_book.get_context_length())
    print(empty_book.get_welcome('indeed nothing'))


def objFunc1():
    harry_potter_book = Document('Harry Potter(Book)', 'J. K. Rowling',
                                 '... Forever Do not believe any thing is capable of thinking independently ...')
    harry_potter_movie = Video('Harry Potter(Movie)', 'J. K. Rowling', 120)
    print(harry_potter_book.object_type)
    print(harry_potter_movie.object_type)

    harry_potter_book.print_title()
    harry_potter_movie.print_title()
    print(harry_potter_book.get_context_length())
    print(harry_potter_movie.get_context_length())


if __name__ == '__main__':
    jsonHandler()
    annoyFunc()
    pureFunc()
    objFunc()
    objFunc1()







