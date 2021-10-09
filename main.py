# %%
import numpy as np

data = np.arange(5000).reshape(100,50)
data
# %%
import pandas as pd
# %%

columnName = ['column_'+str(i) for i in range(50) ]
columnName
# %%

dataSample = pd.DataFrame(data)
dataSample.head()
# %%
type(dataSample)
# %%
type(dataSample[0])
# %%
dataSample = pd.DataFrame(data, columns=columnName)
dataSample.head()
# %%
dict1 = {'name1':'XYZ1', 'name2':'XYZ2'}
dict1
dict2 = {'score1':15, 'score2':30}
dict2

pd.DataFrame(data=(dict1, dict2))
# %%
dict1 = {'name1':list(range(10)), 'name2':list(range(10,20))}
pd.DataFrame(data=(dict1))
# %%
data = pd.read_csv('abc.txt')