import numpy as np
import pandas as pd

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

df.iloc[2,2] = 111
df.loc['20130101','B'] = 222
# df[df.A>4] = 0 #整个A>4的整列都更改
# df.A[df.A>4] = 0 #仅对A列A>4的数字都更改为0
df.B[df.A>4] = 0 #仅对B列A>4的数字都更改为0
df['F'] = np.nan #增加F列，值全部为nan
df['E'] = pd.Series([1,2,3,4,5,6],index=dates) #新插入的列，如果要融合到原有表格中，需要有相同的index

print (df)