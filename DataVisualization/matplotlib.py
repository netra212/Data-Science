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

# 

