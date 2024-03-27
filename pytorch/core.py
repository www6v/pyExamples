import numpy as np
import torch

print("--------")
### 基本类型
x=torch.tensor([1,2,3])
print(x)
print(x.dtype)
x=torch.tensor([1,2,3]).to(torch.float16)
print(x.dtype)
x=torch.tensor([1,2,3]).to(torch.float32)
print(x.dtype)


print("--------")
### 存储方式
x=torch.tensor([[1,2,3],[4,5,6]])
print(x)
print(x.storage)


print("--------")
### 张量 +
x=torch.tensor([1,2,3])
y=torch.tensor([4,5,6])
z=x+y
print(z)
# print(x)
# x=x.to("cuda");
# x=x.to("cuda:0");
x=x.to("cpu");
z=x+y
print(z)


print("--------")
### 和numpy的相互转换 [指向同一个内存地址]
arr=np.zeros(3)
tensor=torch.from_numpy(arr)
print("before add 1:")
print(arr)
print(tensor)

print("\nafter add 1:")
np.add(arr,1,out=arr)
print(arr)
print(tensor)


print("--------")
### clone(), 中断这种关联
tensor = torch.zeros(3)
arr=tensor.clone().numpy()
print("before add 1:")
print(tensor)
print(arr)

print("\nafter add 1:")
tensor.add_(1)
print(tensor)
print(arr)


### 张量的stripe
a=torch.tensor([[1,2,3],
                [4,5,6]])
b=torch.tensor([[1,2],
                [3,4],
                [5,6]])
print('a:', a)
print('stride of a:', a.stride())
print('b:', b)
print('stride of b:', b.stride())


### 神经网络里面的参数初始化
x=torch.randn(3,4)
print('标准正态分布x：', x)

x=torch.randn(3,4)
print('均匀分布x：', x)
      


      
      
