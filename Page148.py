import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager


file_path = '/Users/peterpan/Desktop/DataAnalysis-master/911.csv'

df = pd.read_csv(file_path)

df['timeStamp'] = pd.to_datetime(df['timeStamp'])
df.set_index('timeStamp',inplace = True)
print(df)


#统计出911数据中不同月份电话次数的变化情况

count_by_month = df.resample('M').count()['title']
print(count_by_month)

#画图

_x = count_by_month.index
_y = count_by_month.values


_x = [ i.strftime('%Y-%m-%d') for i in _x ]

plt.figure(figsize=(20,8),dpi=80)
plt.plot(range(len(_x)),_y)
plt.xticks(range(len(_x)),_x,rotation = 45)

plt.show()