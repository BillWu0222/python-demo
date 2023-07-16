import numpy as np
# 1. 將 list 轉成 numpy.ndarray，就可以使用 numpy 提供的各種功能
a = np.array([1, 2, 3])
print(type(a))
print(a.shape)

b = np.array([[1,2,3]])
print(type(b))
print(b.shape)

c = np.array([[1,2,3,98],[4,5,6,7],[9,10,11,45]])
print(type(c))
print(c.shape)

d = np.array([[[1,2,3],[4,5,6]]])
print(type(d))
print(d.shape)