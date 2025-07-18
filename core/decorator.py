## 简单装饰器
def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper


@my_decorator
def greet():
    print('hello world')


greet()
print('-----------------')

##### 类装饰器
class Count:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print('num of calls is: {}'.format(self.num_calls))
        return self.func(*args, **kwargs)


@Count
def example():
    print("hello world")

example()
print('-----------------')

### 带参数的装饰器
def logging(level):
    def outwrapper(func):
        def wrapper(*args, **kwargs):
            print("[{0}]: enter {1}()".format(level, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return outwrapper

@logging(level="INFO")
def hello(a, b, c):
    print(a, b, c)

hello("hello,","good","morning")

### 等价
logging(level="INFO")(hello)("hello,","good","morning")
print('-----------------')