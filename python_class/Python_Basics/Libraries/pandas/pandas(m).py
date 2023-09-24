"Series = 1-D data"
"Dataframe = 2-D data"
"Panel = 3-D data"
"............................................................................................"
import base64
import pandas as pd
import numpy as np
"............................................................................................"
# s = pd.Series([])
# print(s)
"............................................................................................"
# a = np.array(['Apple','Orange','Carrot','Doctor'])
# b = pd.Series(a) 
# print(b)
"............................................................................................"
# a = np.array(['Apple','Orange','Carrot','Doctor'])
# b = pd.Series(a,index=[5,6,7,8])  # To change index
# print(b)
"............................................................................................"
"Series in a dictionary"
# a = {'a':0,'b':1,'c':2}
# b = pd.Series(a)
# print(b)
"If we change the indexes it will create new columns of data"
"if indices exceeds data the index cover with NaN(not a number value)"
# a = {'a':0,'b':1,'c':2}
# b = pd.Series(a,index=['a','b','c','d'])
# print(b)
"............................................................................................"
"To insert scalar value"
# a = pd.Series(5,index=[1, 2, 3, 4, 5]) # The five will assign to every coloumns
# print(a)
"............................................................................................"
"Slicing a series"
# a = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
# print(a)
# print()
# print(a[0])                # Calling values by index
# print(a[-1])               
# print(a[-3:])
# print(a[3:])
# print(a[:3])
# print(a['a'])              # Calling values by Label
# print(a['b'])                  
# print(a[['b','d','e']])    # If you want to pass multiple label pass it as a sequence
"............................................................................................"
# a = pd.Series([i for i in range(0,21)])
# print("Axes =",a.axes) # To see axes of the series
# print()
# print("isEmpty =",a.empty) # To check the series is empty or not
# print()
# print("Dimentions =",a.ndim) # To check dimention
# print()
# print("All values =",a.values)  # To get all the values
"............................................................................................"
# a = pd.Series([i for i in range(0,21)])
# print(a.head(5)) # This will return the first 5 values
# print(a.tail(5)) # This will return the last 5 values
"............................................................................................"
# age = {'a':20,'b':23,'c':21,'d':18,'e':44,'f':32}
# a = pd.Series(age)
# print("Age of fifth person is",a[4])
# print("Dimention is",a.ndim)
"............................................................................................"

"DataFrames"
"............................................................................................"
# df = pd.DataFrame() 
# print(df)
"............................................................................................"
"Print a 1-D array"
# a = np.array(['a','b','c','d','e','f'])
# df = pd.DataFrame(a) 
# print(df)
"............................................................................................"
"Print a 2-D array"
# a = np.array([['A','Alpha'],['B','Bravo'],['C','Charlie'],['D','Delta']])
# print(pd.DataFrame(a,columns=['Letter','Codename'])) # (columns is used) To change the name of the column 
"............................................................................................"
# a = [['A',22],['B',33],['C',44],['D',55]]
# print(pd.DataFrame(a,columns=['Letter','Codename'],dtype='float64')) # dtype used to mention the type
"............................................................................................"
"Another way to print DataFrame"
# print(pd.DataFrame({'Name':['A','B','C','D'],'Value':[1,2,3,4]}))
"............................................................................................"
# a = [['A',22],['B',33],['C',44],['D',55]]
# print(pd.DataFrame(a,columns=['Letter','Codename'],index=['a1','b2','c3','d4'])) # To mention indices
"............................................................................................"
# data = [{'a':1,'b':2},{'a':5,'b':8,'c':10}]
# df = pd.DataFrame(data)
# print(df)
"............................................................................................"
# data = [{'a':1,'b':2},{'a':5,'b':8,'c':10}]
# df = pd.DataFrame(data,index=['first','second'])
# print(df)
"............................................................................................"
# import pandas as pd
# data = {'one':pd.Series([1,2,3],index=['a','b','c'],dtype="int64"),
#         'two':pd.Series([1,2,3,4],index=['a','b','c','d'],dtype="int64")
#        }
# df = pd.DataFrame(data)
# print(df)
# print()
# print(df['one'])
# print(type(df['one']))
# print()
# print(type(df[['one','two']]))
"............................................................................................"
# data = {'one':pd.Series([1,2,3],index=['a','b','c']),
#         'two':pd.Series([1,2,3,4],index=['a','b','c','d']),
#         'three':pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
#        }
# df = pd.DataFrame(data)
# print(df)
# print()
# print(df[df['one']>1])
# print(df[df['one']==3])
"............................................................................................"
# data = {'one':pd.Series([1,2,3],index=['a','b','c']),
#         'two':pd.Series([1,2,3,4],index=['a','b','c','d'])
#        }
# df = pd.DataFrame(data)
# # print(df)
# df['three']=pd.Series([10,20,30],index=['a','b','c'])
# # print(df)
# # print()
# df['four']=df['one']+df['three']
# # print(df)
# df['five']=df['one']+df['two']
# print(df)
# print()
# del df['one']
# print(df)
# print()
# df.pop('two')
# print(df)
"............................................................................................"
# data = {'one':pd.Series([1,2,3],index=['a','b','c']),
#         'two':pd.Series([1,2,3,4],index=['a','b','c','d'])
#        }
# df = pd.DataFrame(data)
# print(df)
# newdata = pd.Series(data = {'one':9,'two':8},name='e')
# df  = df.append(newdata,ignore_index=False)
# print(df)
# print()

# df = df.drop('a')
# print(df)
"............................................................................................"
"loc is used to fetch values by label"
# a = {"ONE":pd.Series([1,2,3,4,5,6],index=['A','B','C','D','E','F']),
#      "TWO":pd.Series([7,8,9,10,11,12],index=['A','B','C','D','E','F']),
#      "THREE":pd.Series([13,14,15,16,17,18],index=['A','B','C','D','E','F']),
#      "FOUR":pd.Series([19,20,21,22,23,24],index=['A','B','C','D','E','F']),
#      "FIVE":pd.Series([25,26,27,28,29,30],index=['A','B','C','D','E','F']),
#      "SIX":pd.Series([31,32,33,34,35,36],index=['A','B','C','D','E','F'])
#      }
# df = pd.DataFrame(a)
# print(df.loc['B'])
# print(df.loc['B','TWO'])
# print(df.loc['B':])
# print(df.loc['B':'E'])
# print(df.loc[['B','C','D'],'TWO'])
# print(df.loc[['B','C','D']])
# print(df.loc[['B','C','D'],['TWO','ONE']])
# print(df.loc['B':'C',['TWO']])
"............................................................................................"
"iloc is used to fetch row values"
# a = {"ONE":pd.Series([1,2,3,4,5,6],index=['A','B','C','D','E','F']),
#      "TWO":pd.Series([7,8,9,10,11,12],index=['A','B','C','D','E','F']),
#      "THREE":pd.Series([13,14,15,16,17,18],index=['A','B','C','D','E','F']),
#      "FOUR":pd.Series([19,20,21,22,23,24],index=['A','B','C','D','E','F']),
#      "FIVE":pd.Series([25,26,27,28,29,30],index=['A','B','C','D','E','F']),
#      "SIX":pd.Series([31,32,33,34,35,36],index=['A','B','C','D','E','F'])
#      }
# df = pd.DataFrame(a)
# print(df.iloc[0])
# print(df.iloc[[0,3]])
# print(df.iloc[3:6])
# print(df.iloc[1:4:2])
# print(df.iloc[::])
"............................................................................................"
# data = {'one':pd.Series([1,2,3],index=['a','b','c']),
#         'two':pd.Series([1,2,3,4],index=['a','b','c','d'])
#        }
# df = pd.DataFrame(data)
# print(df)
# newdata = pd.Series(data = {'one':9,'two':8},name='e')
# df  = df.append(newdata,ignore_index=False)
# print(df)
# print()
"............................................................................................"
"In-built Functions"
# data = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
#         'Age':pd.Series([25,26,25,30,32,21,31]),
#         'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])
#         }
# df = pd.DataFrame(data)
# print(df)
# print(df.T) # To convert to transpose 
# print(df.dtypes) # To get datatype details
# print(df.axes) # To get details of the dataframe
# print(df.empty) # To check weather the data frame is empty or not
# print(df.size) # To get Size of the dataframe
# print(df.columns) # To Get column info
# print(df.values) # it will print the dataframe as an array
# print(df.head(2)) # It will print the first two values
# print(df.tail(2)) # It will print the last two values
"............................................................................................"
# data = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
#         'Age':pd.Series([25,26,25,30,32,21,31,34,43,23,33,56]),
#         'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,4.3,4.2,5.3,1.2,3.9])
#         }
# df = pd.DataFrame(data)
# print(df.count()) # To get the count
# print(df.sum()) # To get sum
# print(df.mean()) # To get mean
# print(df.median())# To get median
# print(df.std()) # To get std
# print(df.min()) # To get min
# print(df.max()) # To get max
# print(df.describe()) # It will print all the essential details like (mean,std,min,25%,50%,75%,max )
"............................................................................................"
# def a(e,n):
#     return e + n
# df1 = [[1,2],[3,4],[5,6],[7,8],[9,10]]
# df = pd.DataFrame(df1,index=['a','b','c','d','e'],columns=['c1','c2'])
# print(df)
# print(df.pipe(a,3))  
"Pipe will do the operation mentioned in the function and apply it to all the elements contains in the dataframe"
"............................................................................................"
# df1 = [[1,2],[3,4],[5,6],[7,8],[9,10]]
# df = pd.DataFrame(df1,index=['a','b','c','d','e'],columns=['c1','c2'])
# print(df)
# print()
# print(df.apply(np.mean)) # It will print mean value of columns
# print(df.apply(np.max))  # It will print max value of columns
# print(df.apply(np.mean,axis=1)) # It will print mean value of rows
# print(df.apply(np.max,axis=1))  # It will print max value of rows
# print(df.applymap(lambda x : x * 100)) # It will apply a function to the dataframe
# print(df.applymap(lambda x : x / 2 * 100))
"............................................................................................"
"Label sorting"
# df = pd.DataFrame(np.random.rand(10,2),index=[1,4,6,2,3,5,9,8,0,7])
# Sorted = df.sort_index() # Ascending sort
# print(Sorted) 

# df = pd.DataFrame(np.random.rand(10,2),index=[1,4,6,2,3,5,9,8,0,7])
# Sorted = df.sort_index(ascending=False) # Decending sort
# print(Sorted)
"............................................................................................"
"Column sort"
# df = pd.DataFrame(np.random.rand(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns=['a','b'])
# Sorted = df.sort_values(by='a')
# print(Sorted) 
"............................................................................................"
# df = pd.DataFrame(np.random.rand(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns=['a','b'])
# Sorted = df.sort_values(by='a')
# print(Sorted) 
# "By using 'kind' you can multi-sort (quicksort, heapsort, mergesort)"
# print()
# print("Merge-Sort -->")
# Sorted = df.sort_values(by='a',kind="mergesort")
# print(Sorted) 
# print()
# print("Heap-Sort -->")
# Sorted = df.sort_values(by='a',kind="heapsort")
# print(Sorted) 
# print()
# print("Quick-Sort -->")
# Sorted = df.sort_values(by='a',kind="quicksort")
# print(Sorted) 
"............................................................................................"
# df = pd.DataFrame(np.random.rand(5,3),index=['a','c','e','f','g'],columns=['C1','C2','C3'])
# df = df.reindex(['a','b','c','d','e','f','g','h','i']) # This will reindex the dataframe
# print(df)
# print()
# print(df['C1'].isnull()) # To check the column value contains a NaN value
# print(df['C1'].notnull()) # To check the column value not contains a NaN value
# print(df.fillna(0)) # it will fill NaN values with 0
# print(df.fillna(method='pad')) # it will forward fill NaN values
# print(df.fillna(method='bfill')) # it will backward fill NaN values
# print(df.dropna()) # To remove all NaN values
"............................................................................................"
# d = {"Name":["A","B",'a','C','D','a','D'],"Age":[21,22,33,21,180,20,180]}
# df = pd.DataFrame(d)
# print(df)
# print()
# print(df.replace({'a':'A',180:18}))  # It will replace values
"............................................................................................"
"If the both columns contains same values it will replace from both columns"
# d = {"Number":[10,12,13,14,15,16],"Number2":[10,17,18,19,20,21]}
# df = pd.DataFrame(d)
# print(df)
# print(df.replace({10:20}))  # It will replace values
"............................................................................................"
"To replace only in one column"
# d = {"Number":[10,12,13,14,15,16],"Number2":[10,17,18,19,20,21]}
# df = pd.DataFrame(d)
# print(df)
# df['Number'] = df['Number'].replace({10:80})
# print(df)
"............................................................................................"
"Group-By - To group values according to data"
# d = {"Team":['Riders','Riders','Devils','Devils','Kings','Kings','Kings','Kings','Riders',
#              'Royals','Royals','Riders'],
#              "Rank":[1,2,2,3,3,4,1,1,2,4,1,2],
#              'Year':[2014,2015,2014,2015,2014,2015,2016,2016,2016,2014,2015,2017],
#              'Points':[725,826,825,930,732,621,731,534,473,823,933,856]
#              }
# df = pd.DataFrame(d)
# grouped = df.groupby('Rank')
# for i, j in grouped:
#     print('Name = ',i)
#     print('Group (by Rank)--> \n',j)
"............................................................................................"
"Merge Data"
# data1 = pd.DataFrame({
#     "ID":[1,2,3,4,5],
#     "Name":['Alex','Amy','Allen','Alice','Aion'],
#     "Subject_id":['sub1','sub2','sub3','sub4','sub5']
# })
# data2 = pd.DataFrame({
#     "ID":[1,2,3,4,5],
#     "Name":['Alex','Amy','Allen','Alice','Aion'],
#     "Subject_id":['sub2','sub5','sub3','sub4','sub6']
# })
# # a = pd.merge(data1,data2,on='ID')
# # print(a)
# a = pd.merge(data1,data2,on='Subject_id')  # If datas are same it will only take the common datas
# print(a)
"............................................................................................"
"Dataframe Joining"
# left = pd.DataFrame({
#     'id':[1,2,3,4,5],
#     'Name':['alex','amy','allen','alice','aion'],
#     'subject_id':['sub1','sub2','sub3','sub4','sub5']})

# right = pd.DataFrame({
#     'id':[1,2,3,4,5],
#     'Name':['billy','brain','bran','bryce','betty'],
#     'subject_id':['sub2','sub4','sub3','sub6','sub5']})
# print(left)
# print()
# print(right)
# print()

# print("Left Joining -->") 
# print(pd.merge(left,right,on='subject_id',how='left'))
# print()
# print("Right Joining -->")
# print(pd.merge(left,right,on='subject_id',how='right'))
# print()
# print("Inner Joining -->")
# print(pd.merge(left,right,on='subject_id',how='inner'))
# print()
# print("Outer Joining -->")
# print(pd.merge(left,right,on='subject_id',how='outer'))
# print()
"............................................................................................"
# one = pd.DataFrame({
#     'id':[1,2,3,4,5],
#     'Name':['alex','amy','allen','alice','aion'],
#     'subject_id':['sub1','sub2','sub3','sub4','sub5'],
#     'marks_scored':[84,87,88,78,97]},
#     index=[1,2,3,4,5])

# two = pd.DataFrame({
#     'id':[1,2,3,4,5],
#     'Name':['billy','brain','bran','bryce','betty'],
#     'subject_id':['sub2','sub4','sub3','sub6','sub5'],
#     'marks_scored':[82,85,81,71,91]},
#         index=[1,2,3,4,5])

# print(one)
# print()
# print(two)
# print()

# print(pd.concat([one,two],ignore_index=True))
"............................................................................................"
# df = pd.DataFrame({"Animal":['Falcon','Falcon','Parrot','Parrot'],
#                   "Maxspeed":[380,370,24,26]})
# a = df.groupby(['Animal']).sum()
# print(a)
"............................................................................................"
# df=pd.read_csv("http://bit.ly/drinksbycountry")
# print(df)
# print()
# print(df.groupby(['continent']).mean())
# print(df.beer_servings.agg(['sum','min','max']))
# s=df.groupby(df['continent']).beer_servings.agg(['sum','min','max','count','mean'])
# print(s)
"............................................................................................"
"download this dataset --> https://www.kaggle.com/datasets/saurabh00007/iriscsv"
"............................................................................................"