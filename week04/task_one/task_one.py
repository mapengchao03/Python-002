import pandas as pd
import numpy as np


# 自定义的table1, table2, data为测试数据

# 定义table1
table1 = pd.DataFrame(
    {'id': [199, 299, 3999, 199, 299, 699, 699, 899, 9999, 10, 199],
     'order_id': [199, 399, 399, 499, 599, 699, 799, 799, 699, 599, 499],
     'column_name': ['A', 'B', 'B', 'C', 'D', 'E', 'E', 'F', 'G', 'H', 'I'],
     'age': [11, 12, 23, 33, 34, 15, 46, 66, 57, 78, 98],
     'feature1': [1, 1, 2, 3, 3, 1, 4, 6, 5, 7, 9],
     'feature2': ['low', 'medium', 'medium', 'high', 'low', 'high', 'low', 'medium', 'medium', 'high', 'low']
     }
)

# 定义table2
table2 = pd.DataFrame(
    {'id': [199, 299, 3999, 199, 299, 699, 9999, 10, 199],
     'order_id': [199, 299, 3999, 499, 799, 899, 9999, 1099, 119],
     'column_name':['A', 'A', 'B', 'F', 'E', 'F', 'G', 'H', 'N'],
     'pazham':['apple','orange','pine','pear', 'apple','orange','pine','pear', 'tea'],
     'kilo':['high','low','high','medium', 'high','low','high','medium', 'high'],
     'price':np.array([5,6,5,7,6,5,3,2,1])
     }
)

# 定义data
data = pd.DataFrame(
    {'id': [199, 299, 3999, 499, 599, 699, 799, 899, 999, 10, 199],
     'order_id': [199, 399, 399, 499, 599, 699, 799, 799, 699, 599, 499],
     'column_name': ['A', 'B', 'B', 'C', 'D', 'E', 'E', 'F', 'G', 'H', 'I'],
     'age': [11, 12, 23, 33, 30, 15, 46, 66, 57, 78, 98],
     'feature1': [1, 1, 2, 3, 3, 1, 4, 6, 5, 7, 9],
     'feature2': ['low', 'medium', 'medium', 'high', 'low', 'high', 'low', 'medium', 'medium', 'high', 'low']
     }
)


# 1. SELECT * FROM data;
print(data)


# 2. SELECT * FROM data LIMIT 10;
print(data[0:10])


# 3. SELECT id FROM data;  //id 是 data 表的特定一列
print(data['id'])


# 4. SELECT COUNT(id) FROM data;
print(data['id'].count())


# 5. SELECT * FROM data WHERE id<1000 AND age>30;
print(data[(data['id'] < 1000) & (data['age'] > 30)])


# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
print(table1.groupby('id')['order_id'].nunique())


# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
print(pd.merge(table1, table2, how='inner', on='id'))


# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
print(pd.concat([table1, table2]))


# 9. DELETE FROM table1 WHERE id=10;
print(data[data['id'] != 10])


# 10. ALTER TABLE table1 DROP COLUMN column_name;
print(data.drop('column_name', axis=1))

