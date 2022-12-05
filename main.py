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
# ser = pd.Series()
print()
data = np.array(['g', 'e', 'e', 'k', 's'])

ser = pd.Series(data)
print(ser)
print("")


df=pd.DataFrame()
print(df)
lst=['ashish','mundra']
df=pd.DataFrame(lst)
print(df)

# Pandas DataFrame
# Pandas DataFrame is two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns. Pandas DataFrame consists of three principal components, the data, rows, and columns.
# Creating a Pandas DataFrame
# Pandas DataFrame will be created by loading the datasets from existing storage, storage can be SQL Database, CSV file, and Excel file. Pandas DataFrame can be created from the lists, dictionary, and from a list of dictionary etc. Dataframe can be created in different ways here are some ways by which we create a dataframe:
lst=['ashish','mundra','friend','address','house']
df=pd.DataFrame(lst)
print(df)
print("")

data = {'Name':['ashish','ajay','rohan','harshal'],
      'Age':[20,19,29,20]}
df = pd.DataFrame(data)
print(df)
print("")



# Dealing with Rows and Columns7
# A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns. We can perform basic operations on rows/columns like selecting, deleting, adding, and renaming.
data={'Name':['jai','nick','anuj','ashish'],
      'Age':[27,24,25,32],
      'Address':['delhi','kanpur','jaipur','ajmer'],
      'Qualification':['Msc','MA','MCA','phd']}
df=pd.DataFrame(data)
print(df[['Name','Qualification']])
print("")
# Create pandas dataframe from lists using dictionary:
# Creating pandas data-frame from lists using dictionary can be achieved in different ways. We can create pandas dataframe from lists using dictionary using pandas.DataFrame. With this method in Pandas we can transform a dictionary of list to a dataframe.
dicit={'name':["pankaj","ashish","ravi","rohan"],
       'degree':["MBA","BCA","M.TECT","MCA"],
       'score':[90,40,50,60]}
df=pd.DataFrame(dicit)
print(df)

