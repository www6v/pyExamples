
## args
def my_sum_function(*args):
    print(sum(args))


def argFunc():
    my_sum_function(1)
    my_sum_function(1, 2)
    my_sum_function(1, 2, 3)

## kwargs
def self_defined_function(*args, **kwargs):
    if "denominator" not in kwargs:
        print(sum(args))
    else:
        # 注意：kwargs的类型是字典
        denominator = kwargs["denominator"]
        print(sum(args) / denominator)


def self_defined_function1(*args, **kwargs):
    denominator = kwargs.get("denominator", 1) ## 默认值是1
    print(sum(args) / denominator)

def kwargs():
    # 没有denominator时，打印几个数的和
    self_defined_function(1, 2, 3)
    # 有denominator时，先求几个数的和，再除以denominator
    self_defined_function(1, 2, 3, denominator=3)

    self_defined_function1(1, 2, 3)
    self_defined_function1(1, 2, 3, denominator=3)
