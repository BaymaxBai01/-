import numpy as np

A = np.arange(12).reshape((3,4))
print (A)
print (np.split(A,2,axis=1)) #纵向均等分割
print (np.split(A,3,axis=0)) #横向均等分割
print (np.array_split(A,3,axis=1)) #纵向不等分割

# 关联赋值，a值改变，全部改变
a = np.arange(4)
print (a)
b=a
c=a
d=b
a[0] = 11
print (b)
print (d)

# 非关联赋值
e = a.copy()
a[3] = 33
print (a)
print (e)