import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 

# 2D Plot. 
price = [48000, 54000, 57000, 49000, 47000, 45000]
year = [2015, 2016, 2017, 2018, 2019, 2020]
plt.plot(year, price)
# plot(x_axis, y_axis)
# x_axis => we always plot categorical data on x-axis. 
# y-axis => we always plot numerical data on y-axis.

# 
batsman = pd.read_csv("/content/drive/MyDrive/Datasets_DataVisualization/sharma-kohli.csv")
# batsman

plt.plot(batsman['index'], batsman['V Kohli'])

# plotting multiple plots. 
plt.plot(batsman['index'], batsman['V Kohli'])
plt.plot(batsman['index'], batsman['RG Sharma'])

# plotting multiple plots. 
plt.plot(batsman['index'], batsman['V Kohli'])
plt.plot(batsman['index'], batsman['RG Sharma'])

plt.title("Comparing the career of Rohit sharma and Virat kohli")
plt.xlabel("Season in year")
plt.ylabel("Runs scored")

# colors(hex) and line(width and style) and marker(size)
# plotting multiple plots. 
plt.plot(batsman['index'], batsman['V Kohli'], color='green')
plt.plot(batsman['index'], batsman['RG Sharma'], color='red')

plt.title("Comparing the career of Rohit sharma and Virat kohli")
plt.xlabel("Season in year")
plt.ylabel("Runs scored")

plt.plot(batsman['index'], batsman['V Kohli'], color='green', linestyle='dotted', linewidth=3)
plt.plot(batsman['index'], batsman['RG Sharma'], color='red',linestyle='dashdot', linewidth=2)

plt.title("Comparing the career of Rohit sharma and Virat kohli")
plt.xlabel("Season in year")
plt.ylabel("Runs scored")

plt.plot(batsman['index'], batsman['V Kohli'], color='green', linestyle='dotted', linewidth=3, marker='D', markersize=10)
plt.plot(batsman['index'], batsman['RG Sharma'], color='red',linestyle='dashdot', linewidth=2, marker='o')

plt.title("Comparing the career of Rohit sharma and Virat kohli")
plt.xlabel("Season in year")
plt.ylabel("Runs scored")

# legend -> location.
plt.plot(batsman['index'], batsman['V Kohli'], color='green', linestyle='dotted', linewidth=3, marker='D', markersize=10, label='virat')
plt.plot(batsman['index'], batsman['RG Sharma'], color='red',linestyle='dashdot', linewidth=2, marker='o', label='Rohit')

plt.title("Comparing the career of Rohit sharma and Virat kohli")
plt.xlabel("Season in year")
plt.ylabel("Runs scored")

plt.legend(loc='best') # best always takes where there is place in the graphs. 

# 
price = [48000, 54000, 57000, 49000, 47000, 45000, 4500000]
year = [2015, 2016, 2017, 2018, 2019, 2020,2021]

plt.plot(year, price)
# we used the triming when we have outlier in our datasets. 
plt.ylim(0,75000) # setting the limits or range.
plt.xlim(2017,2021)

# 
# Legend -> Location.
plt.plot(batsman['index'], batsman['V Kohli'], color='green', linestyle='dotted', linewidth=3, marker='D', markersize=10, label='virat')
plt.plot(batsman['index'], batsman['RG Sharma'], color='red',linestyle='dashdot', linewidth=2, marker='o', label='Rohit')

plt.title("Comparing the career of Rohit sharma and Virat kohli")
plt.xlabel("Season in year")
plt.ylabel("Runs scored")
plt.grid()

plt.legend(loc='best') # best always takes where there is place in the graphs.
plt.show()

# scatter plot. 
# Used for the Bivariate Analysis.
# Only for the numerical vs numerical columns. 
# Use case - Finding correlation.
# plt.scatter simple function. 
x = np.linspace(-10, 10, 50) # -10, +10, samma 50 points. 
y = 10*x + np.random.randint(0,300,50)

y

# 
plt.scatter(x,y)
plt.xlabel("numerical inputs")
plt.ylabel("prediction")

# 
df = pd.read_csv("/content/drive/MyDrive/Datasets_DataVisualization/batter.csv")
df = df.head(50)
df

# 
plt.scatter(df['avg'], df['strike_rate'], color='green')
plt.title("Avg and strike rate analysis of Top 50 Batsman")
plt.xlabel("Average")
plt.ylabel("strike rate")

# 
# size
import seaborn as sns
tips = sns.load_dataset('tips')
# tips
# # This is slower techniques. 
# s=tips['size']*20 represent the tyo particular customers ko sath ma aru kati Jana customers ako theeya tww, size le dekhaucha..
plt.scatter(tips['total_bill'], tips['tip'], s=tips['size']*20)

# 
# scatterplot using plt.plot 
# This is faster techniques. 
plt.plot(tips['total_bill'], tips['tip'], 'o')

# Barchart
# # Bivariate Analysis.
# Numerical Vs Categorical.
# Use case - Aggregate Analysis of groups.
# simple bar chart. 
children = [10,20,40,10,30]
colors = ['red','blue','green','yellow','pink']
plt.bar(colors, children, color='green')

# 
# horizontal bar chart. 
children = [10,20,40,10,30]
colors = ['red','blue','green','yellow','pink']
plt.barh(colors, children, color='green')
# Horizontal Bar chart use case: if the numerical of categories is increased then
# better to use the horizontal bar chart. 

# 
# color and label. 
df = pd.read_csv("/content/drive/MyDrive/Datasets_DataVisualization/batsman_season_record.csv")
df

# 
plt.bar(df['batsman'], df['2015'])
plt.bar(df['batsman'], df['2016'])
plt.bar(df['batsman'], df['2017'])

# 
# plotting bar chart side by side 
plt.bar(np.arange(df.shape[0]) - 0.2, df['2015'], width=0.2)
plt.bar(np.arange(df.shape[0]), df['2016'], width=0.2)
plt.bar(np.arange(df.shape[0]) + 0.2, df['2017'], width=0.2)

plt.xticks(np.arange(df.shape[0]),df['batsman'])
plt.show()

# 
# a problem
children = [10,20,40,10,30]
colors = ['red red red','blue blue blue','green green green','yellow yellow yellow','pink pink pink']

plt.bar(colors, children, color='green')
plt.xticks(rotation='vertical')

# 
# stacked bar chart.: Issues found here. 
plt.bar(df['batsman'], df['2015'], color='red', label='2017')
plt.bar(df['batsman'], df['2016'], bottom=df['2015'], color='green', label='2016')
plt.bar(df['batsman'], df['2017'], bottom=df['2016']+df['2015'], color='blue', label='2017')
plt.legend()

# 
# Histogram
# Univariate Analysis. 
# Numerical columns. 
# Use case - Frequency Counts. 

# Simple Data. 

data = [32, 45, 56, 10, 15, 27, 61]
plt.hist(data,bins=[10,15,20,25,30,35,45,60,70,90])

# on some data. 
df = pd.read_csv("/content/drive/MyDrive/Datasets_DataVisualization/vk.csv")
df

# 
plt.hist(df['batsman_runs'], bins=[0,10,20,30,40,50,60,70,80,90,100,120])
plt.show()

# 
# Logarithmic:
arr = np.load("/content/drive/MyDrive/Datasets_DataVisualization/big-array.npy")
plt.hist(arr, bins=[10,20,30,40,50,60,70], log=True)
plt.show()

# 
# Pie-chart
# 
# Univariate/Bivariate Analysis. 
# Categorical Vs Numerical. 
# Use case - To find contribution on a standard scale. 
# simple data. 
data = [23, 45, 100, 20, 40]
subjects = ['eng','science','maths','sst','nepali']
plt.pie(data, labels=subjects)
plt.show()

# 
df = pd.read_csv("/content/drive/MyDrive/Datasets_DataVisualization/gayle-175.csv")
df

# 
plt.pie(df['batsman_runs'], labels=df['batsman'], autopct='%0.1f%%')
plt.show()

# 
# Percentage and colors. 
plt.pie(df['batsman_runs'], labels=df['batsman'], autopct='%0.1f%%',explode=[0.3,0,0,0,0,0.1])
plt.show()

# 
# Changing styles.
# plt.style.available
plt.style.use('fivethirtyeight')

# 
arr = np.load("/content/drive/MyDrive/Datasets_DataVisualization/big-array.npy")
plt.hist(arr, bins=[10,20,30,40,50,60,70], log=True)
plt.show()

# 
# save figure. 
arr = np.load("/content/drive/MyDrive/Datasets_DataVisualization/big-array.npy")
plt.hist(arr, bins=[10,20,30,40,50,60,70], log=True)
# don't use the plt.show in this case while saving the image. 
# otherwise, black image will be save. 
plt.savefig('sample1.png')

# 


