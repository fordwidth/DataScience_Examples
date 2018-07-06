# Prep Lyme Disease Incidence report
import pandas as pd
# https://www.cdc.gov/lyme/resources/ld-Case-Counts-by-County-00-16.csv
lyme = pd.read_csv("ld-Case-Counts-by-County-00-16.csv")
MA = lyme.loc[lyme['Stname'] == 'Massachusetts']
MA = MA.drop(['Stname', 'STCODE', 'CTYCODE'], 1)

# remove county from county name
MA['Ctyname'] = MA['Ctyname'].str.split(' ').str[0]
# set index and make equal to that of weather report
MA = MA.rename(index = str, columns = {'Ctyname':'County'})
MA.set_index('County', drop = True, inplace = True)

# remove Massachusetts from county names
MA = MA.drop(['Massachusetts'], axis = 0)
years = list(range(2000, 2017, 1))
MA.columns = years

# Weather data only available for 2005 to 2013. Cut. 
years = [2000, 2001, 2002, 2003, 2004, 2014, 2015, 2016]
MA = MA.drop(labels= years, axis=1)

# Data for Franklin county is so small it jumps wildly and will skew group results. Cut. 
MA = MA.drop(labels= 'Franklin', axis=0)
MA = MA.T
Countymean = MA.mean() #  Barnstable    208.777778 checks out

# Normalize winter temps to mean of each County over time period
MA = MA/Countymean # Barnstable 2005 = 1.08, 2006 = 0.49 checks out
# Get mean and standard deviation for normalized winter temps
MAmean = list(MA.mean(axis = 1)) 
MAstd = list(MA.std(axis = 1))
MA.head()

###########################################
# record of average temperatures over winter months Jan, Feb, Mar.  
# source: https://w2.weather.gov/climate/xmacis.php?wfo=box
#Weather station associated with county was identified and data manually collected. 
weather = pd.read_csv('MA_County_Winter_Lows.csv')
weather.set_index('County', drop = True, inplace = True)

# Remove station information 
weather = weather.drop(labels = 'Station', axis=1)
weather = weather.drop('Average Temp for (Jan-Feb-Mar)', axis = 0)

# Flip to have years as columns and 
weather = weather.T

# Data for Franklin county incidence is so small it jumps wildly and will skew group results. Cut. 
weather = weather.drop(labels= 'Franklin', axis=1)

# get mean for each county 
CountymeanWeather = weather.mean() 

# Normalize winter temps to mean of each County over time period
#weather = weather/CountymeanWeather #

# Get mean change for each year
weathermean = list(weather.mean(axis = 1)) 
weatherstd = list(weather.std(axis = 1))
y_plot = range(len(weathermean))
years = list(range(2005, 2014, 1))
weather.head()

##############################################
import matplotlib.pyplot as plt
fig, ax1 = plt.subplots()


COLOR = 'orange'
ax1.set_ylabel('Normalized Mean Temp in MA Counties', color = COLOR)  
ax1.bar(y_plot, MAmean, yerr = MAstd, color = COLOR)
ax1.tick_params(axis='y', color = COLOR)
ax1.set_xticks(range(len(years)), minor=False)
ax1.set_xticklabels(years, fontdict=None, minor=False)

ax2 = ax1.twinx()  # instantiate second axes that shares axis with ax1

COLOR = 'brown'
ax2.set_title("Cold Winters Do Not Directly Affect Lyme Disease")
ax2.set_xlabel('Year')
ax2.set_ylabel('Mean Normalized Incidence/100K', color = COLOR)
ax2.plot(weathermean, color = COLOR, linewidth = 5.0)
ax2.tick_params(axis = 'y', labelcolor = COLOR)
ax2.errorbar(range(len(years)), weathermean, yerr = weatherstd, ecolor = COLOR, fmt = 'none')

plt.show()
fig.savefig('Winter_LymeDisease.png')
