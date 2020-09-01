import pandas as pd
import numpy as np

# df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
# df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
# df3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
#
# print (df1,df2,df3)
#
# # res = pd.concat([df1,df2,df3],axis=0) #上下合并，但是并不改变索引
#
# # print (res)
#
# res = pd.concat([df1,df2,df3],axis=0,ignore_index=True) #上下合并，并且改变索引
#
# print (res)

# df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index = [1,2,3])
# df2 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index = [2,3,4])
#
# res = pd.concat([df1,df2],join='outer')
# print (res)
#
# res1 = pd.concat([df1,df2],join='inner',ignore_index=True)
# print (res1)
#
# res2 = pd.concat([df1,df2],axis=1,join_axes=[df1.index]) #左连接
# print (res2)
#
# res3 = pd.concat([df1,df2],axis=1) #全连接
# print (res3)

df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
# df3 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index = [2,3,4])

res = df1.append(df2,ignore_index=True)
print (res)

s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
res1 = df1.append(s1,ignore_index=True)

print (res1)