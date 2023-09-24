"File = iris.csv"
"............................................................................................"
import pandas as pd
df = pd.read_csv("Iris.csv")

"Question 1 - select sepal length"
# print(df['SepalLengthCm'])

"Question 2 - select sepal and petal length"
# print(df[['SepalLengthCm','PetalLengthCm']])

"Question 3 - select all values with sepal length > 5cm"
# print(df[df['SepalLengthCm'] > 5.0])

"Question 4 - create a new column which is TotalpetalCm=PetalLengthCm+PetalWidthCm"
# df['TotalpetalCm'] = df['PetalLengthCm'] + df['PetalWidthCm']
# print(df)

"Question 5 - Delete column TotalPetalCm from dataset"
# del(df['TotalpetalCm'])
# print(df)

"Question 6 - Access the dataframe using iloc the first 10 records"
# print(df.iloc[0:10])

"Question 7 - delete the first row from the dataframe"
# df.drop(index=df.index[0], inplace=True, axis=0)
# print(df)

"Question 8 - delete the first 10 rows from the dataframe"
# df.drop(index=df.index[0:10], inplace=True, axis=0)
# print(df)

"Question 9 - Reindex the dataframe"
# df = df.reindex([i for i in range(len(df))])
# df = df.reset_index()
# print(df)

"Question 10 - use the describe function"
# descr = df.describe()
# print(descr)

"Question 11 - find the sentos,verginaca and vericolor flowe describe them separately"
# main_group = df.groupby('Species')
# setosa_group = main_group.get_group('Iris-setosa')
# versicolor_group = main_group.get_group('Iris-versicolor')
# verginaca_group = main_group.get_group('Iris-virginica')
# print("Setosa -->")
# print(setosa_group.describe())
# print()
# print("Verginaca -->")
# print(verginaca_group.describe())
# print()
# print("Versicolor -->")
# print(versicolor_group.describe())
# print()

"Question 12 - sort the dataframe according to SepalLengthCm"
# Sorted = df.sort_values(by='SepalLengthCm')
# print(Sorted) 

"Question 13 - Rename the PetalLengthCm column as PL(Cm),SepalwidthCm as AW(Cm) and PetalWidthCm as PW(Cm) rename SepalLengthCm as SP(Cm)"
# df = df.rename(columns={'PetalLengthCm':'PL(Cm)','SepalWidthCm':'AW(Cm)','PetalWidthCm':'PW(Cm)','SepalLengthCm':'SP(Cm)'})
# print(df)

"Question 14 - Find and print count of each kind of flower print the count as integer value"
# main_group = df.groupby('Species')
# print(main_group['Id'].count())

"Question 15 - Find the data of flower 'iris-virginiva' tupe where petal-length>1.5"
# main_group = df.groupby(['Species'])
# grouped = main_group.get_group('Iris-virginica')
# print(grouped[grouped['PetalLengthCm'] > 1.5])