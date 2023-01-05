

def reference():
    a = 1
    b = a
    a = a + 1
    print(a)
    print(b)

    l1 = [1, 2, 3]
    l2 = l1
    l1.append(4)
    print(l1)
    print(l2)

def reference1():
    i = 1
    my_func1(i)
    print(i)

    j = 1
    j = my_func2(j)
    print(j)

    l11 = [1, 2, 3]
    my_func3(l11)
    print(l11)


    l12 = [1, 2, 3]
    my_func4(l12)
    print(l12)


    l13 = [1, 2, 3]
    l13 = my_func5(l13)
    print(l13)

def my_func1(b):
	b = 2

def my_func2(b):
	b = 2
	return b

def my_func3(l2):
	l2.append(4)


def my_func4(l2):
	l2 = l2 + [4]

# 与my_func3相比, 更倾向于这种写法
def my_func5(l2):
	l2 = l2 + [4]
	return l2