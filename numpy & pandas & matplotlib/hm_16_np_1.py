import numpy as np

array = np.array([[1,2,3],
                  [2,3,4]])

print (array)
print ('number of dim:',array.ndim)
print ('shape:',array.shape)
print ('size:',array.size)

a = np.array([2,23,4],dtype = np.int64)
print (a.dtype)

b = np.array([[2,23],[2,32]])
print (b)

c = np.zeros((3,4))
print (c)

d = np.ones((3,4),dtype = np.int64)
print (d)

e = np.arange(12).reshape((3,4))
print (e)

f = e**2
print (f)

g = 10*np.sin(f)
print (g)

print (f<100)

# 矩阵乘法
h = np.dot(b,b)
print (h)

# 返回一个0~1之间得随机数，形状为2行*4列的矩阵
# i = np.random.random((2,4))
# 返回一个样本，具有标准正态分布。
# i = np.random.randn()
# 返回随机的整数，位于半开区间 [low, high)。
i = np.random.randint(9,15,size=(2,4))
print (i)
# print (np.sum(i,axis = 1)) #对每一行求和
# print (np.max(i,axis = 0)) #对每一列找最大值
# print (np.min(i))

A = np.arange(2,14).reshape((3,4))
print (A)
print (np.argmin(A)) #最小值索引
print (np.argmax(A)) #最大值索引
print (np.mean(A)) #平均值
print (np.median(A)) #中位数
print (np.cumsum(A)) #逐步累加
print (np.diff(A)) #累差
print (np.nonzero(A)) #非0值的位置
print (np.sort(A)) #矩阵排序
print (np.transpose(A)) #矩阵的转置
print (A.T) #同上
print ((A.T).dot(A)) #A的转置与A的矩阵乘法
print (np.clip(A,5,9)) #保留A中大于5小于9的数，小于5的值转为5，大于9的值转为9
print (np.mean(A,axis=1)) #对每一行求平均值

# 索引
B = np.arange(3,15).reshape(3,4)
print (B)
print (B[1][1])
print (B[2,1])
print (B[:,1]) #第一列的所有数
print (B[1,2:4]) #第一行第2位到第3位的数

# 通过循环来打印行
for row in B:
    print (row)
# 通过循环来打印（转置）列
for column in B.T:
    print (column)
# 打印每一个项目
for item in B.flat:
    print (item)
# 将矩阵转为一行
print (B.flatten())

# 矩阵的合并
C = np.array([1,1,1])
D = np.array([2,2,2])
E = np.vstack((C,D)) #上下合并
print (E)
print (E.shape,C.shape) #打印E和C的形状
F = np.hstack((C,D)) #左右合并
print (F)
print (F.shape,C.shape)
G = C [np.newaxis,:] #在行上增加一个维度
print (G)
print (G.shape)
H = C [:,np.newaxis] #在列上增加一个维度
print (H)
print (H.shape)
I = np.hstack((C[:,np.newaxis],D[:,np.newaxis])) #左右合并
print (I)
print (I.shape)
# 多个array进行合并
J = np.concatenate((C[:,np.newaxis],D[:,np.newaxis],D[:,np.newaxis],C[:,np.newaxis]),axis=0) #纵向合并
print (J)
print (J.shape)
K = np.concatenate((C[:,np.newaxis],D[:,np.newaxis],D[:,np.newaxis],C[:,np.newaxis]),axis=1) #横向合并
print (K)
print (K.shape)
