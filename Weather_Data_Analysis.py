#!/usr/bin/env python
# coding: utf-8

# ## Project Name:- "Exploring Weather Trends: Insights and Analysis for Effective Decision Making"
# * Astract:-This project aims to conduct a comprehensive analysis of a weather dataset using Python data analysis techniques.The primary objective of this project is to extract valuable insights and meaningful patterns from the weather data for practical applications.The outcomes of this analysis will contribute to informed decision-making processes and enable professionals in various domains to make more effective and evidence-based decisions related to weather conditions.

# ### 1.Data Cleaning and Pre-Processing
# * Checking for the  missing values and handle them appropriately (imputation or removal).
# * Converting the data types of columns if required (e.g., converting date/time to a datetime object).
# * Removing the duplicates if any.

# * The provided weather dataset exhibits a high level of data integrity, with no duplicate values or missing entries observed. The dataset has been carefully curated, ensuring its suitability for analysis purposes.

# ## 2.Descriptive Statistics:

# In[3]:


## importing the Required libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


# In[7]:


## Loading the dataset
data=pd.read_csv("weatherdata.csv")


# In[8]:


data


# In[10]:


## checking the size of the data set
data.shape


# In[11]:


data.head()  ## it showing the top 5 fields in the data set


# In[12]:


data.tail() ## it showing the top 5 from the last position


# In[13]:


## Basic Statistics
data.describe()


# * 1.Histograms
# * To examine the distribution of variables, create histograms using the hist() function from the matplotlib library. we can select specific columns of interest and customize the number of bins, labels, and plot aesthetics to best represent the data distribution.

# In[14]:


data.columns


# In[16]:


## Histograms
plt.hist(data['Temp_C'],bins=10,color='red')
plt.xlabel('Temperature (celsius)')
plt.ylabel('Frequency')
plt.title('Distribution of Temperature')


# *  temperature is 20 degrees Celsius and the frequency is 1400, it indicates the number of occurrences or observations of the temperature value 20 degrees Celsius.

# In[15]:


## histogram for distribution of presuure
plt.hist(data['Press_kPa'],bins=10,color='blue')
plt.xlabel('Presuure (kpa)')
plt.ylabel('Frequency')
plt.title('Distribution of Presure')


# * 2.Box Plots:
# * Generate box plots using the boxplot() function from the matplotlib library to visualize the distribution, central tendency, and outliers of variables. This plot provides information on the minimum, maximum, quartiles, and any potential outliers present in the data.

# In[17]:


## Box plots
plt.boxplot(data['Temp_C'])
plt.xlabel('Temperature')
plt.ylabel('Degree Celsius')
plt.title('Distribution of Temperature')


# * The box plot helps in understanding the central tendency, spread, and potential outliers in the temperature distribution. It provides a concise summary of the temperature data and facilitates easy comparison with other variables or across different groups or time periods.

# In[18]:


plt.boxplot(data['Press_kPa'])
plt.xlabel('Pressure')
plt.ylabel('Kilo Pascal')
plt.title('Distribution of Presuure')


# In[16]:


data.columns


# * 3.Density Plots:-Density plots can be created using the plot(kind='density') function of the DataFrame. This plot provides an estimation of the probability density function of a variable. It helps visualize the overall shape and peaks in the distribution.

# In[20]:


## Density plots
data['Temp_C'].plot(kind='density')
plt.xlabel('Temperature (Celsius)')
plt.ylabel('Density')
plt.title('Density plot of Temperature')


# * 4.Range, Minimum, and Maximum Values:
# * To analyze the range, minimum, and maximum values for each column, you can use the min() and max() functions on the DataFrame. This will return the minimum and maximum values for all the columns. Additionally, you can calculate the range by subtracting the minimum value from the maximum value.

# In[34]:


min_values=data.min()
max_values=data.max()


# In[35]:


print("minimum values")
print(min_values)
print("Maximum Values")
print(max_values)


# ## 3 Time-Based Analysis

# * Explore the temporal aspect of the data by analyzing trends, seasonality, and patterns over time.
# * Plot time series plots for variables like temperature, humidity, and wind speed to observe long-term trends.
# * Investigate if there are any recurring weather patterns or events during specific months or seasons.

# In[37]:


## Convert the "Date/Time" column to a datetime data type
data['Date/Time']=pd.to_datetime(data['Date/Time'])
## set the"Date/Time" column as the index
data.set_index("Date/Time",inplace=True)


# In[43]:


## Plot the Time series plots
data['Temp_C'].plot(figsize=(12,6))
plt.title("Temperature Time Series")
plt.xlabel("Date")
plt.ylabel("Temperature(Degree celsius)")
plt.show()


# In[46]:


## Analyzing the reccuring weather patterns

## Group by month and caluclulating Mean Temperature
monthly_mean_temperature=data['Temp_C'].resample('M').mean()

## ploting the monthly mean temperature
monthly_mean_temperature.plot(figsize=(12,6))
plt.title("Monthly mean temperature")
plt.xlabel("Date")
plt.ylabel("Temperature (Degree celsius)")
plt.show()


# In[54]:


# Group by month and caluclulating Mean Temperature
Quarterly_mean_temperature=data['Temp_C'].resample('Q').mean()

## ploting the Quarterly mean temperature
Quarterly_mean_temperature.plot(figsize=(12,6))
plt.title("Quarterly mean temperature")
plt.xlabel("Date")
plt.ylabel("Temperature (Degree celsius)")
plt.show()


# In[56]:


## similarly we can do for remaining columns
## Group by month and caluclulating Mean Pressure
monthly_mean_pressure=data['Press_kPa'].resample('M').mean()

## ploting the monthly mean temperature
monthly_mean_pressure.plot(figsize=(12,6))
plt.title("Monthly mean Pressure")
plt.xlabel("Date")
plt.ylabel("Pressure  (Kpa)")
plt.show()


# In[ ]:





# In[55]:


data.columns


# In[57]:


## Group by month and caluclulating Mean Relative Humidity
monthly_mean_relativehumidity=data['Rel Hum_%'].resample('M').mean()

## ploting the monthly mean temperature
monthly_mean_relativehumidity.plot(figsize=(12,6))
plt.title("Monthly mean Relativehumidity")
plt.xlabel("Date")
plt.ylabel("Relative humidity %")
plt.show()


# In[60]:


## Group by month and caluclulating Mean Wind speed 
monthly_mean_windspeed=data['Wind Speed_km/h'].resample('M').mean()

## ploting the monthly mean windsspeed
monthly_mean_windspeed.plot(figsize=(12,6))
plt.title("Monthly mean windspeed")
plt.xlabel("Date")
plt.ylabel("wind speed in km/hr")
plt.show()


# ## 4.Correlation Analysis:

# * Determine the relationships between different variables using correlation analysis.
# * Calculate correlation coefficients (e.g., Pearson's correlation) to identify the strength and direction of relationships.
# * Create correlation matrices and visualize them using heatmaps

# In[68]:


## calculating the corelation coefficents 
correlation_matrix=data.corr(numeric_only=True)


# In[69]:


correlation_matrix


# In[70]:


## visuvalize the correlation matrices using the heat pumps 
import seaborn as sns 
sns.heatmap(correlation_matrix,annot=True,cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()


# ## 5.Weather Patterns

# In[82]:


## Extract the weather column
weather_conditions=data['Weather']
print(weather_conditions)
## calculate the frequency of each weather conditon
weather_frequency=weather_conditions.value_counts()
print(weather_frequency)
## identify the most common weather conditions
most_common_weather=weather_frequency.head(5) ## select the top 5 most common weather conditions
print(most_common_weather)
## Analyze weather conditions by season or month
# Group data by season and calculate frequency of weather conditions
weather_by_visibility = data.groupby('Visibility_km')['Weather'].value_counts()
print(weather_by_visibility)
# Group data by month and calculate frequency of weather conditions
weather_by_month = data.groupby(data.index.month)['Weather'].value_counts()
print(weather_by_month)


# In[84]:


## Visuvalize the distribution of weather condition
# Bar chart for overall weather frequency
weather_frequency.plot(kind='bar',figsize=(10,6))
plt.title("Weather frequency")
plt.xlabel("weather condition")
plt.ylabel(" ")
plt.show()


# In[85]:


## pie chart for most common weather conditions
most_common_weather.plot(kind='pie',figsize=(8,8),autopct='%1.1f%%')
plt.title("Most common weather conditions")
plt.xlabel('')
plt.show()


# ## 6.Wind Analysis

# * Investigate the relationship between wind speed and other variables (temperature, humidity, etc.).
# * Determine the average wind speed for different wind directions.
# * Plot wind roses or wind speed histograms to visualize wind patterns.

# In[6]:


## investigating the wind speed with the other variables


## scatter plot of wind speed and temperature
plt.scatter(data['Wind Speed_km/h'],data['Temp_C'])
plt.title(" windspeed vs temperature")
plt.xlabel("wind speed in km/hr")
plt.ylabel("Temperature in degree celsius")
plt.show()
            


# In[10]:


## line plot of wind speed over time
plt.plot(data.index,data['Wind Speed_km/h'])
plt.title('Wind speed over time')
plt.xlabel('Date/Time')
plt.ylabel("wind speed km/hr")
plt.show()
          


# In[13]:


## Determine the average wind speed for different prssure variations
average_windspeed_by_pressurevariation=data.groupby("Press_kPa")["Wind Speed_km/h"].mean()
print(average_windspeed_by_pressurevariation)


# In[20]:


## plotting the wind speed histograms to visualize wind patterns
import numpy as np
from windrose import WindroseAxes

## wind rose plot
ax=WindroseAxes.from_ax()
ax.bar(data['Press_kPa'], data['Wind Speed_km/h'], normed=True, opening=0.8, edgecolor='white')
ax.set_legend()
plt.title("Wind Rose")
plt.show()



# In[22]:


## wind speed histogram
plt.hist(data['Wind Speed_km/h'],bins=np.arange(0,40,5))
plt.title('wind speed histogram')
plt.xlabel("wind speed km/hr")
plt.ylabel("frequency")
plt.show()


# ## Conclusion
# * In this project,I performed a comprehensive analysis of a weather dataset, focusing on various stages from data cleaning and preprocessing to Analysis. Here are the key findings and conclusions from each stage:
# 
# * Data Cleaning and Preprocessing: I started by ensuring the dataset was free of duplicate values and missing data. After cleaning, we confirmed that the dataset was in good shape and ready for analysis.
# 
# * Descriptive Statistics: I calculated basic statistics such as mean, median, mode, and standard deviation for temperature, humidity, and other variables. This provided insights into the central tendency and dispersion of the data.
# 
# * Histograms: By creating histograms, I examined the distribution of variables, such as temperature, humidity, and wind speed. These visualizations helped identify the frequency of different values and the shape of the distributions.
# 
# * Box Plots: Using box plots, I visualized the central tendency and outliers in the data. This allowed us to identify any extreme values and understand the spread and variability of the variables.
# 
# * Density Plots: Density plots helped us understand the probability density function of variables. By visualizing the shape and peaks in the distribution, I gained insights into the overall patterns and concentrations of values.
# 
# * Correlation Analysis: I explored the relationships between different variables using correlation analysis. By calculating correlation coefficients, we identified the strength  of the relationships. This provided insights into how variables such as temperature, humidity, and wind speed are related to each other.

# In[ ]:




