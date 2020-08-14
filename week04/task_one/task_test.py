import pandas as pd
import numpy as np

# 定义df1
df1 = pd.DataFrame({'alpha':['A','B','B','C','D','E'],'feature1':[1,1,2,3,3,1],
            'feature2':['low','medium','medium','high','low','high']})

# 定义df2
df2 = pd.DataFrame({'alpha':['A','A','B','F'],'pazham':['apple','orange','pine','pear'],
            'kilo':['high','low','high','medium'],'price':np.array([5,6,5,7])})

# tt = df1.groupby('alpha')
# for name, group in tt:
#     print(group)

# print(pd.merge(df1, df2, how='inner', on='alpha'))

# print(pd.concat([df1, df2]))

tt = df1.groupby('alpha')['feature1'].nunique()
print(tt)
