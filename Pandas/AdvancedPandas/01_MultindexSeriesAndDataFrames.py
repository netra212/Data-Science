import numpy as np 
import pandas as pd

# series is 1D and DataFrame are 2D Objects. 

# can we have multiple index? Let's try
index_val = [('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
a = pd.Series([1,2,3,4,5,6,7,8],index=index_val)
print(a)

# The solution -> multiindex series(also known as Hierarchical Indexing)
# multiple index levels within a single index

# how to create multiindex object
# 1. pd.MultiIndex.from_tuples()
index_val = [('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
multiindex = pd.MultiIndex.from_tuples(index_val)
print(multiindex.levels[1]) # decouple the series. 
# 2. pd.MultiIndex.from_product()
pd.MultiIndex.from_product([['cse','ece'],[2019,2020,2021,2022]])

# level inside multiindex object
# creating a series with multiindex object
print("\nMultiindex series: \n")
s = pd.Series([1,2,3,4,5,6,7,8],index=multiindex)
print(s)

# how to fetch items from such a series
print(s['cse'])

# a logical question to ask

# unstack() : convert the multi-index series into the dataframe. 
# inner index converted into the column. In this case, date. 
print("\nunstack(): convert the multi-index series into the DataFrame.\n")
temp = s.unstack()
print(temp)

# How to fetch items from such a series.
# Multi-Index DataFrame. 
print("Multi-Index DataFrame: ")
branch_df1 = pd.DataFrame(
    [
        [1,2],
        [3,4],
        [5,6],
        [7,8],
        [9,10],
        [11,12],
        [13,14],
        [15,16]
    ],
    index=multiindex,
    columns=["avg_package", "students"]
)
print(branch_df1)

# pandas understand index and column as same. 

# multiindex df from columns perspective. 
print("\nMultiindex df from columns perspective: \n")
branch_df2 = pd.DataFrame([
    [1,2,0,0],
    [3,4,0,0],
    [5,6,0,0],
    [7,8,0,0],
], index=[2019, 2020, 2021, 2022],
columns=pd.MultiIndex.from_product([
    ['delhi','mumbai'],
    ['avg_package','students']
]))
print(branch_df2)
# from_product() <-- Perform the cartesian product. 

print(branch_df2['mumbai'])
print(branch_df2['mumbai']['avg_package'])
print("\n Fetching rows data: \n")
print(branch_df2.loc[2019])

# Multiindex df in terms of both cols and index. 
print("\nMultiindex df in terms of both cols and index: ")
print("\n4D Representation of the Data: \n")
branch_df3 = pd.DataFrame([
    [1,2,0,0],
    [3,4,0,0],
    [5,6,0,0],
    [7,8,0,0],
    [9,10,0,0],
    [11,12,0,0],
    [13,14,0,0],
    [15,16,0,0],
], index=multiindex,
columns=pd.MultiIndex.from_product([
    ['delhi','mumbai'],
    ['avg_package','students']
]))
print(branch_df3)


"""
***********************************
#. Stacking and Unstacking. 
***********************************
"""
print("\n***********************************")
print("Stacking and Unstacking. ")
print("***********************************\n")
# unstack() le vitra ko index laii rows to columns ma convert gardincha but branch_df1 ma year is cols ma convert huncha but there is already cols avg_package, and students... but still there column ma huncha..
print("\n***********************************")
print("Unstacking: Converting rows to column. ")
print("***********************************\n")
print(branch_df1.unstack())
print("\nImplementing unstacking 2 times : ")
print("\nLevel 0 ma vako panii column ma convert vaihalcha...")
print(branch_df1.unstack().unstack())

# stacking. 
print("\n***********************************")
print("stacking: Converting columns to rows. ")
print("***********************************\n")
print(branch_df1.unstack().stack())

print(branch_df2.stack())

print(branch_df3.unstack())

print(branch_df3.stack())

"""
#. Working with multi-index DataFrames:
"""
print("*********************************")
print("Working with multi-index DataFrames: ")
print("*********************************")

print("shape of branch_df3: ",branch_df3.shape)
print("first 5 data: \n", branch_df3.head())
print("Information: ", branch_df3.info())
print("Duplicated : \n",branch_df3.duplicated())
print("Checking null values : ", branch_df3.isnull())


# Extracting rows single. 
# loc -> when we have an name index. 
# iloc -> when we have an number index. 
print("\nExtracting rows single. ")
print(branch_df3.loc[('cse',2022)])

# 
print("\nExtracting multiple rows alternatively with loc(name index vako time ma use huncha...)")
print(branch_df3.loc[('cse', 2019):('ece',2020):2])
print("\nExtracting multiple rows alternatively with iloc(int index vako time ma use huncha...\n)")
print(branch_df3.iloc[0:5:2])

print("\nExtracting cols : ")
print(branch_df3['delhi']['students'])
print(branch_df3.iloc[:,1:3])

# Extracing both.
print("\nExtracting Both: ")
print(branch_df3.iloc[[0,4],[1,2]])

# sorting.
print("\n*****************************")
print("Sorting Index")
print("*******************************\n")

print("sorting on descending order: ", branch_df3.sort_index(ascending=False))
print("sorting on descending order: ", branch_df3.sort_index(ascending=[False,True]))
# branch zero : sort descending order 
# branch 2 : sort ascending order. 

# what if i don't want to sort in two level.
print("\nWhat if i don't want to sort in two level.") 
print(branch_df3.sort_index(level=1, ascending=[False])) # sorting on the basis of the year. 

# multiindex dataframe(col) -> transpose. 
print("\nTranspose: \n",branch_df3.transpose())

print("\n swap level row-wise: \n", branch_df3.swaplevel())

print("\n swap level col-wise: \n", branch_df3.swaplevel(axis=1))

"""
#. Long Vs Wide Data
#. Wide format: where we have a single row for every data points with multiple columsn to hold the values of various attributes. 

#. Long format: where, each data points we have as many rows as the number of attributes and each row contains the value of a particular attribute for a given data point.
"""
print("\n*****************************")
print("Long Vs Wide Data")
print("\nWide format: where we have a single row for every data points with multiple columsn to hold the values of various attributes.  ")
print("\nLong format: where, each data points we have as many rows as the number of attributes and each row contains the value of a particular attribute for a given data point.")
print("*******************************\n")

# melt -> wide data format ko long data format ma convert garne. 
# melt -> wide to long. 
print(pd.DataFrame({
    'cse':[120]
}).melt())

print("wide format data to long format data:\n", pd.DataFrame({
    'cse':[120],
    'ece':[100],
    'mech':[50]
}).melt(var_name="branch",value_name="num_students"))

print("\nWide format data to long format data:\n", pd.DataFrame({
    'branch':['cse','ece','mech'],
    '2020':[100,150,60],
    '2021':[120,130,80],
    '2022':[150,140,70]
}))

print("\nImplementation melt function: \n")
print(pd.DataFrame({
    'branch':['cse','ece','mech'],
    '2020':[100,150,60],
    '2021':[120,130,80],
    '2022':[150,140,70]
}).melt(id_vars=['branch'], var_name='year',value_name='students'))

# Reading Datasets. 
death = pd.read_csv("/Users/netrakc/Desktop/Data-Science/Pandas/AdvancedPandas/time_series_covid19_deaths_global.csv")

confirmed = pd.read_csv("/Users/netrakc/Desktop/Data-Science/Pandas/AdvancedPandas/time_series_covid19_confirmed_global.csv")

print("\nDeath Datasets: ")
print(death.head())
print(death.shape)
print("\nConfirmed Datasets: ")
print(confirmed.head())
print(confirmed.shape)


# merge two datasets with four columns:
# cols name: country, date, confirmed number, death number.
# usa, 3rd jan, 2000, 30
# nepal, 4th feb, 1400, 45

# Convert wide datasets into the long format.
print("\n#Converting wide range datasets into long format datasets: ") 
print(death.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], var_name='date', value_name='num_deaths'))

print("\n#Converting wide range datasets into long format datasets: ")
print(confirmed.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], var_name='date', value_name='num_deaths'))

print(confirmed.merge(death, on=['Province/State', 'Country/Region', 'Lat','Long'])[['Province/State', 'Country/Region', 'Lat','Long']])



