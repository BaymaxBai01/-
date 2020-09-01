import pandas as  pd
import numpy as np
import matplotlib.pyplot as plt

# data = pd.Series(np.random.randn(1000),index=np.arange(1000))
# data = data.cumsum()

data = pd.DataFrame(np.random.randn(1000,4),
                    index=np.arange(1000),
                    columns=list("ABCD"))
data = data.cumsum()
# print (data.head(3)) #默认数据是5
# data.plot() #打印线
ax = data.plot.scatter(x='A',y='B',color='Blue',label='Class_1') #打印点
data.plot.scatter(x='A',y='C',color='Red',label='Class_2',ax=ax) #打印点
plt.show()