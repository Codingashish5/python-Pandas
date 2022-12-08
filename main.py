# Pandas
# Pandas is an open-source library that is built on top of NumPy library. It is a Python package that offers various data structures and operations for manipulating numerical data and time series. It is mainly popular for importing and analyzing data much easier. Pandas is fast and it has high-performance & productivity for users.
# Fast and efficient for manipulating and analyzing data.
# Data from different file objects can be loaded.
# Easy handling of missing data (represented as NaN) in floating point as well as non-floating point data
# Size mutability: columns can be inserted and deleted from DataFrame and higher dimensional objects
# Data set merging and joining.
# Flexible reshaping and pivoting of data sets
# Provides time-series functionality.
# Powerful group by functionality for performing split-apply-combine operations on data sets
import pandas as pd
import numpy as np
import re
# ser = pd.Series(dtype='float')
# print()
# data = np.array(['g', 'e', 'e', 'k', 's'])
#
# ser = pd.Series(data)
# print(ser)
# print("")
#
#
# df=pd.DataFrame()
# print(df)
# lst=['ashish','mundra']
# df=pd.DataFrame(lst)
# print(df)
#
# # Pandas DataFrame
# # Pandas DataFrame is two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns. Pandas DataFrame consists of three principal components, the data, rows, and columns.
# # Creating a Pandas DataFrame
# # Pandas DataFrame will be created by loading the datasets from existing storage, storage can be SQL Database, CSV file, and Excel file. Pandas DataFrame can be created from the lists, dictionary, and from a list of dictionary etc. Dataframe can be created in different ways here are some ways by which we create a dataframe:
# lst=['ashish','mundra','friend','address','house']
# df=pd.DataFrame(lst)
# print(df)
# print("")
#
# data = {'Name':['ashish','ajay','rohan','harshal'],
#       'Age':[20,19,29,20]}
# df = pd.DataFrame(data)
# print(df)
# print("")
#
#
#
# # Dealing with Rows and Columns7
# # A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns. We can perform basic operations on rows/columns like selecting, deleting, adding, and renaming.
# data={'Name':['jai','nick','anuj','ashish'],
#       'Age':[27,24,25,32],
#       'Address':['delhi','kanpur','jaipur','ajmer'],
#       'Qualification':['Msc','MA','MCA','phd']}
# df=pd.DataFrame(data)
# print(df[['Name','Qualification']])
# print("")
# # Create pandas dataframe from lists using dictionary:
# # Creating pandas data-frame from lists using dictionary can be achieved in different ways. We can create pandas dataframe from lists using dictionary using pandas.DataFrame. With this method in Pandas we can transform a dictionary of list to a dataframe.
# dicit={'name':["pankaj","ashish","ravi","rohan"],
#        'degree':["MBA","BCA","M.TECT","MCA"],
#        'score':[90,40,50,60]}
# df=pd.DataFrame(dicit)
# print(df)
# print("")

# data = pd.read_csv("nba.csv", index_col="Name")
#
# # retrieving row by loc method
# first = data.loc["Avery Bradley"]
# second = data.loc["R.J. Hunter"]
#
# print(first, "\n\n\n", second)
# print("")

#
# dict = {'First score':[100,90,np.nan,95],
#       'Second Score':[30,45,56,np.nan],
#       'third score':[np.nan,40,80,98]}
# df = pd.DataFrame(dict)
#
# print(df.isnull())
#
# dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
#         'degree': ["MBA", "BCA", "M.Tech", "MBA"],
#         'score':[90, 40, 80, 98]}
# df = pd.DataFrame(dict)
# for i, j in df.iterrows():
#     print(i, j)
#     print()

# df = pd.read_csv("nba.csv")
#
# ser = pd.Series(df['Name'])
# data = ser.head(10)
# data
# data=pd.Series([5,2,3,7],index=['a','b','c','d'])
# data1=pd.Series([1,6,4,9],index=['a','b','c','d'])
# print(data,"\n\n",data1)
# print("")
#
# list=['a','s','h','i','s','h']
# ser=pd.Series(list)
# print(ser)
# print("")
#
# data = np.array(['g', 'e', 'e', 'k', 's'])
#
# # providing an index
# ser = pd.Series(data, index=[10, 11, 12, 13, 14])
# print(ser)
# print("")
#
#
# list=['a','s','h','i','s','h']
# ser = pd.Series(list)
# print(ser)
# # Creating a series from Scalar value:
# ser = pd.Series(10,index=[0,1,2,3,4,5])
# print(ser)
# print("")
# # Creating a series using NumPy functions
# ser1 = pd.Series(np.linspace(3,33,3))
# print(ser1)
# ser2 = pd.Series(np.linspace(1,100,10))
# print("'& quot\n"         ,ser2)
# print("")
#
# ser = pd.Series(range(20))
# print(ser)
# print("")
#
# ser=pd.Series(range(1,20,3), index=[x for x in 'abcdefg'])
# print(ser)
#
# ser=np.arange(10,15)
# serobj=pd.Series(data=ser*5,index=ser)
# print(serobj)
# print("")
# # Python | Pandas Dataframe/Series.head() method
# data = pd.read_csv("nba.csv")
# data_top=data.head()
# print(data_top)
# print("")
#
# data = pd.read_csv("nba.csv")
# n=10
# series=data["Name"]
# top=series.head(n = n)
# print(top)
# print("")
#
# # Python | Pandas Dataframe.describe() method
# # Python is a great language for doing data analysis, primarily because of the fantastic ecosystem of data-centric Python packages. Pandas is one of those packages and makes importing and analyzing data much easier.
#
# # Pandas describe() is used to view some basic statistical details like percentile, mean, std etc. of a data frame or a series of numeric values. When this method is applied to a series of string, it returns a different output which is shown in the examples below.
# data=pd.read_csv("nba.csv")
# data.dropna(inplace=True)
# perc=[.20,.40,.60,.80]
# include=['object','float','int']
# desc=data.describe(percentiles=perc,include=include)
# print(desc)
# print("")
# print("Example2")
# data=pd.read_csv("nba.csv")
# data.dropna(inplace=True)
# desc=data["Name"].describe()
# print(desc)
# print("")
#
#
# # Dealing with Rows and Columns in Pandas DataFrame
# data={'NAME':['jai','princi','gaurav','anuj'],
#       'height':[5.1,5.2,5.3,5.4],
#         'Qualification': ['Msc', 'MA', 'Msc', 'Msc'],
#        'Age':[27, 24, 22, 32]}
# df=pd.DataFrame(data)
# address=['delhi','bangalore','chennai','patna']
# df['address']=address
# print(df)
# print("")
#
# # Dealing with Rows:
# data = pd.read_csv("nba.csv", index_col="Name")
#
# # retrieving row by loc method
# first = data.loc["Avery Bradley"]
# second = data.loc["R.J. Hunter"]
#
# print(first, "\n\n\n", second)
# print("")
# print("Example 2")
# df = pd.read_csv("nba.csv", index_col="Name")
#
# df.head(10)
#
# new_row = pd.DataFrame({'Name': 'Geeks', 'Team': 'Boston', 'Number': 3,
#                         'Position': 'PG', 'Age': 33, 'Height': '6-2',
#                         'Weight': 189, 'College': 'MIT', 'Salary': 99999},
#                        index=[0])
# # simply concatenate both dataframes
# df = pd.concat([new_row, df]).reset_index(drop=True)
# df.head(5)

# # Dealing with Rows and Columns in Pandas DataFrame
# # making data frame from csv file
# data = pd.read_csv("nba.csv", index_col="Name")
#
# # dropping passed columns
# data.drop(["Team", "Weight"], axis=1, inplace=True)
#
# # display
# print(data)
# print("")

# Python | Extracting rows using Pandas .iloc[]
# Python is a great language for doing data analysis, primarily because of the fantastic ecosystem of data-centric Python packages. Pandas is one of those packages that makes importing and analyzing data much easier.
# data=pd.read_csv("nba.csv")
# row1=data.loc[3]
# row2=data.iloc[3]
# print(row1==row2)
# print("")
# print("example 2")
# data=pd.read_csv("nba.csv")
# row1=data.iloc[[4,5,6,7]]
# row2=data.iloc[4:8]
# print(row1==row2)
# print("")

# Indexing and Selecting Data with Pandas
# Indexing in pandas means simply selecting particular rows and columns of data from a DataFrame. Indexing could mean selecting all the rows and some of the columns, some of the rows and all of the columns, or some of each of the rows and columns. Indexing can also be known as Subset Selection.
# data = pd.read_csv("nba.csv",  index_col="Name")
# first = data["Age"]
# print(first)
# print("")
#
#
# data = pd.read_csv("nba.csv",  index_col="Name")
# first = data[["Age","College","Salary"]]
# print(first)
# print("")
# # Indexing a DataFrame using .loc[ ] :
# # Selecting a single row
# data = pd.read_csv("nba.csv", index_col ="Name")
# first = data.loc["Avery Bradley"]
# second = data.loc["R.J. Hunter"]
#
# print(first, "\n\n\n", second)
# print("")
# # Selecting multiple rows
# data = pd.read_csv("nba.csv", index_col="Name")
#
# # retrieving multiple rows by loc method
# first = data.loc[["Avery Bradley", "R.J. Hunter"]]
#
# print(first)
# print("")
#
# # data = pd.read_csv("nba.csv", index_col="Name")
# data = pd.read_csv("nba.csv", index_col="Name")
#
#
# first = data.loc[["Avery Bradley", "R.J. Hunter"],
#                    ["Team", "Number", "Position"]]
# print(first)

# Selecting all the rows and a some columns
# data = pd.read_csv("nba.csv", index_col ="Name")
#
# row2 = data.iloc[:, [1, 2]]
#
# print(row2)

# Selecting multiple rows
# data = pd.read_csv("nba.csv", index_col ="Name")
#
#
# row2 = data.iloc [[3, 5, 7]]
# print(row2)


# Boolean Indexing in Pandas
# In boolean indexing, we will select subsets of data based on the actual values of the data in the DataFrame and not on their row/column labels or integer locations. In boolean indexing, we use a boolean vector to filter the data
# Accessing a DataFrame with a boolean index:
# dict = {'name':["ashish", "ravi", "pankaj", "rohan"],
#         'degree':["MBA", "BCA", "MCA", "PHD"],
#         'score':[90, 70, 80, 60]}
#
#
# df = pd.DataFrame(dict, index=[True,False,True,False])
#
# print(df)
# print("")
# # Accessing a Dataframe with a boolean index using .loc[]
# dict={'name':["ashish", "ravi", "pankaj", "rahul"],
#       'degree':["MBA","BCA","MCA","MBA"],
#       'score':[50,60,70,40]}
# df=pd.DataFrame(dict,index=[True,False,True,False])
# # print(df.loc[True])
# print("")
# print(df.iloc[0])
#
# print(df.iloc[1])
# print(df.iloc[2])
# print(df.iloc[3])
#
# # Accessing a Dataframe with a boolean index using .ix[] remove from python
# # Applying a boolean mask to a dataframe : /
# df=pd.DataFrame(dict,index=[0,1,2,3])
# print(df[[True,False,True,False]])
# print("")
# # Masking data based on column value:
# df=pd.DataFrame(dict)
# print(
#     df['degree']=='BCA'
# )
# print("")
# data=pd.read_csv("nba.csv",index_col="Name")
# print(data['Age']>25)
# print("")
# # Masking data based on index value :
# df=pd.DataFrame(dict,index=[0,1,2,3])
# mask=df.index==0
# print(df[mask])
# print("")
#
# df=pd.read_csv("nba (1).csv")
# df=pd.DataFrame(data,index=[0,1,2,3,4,5,6,7,8,9,10,11,12])
# mask=df.index>7
# print(df[mask])
# print("")
#
# # Pandas GroupBy
# # Groupby is a pretty simple concept. We can create a grouping of categories and apply a function to the categories. It’s a simple concept but it’s an extremely valuable technique that’s widely used in data science. In real data science projects, you’ll be dealing with large amounts of data and trying things over and over, so for efficiency, we use Groupby concept. Groupby concept is really important because it’s ability to aggregate data efficiently, both in performance and the amount code is magnificent.
# # Splitting : It is a process in which we split data into group by applying some conditions on datasets.
# # Applying : It is a process in which we apply a function to each group independently
# # Combining : It is a process in which we combine different datasets after applying groupby and results into a data structure
# data1={'Name':['jai','anuj','jai','ashish','gaurav','rohan','rahul','abhi'],
#        'Age':[27,34,35,353,3,2,3,4],
#        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
#                    'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
#        'Qualification': ['Msc', 'MA', 'MCA', 'Phd',
#                          'B.Tech', 'B.com', 'Msc', 'MA']
#        }
# df=pd.DataFrame(data1)
# print(df)
# print("")
# gk=df.groupby('Name')
# gk.first()
# print("")
# # Grouping data by sorting keys :
# data1={'Name':['Jai','anuj','ashish','rahul','rohan','ravi','virkram','mohit'],
#        'Age':[34,54,6,6,78,8,9,9]}
# df=pd.DataFrame(data1)
# print(df)
# print("")
# df.groupby(['Name']).sum()
#
# grp = df.groupby(['Name'])
# for name,group in grp:
#     print(name)
#     print(group)
#     print()
# print("")

# grp=df.groupby('Name','Qualification')
# for name,group in grp:
#     print(name)
#     print(group)
#     print()
# print("")
# Selecting a groups

# grp = df.groupby('Name')
# ad = grp.get_group('Jai')
# print(ad)
# print("")
# grp=df.group(['Name','Age'])
# grp.get_group(('Jai', 34))

# Applying function to group
# data2={'Name':['ashish','ravi','jai','abhi'],
#        'Age':[24,24,56,67],
#        'Address':['nagapur','jaipur','kanpur','manipur'],
#        'Score': [23, 34, 35, 45]}
#
#
# df = pd.DataFrame(data2)
#
# print(df)
# print("")

# grp=df.groupby('Name')
#
# ad=grp['Age'].agg([np.sum,np.mean,np.std])
# print(ad)
#
# # Applying different functions to DataFrame columns :
#
# grp = df.groupby('Name')
#
#
# add=grp.agg({'Age' : 'sum','Score':'std'})
# print(add)
# print("")
# # Aggregation      :: It is a process in which we compute a summary statistic (or statistics) about each group. For Example, Compute group sums ormeans
# grp1= df.groupby('Name')
# add=grp1.aggregate(np.sum)
# print(add)
# print("")
# # Now we perform aggregation on agroup containing multiple keys
# grp2 = df.groupby(['Name', 'Score'])
#
# add2=grp2.aggregate(np.sum)
# print(add2)
#
#
#
# # Transformation : Transformation is a process in which we perform some group-specific computations and return a like-indexed. Transform method returns an object that is indexed the same (same size) as the one being grouped.
# grp=df.groupby('Name')
# sc= lambda x:(x-x.mean())/x.std()*10
# grp.transform(sc)


# Filtration : Filtration is a process in which we discard some groups, according to a group-wise computation that evaluates True or False. In order to filter a group, we use filter method and apply some condition by which we filter group.
# grp=df.groupby('Name')
# grp.filter(lambda x:len(x)>=2)
# print("")

# Python | Pandas Merging, Joining, and Concatenating
# Pandas DataFrame is two-dimensional size-mutable, potentially heterogeneous tabular data structure with labelled axes (rows and columns). A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns. We can join, merge, and concat dataframe using different methods. In Dataframe df.merge(),df.join(), and df.concat() methods help in joining, merging and concating different dataframe.
# Concatenating DataFrame using .concat()
#
# data1={'Name':['jai','ashish'],
#        'Age':[20,21],
#        'address':['jaipur','raipur'],
#        'Qualification':['MCA','MSC']
#        }
# data2={'Name':['ravi','rahul'],
#        'Age':[21,22],
#        'address':['ksg','ajmer'],
#        'Qualification':['BCA','BSC']
#        }
#
# df = pd.DataFrame(data1)

# s1 = pd.Series([1000, 2000], name='Salary')
#
# print(df, "\n\n", s1)

#
# df1 = pd.DataFrame(data2)
# print(df, "\n\n", df1)
# using a .concat() method
# frames = [df, df1]
#
# res1 = pd.concat(frames)
# print(res1)

# Concatenating DataFrame by setting logic on axes :
# res2 = pd.concat([df, df1], axis=1, join='inner')

# print(res2)Concatenating DataFrame by ignoring indexes :
# Now we are going to apply ignore_index as an argument.
    # res = pd.concat([df, df1], ignore_index=True)
    #
    # print(res)


# Concatenating DataFrame with group keys :

# frames=[df,df1]
# res=pd.concat(frames,keys=['x','y'])
# print(res)

# Now we are going to mix Series and dataframe together
# res = pd.concat([df, s1], axis=1)
#
# print(res)


# Merging DataFrame  :Pandas have options for high-performance in-memory merging and joining. When we need to combine very large DataFrames, joins serve as a powerful way to perform these operations swiftly. Joins can only be done on two DataFrames at a time, denoted as left and right tables. The key is the common column that the two DataFrames will be joined on.
# Merging a dataframe with one unique key combination

# res = pd.merge(df, df1, on='key')
#
# print(res)

# Merging dataframe using how in an argument:
#
# res = pd.merge(df, df1, how='left', on=['Name', 'Age'])
#
# print(res)
#
# # Now we set how = 'outer' in order to get union of keys from dataframes.
# res2 = pd.merge(df, df1, how='outer', on=['address', 'Qualification'])
#
# print(res2)

# Joining DataFrame :In order to join dataframe, we use .join() function this function is used for combining the columns of two potentially differently-indexed DataFrames into a single result DataFrame.
# data1 = {'Name':['Jai', 'Princi'],
#         'Age':[27, 24]}
# data2 = {'Address':[ 'Allahabad', 'Kannuaj'],
#         'Qualification':['MCA', 'Phd']}
# df=pd.DataFrame(data1,index=['K0','K1'])
#
#
# df1=pd.DataFrame(data2,index=['K0','K2'])
#
# print(df,"\n\n",df1)
#
# res=df.join(df1)
# print(res)
# Joining dataframe using on in an argument :
# df= pd.DataFrame(data1)
# df1=pd.DataFrame(data2,index=['k0','k2'])
# print(df,"\n\n",df1)
# res2=df.join(df1,on='key')
# print(res2)
# res1 = df.join(df1, how='outer')
#
# print(res1)

# Joining dataframe using on in an argument :
# data1 = {'Name':['Jai', 'Princi'],
#         'Age':[27, 24],
#         'Key':['K0', 'K1']}
# data2 = {'Address':['Allahabad', 'Kannuaj'],
#         'Qualification':['MCA', 'Phd']}
# df = pd.DataFrame(data1)
#
# df1 = pd.DataFrame(data2, index=['K0', 'K2'])
#
#
# print(df, "\n\n", df1)
#
#
#
# res2 = df.join(df1, on='Key')
#
# print(res2)

# Joining singly-indexed DataFrame with multi-indexed DataFrame :
# data1={'Name':['ashish','jai', 'Gaurav'],
#        'Age':[24,35,36]}
# data2={'Address':['ksg','ajmer', 'Allahabad', 'Kanpur'],
#        'Qualification':['MCA','MSC', 'Bcom', 'B.hons']}
#
#
# df=pd.DataFrame(data1,index=pd.Index(['k0','k1', 'K2'],name='key'))
# index = pd.MultiIndex.from_tuples([('K0', 'Y0'), ('K1', 'Y1'),
#                                    ('K2', 'Y2'), ('K2', 'Y3')],
#                                    names=['key', 'Y'])
#
# df1 = pd.DataFrame(data2, index=index)
#
# print(df, "\n\n", df1)
#
# result = df.join(df1, how='inner')
#
# print(result)

# Joining dataframe using on in an argument :
data1 = {'Name': ['Jai', 'Princi'],
         'Age': [27, 24],
         'Key': ['K0', 'K1']}

data2 = {'Address':['ksg','ajmer'],
        'Qualification':['MCA', 'MSC']}


df = pd.DataFrame(data1)


df1 = pd.DataFrame(data2, index=['K0', 'K1'])


print(df, "\n\n", df1)

res2 = df.join(df1, on='Key')


print(res2)