import numpy as np
import pandas as pd

s = pd.Series([1,3,5,np.nan,4,1])
print (s)

dates = pd.date_range('20190101',periods=6)
print (dates)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print (df)

df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print (df1)

df2 = pd.DataFrame({'A':1.,
                    'B':pd.Timestamp('20130102'),
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D':np.array([3]*4,dtype='int32'),
                    'E':pd.Categorical(["test","train","test","train"]),
                    'F':'foo'})
print (df2)
print (df2.dtypes)
print (df2.index)
print (df2.columns)
print (df2.values)
print (df2.describe())
print (df2.T)
print (df2.sort_index(axis=1,ascending=False))
print (df2.sort_index(axis=0,ascending=False))
print (df2.sort_values(by='E',ascending=True))