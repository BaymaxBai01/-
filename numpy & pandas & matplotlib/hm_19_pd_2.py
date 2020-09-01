import numpy as np
import pandas as pd

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

print (df['A'])
print (df.A)
print (df[0:3])
print (df['20130102':'20130104'])
print (df['B'],df[0:2])
# 选择定向行列
print (df.loc['20130102'])
print (df.loc[:,['B']])
print (df.loc['20130102',['B']])
# 按照位置索引
print (df.iloc[3,1])
print (df.iloc[3:5,1:3])
print (df.iloc[[1,3,5],1:3])
# 混合方式索引 *
# print (df.ix[:2,['A','C']])
# 条件索引
print (df[df.A<8])