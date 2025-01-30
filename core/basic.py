import json
import pandas as pd

class MyInputError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return ("{} is invalid input".format(repr(self.value)))


def ifAndLoop():
    ##
    id = 2;
    if id == 0:
        print('red')
    elif id == 1:
        print('yellow')
    else:
        print('green')

    ##
    l = [5, 2, 3, 9]
    for item in l:
        print(item)

    print('-')
    l = [6, 7, 1, 2, 3, 4, 5]
    for index in range(0, len(l)):
      if index < 5:
         print(l[index])

    print('-')
    l = [1, 2, 3, 4, 5, 6, 7]
    for index, item in enumerate(l):
      if index < 5:
         print(index,item)

def errerHandling():
    try:
        s = input('please enter two numbers separated by comma: ')
        num1 = int(s.split(',')[0].strip())
        num2 = int(s.split(',')[1].strip())
    except ValueError as err:
        print('Value Error: {}'.format(err))
    except IndexError as err:
        print('Index Error: {}'.format(err))
    except:
        print('Other error')
    print('continue')


def errorHandling1():
    try:
        raise MyInputError(1)
    except MyInputError as err:
        print('error: {}'.format(err))

def compare():
    a = 257
    b = 257
    print( id(a) )
    print( id(b) )
    print(a == b)  # 对象间的值是否相等
    print(a is b)  # 是否指向同一个内存地址


def jsonHandler():
    with open('abc.json', 'r') as f:
        data = json.loads(f.read())
    df_nested_list = pd.json_normalize(data, record_path=['students'])  # 指定输出 student 项目下的内容
    print(df_nested_list)
