class MyInputError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return ("{} is invalid input".format(repr(self.value)))

def all_unique(lst):
        return len(lst) == len(set(lst))

def listAndTuple():
    ##
    x = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6]
    y = [1, 2, 3, 4, 5]
    print(all_unique(x))
    print(all_unique(y))

    ## list vs. tup
    l = [3, 2, 3, 7, 8, 1]
    print(l[1:2])
    l.count(3)
    l.index(7)
    l.reverse()
    l.sort()

    tup = (3, 2, 3, 7, 8, 1)
    tup.count(3)
    tup.index(7)
    list(reversed(tup))
    sorted(tup)


def dictAndSet():
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

    ##
    s = {1, 2, 3}
    s.add(4)
    s.remove(4)
    print(s)


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

def shallowCopy():
    l1 = [1, 2, 3]
    l2 = list(l1)
    print( l1 == l2 )
    print( l1 is l2 )

# 浅拷贝通常会带来一些副作用
def  shallowCopy1():
    l1 = [[1, 2], (30, 40)]
    l2 = list(l1)
    l1.append(100)
    l1[0].append(3)
    print(l1)
    print(l2)
    l1[1] += (50, 60)
    print(l1)
    print(l2)


def deepcopy():
    import copy
    l1 = [[1, 2], (30, 40)]
    l2 = copy.deepcopy(l1)
    l1.append(100)
    l1[0].append(3)
    print(l1)
    print(l2)