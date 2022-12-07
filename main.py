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
dict=