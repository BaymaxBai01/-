import numpy as np
import pandas as pd

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan

print (df.dropna(axis=0,how='any')) #删除nan行
print (df.dropna(axis=1,how='any')) #删除nan列
print (df.dropna(axis=0,how='all')) #不删除行
print (df.fillna(value=0)) #nan替换为0
print (df.isnull()) #返回是否缺失数据
print (np.any(df.isnull()) == True) #至少有一个nan，则返回True
