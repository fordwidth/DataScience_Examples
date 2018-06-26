{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Assignment 4\n",
    "\n",
    "Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.\n",
    "\n",
    "This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **weather phenomena** (see below) for the region of **Great Barrington, Massachusetts, United States**, or **United States** more broadly.\n",
    "\n",
    "You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Great Barrington, Massachusetts, United States** to Ann Arbor, USA. In that case at least one source file must be about **Great Barrington, Massachusetts, United States**.\n",
    "\n",
    "You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.\n",
    "\n",
    "Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!\n",
    "\n",
    "As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.\n",
    "\n",
    "Here are the assignment instructions:\n",
    "\n",
    " * State the region and the domain category that your data sets are about (e.g., **Great Barrington, Massachusetts, United States** and **weather phenomena**).\n",
    " * You must state a question about the domain category and region that you identified as being interesting.\n",
    " * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.\n",
    " * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.\n",
    " * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.\n",
    "\n",
    "What do we mean by **weather phenomena**?  For this category you might want to consider seasonal changes, natural disasters, or historical trends.\n",
    "\n",
    "## Tips\n",
    "* Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.\n",
    "* Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.\n",
    "* Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.\n",
    "* This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!\n",
    "\n",
    "## Example\n",
    "Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>County</th>\n",
       "      <th>Barnstable</th>\n",
       "      <th>Berkshire</th>\n",
       "      <th>Bristol</th>\n",
       "      <th>Dukes</th>\n",
       "      <th>Essex</th>\n",
       "      <th>Hampden</th>\n",
       "      <th>Hampshire</th>\n",
       "      <th>Middlesex</th>\n",
       "      <th>Nantucket</th>\n",
       "      <th>Norfolk</th>\n",
       "      <th>Plymouth</th>\n",
       "      <th>Suffolk</th>\n",
       "      <th>Worcester</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2005</th>\n",
       "      <td>1.082491</td>\n",
       "      <td>0.597586</td>\n",
       "      <td>0.527302</td>\n",
       "      <td>1.724211</td>\n",
       "      <td>0.771854</td>\n",
       "      <td>0.751592</td>\n",
       "      <td>0.715789</td>\n",
       "      <td>0.708281</td>\n",
       "      <td>0.660759</td>\n",
       "      <td>0.659562</td>\n",
       "      <td>0.774580</td>\n",
       "      <td>0.621664</td>\n",
       "      <td>0.603106</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2006</th>\n",
       "      <td>0.498137</td>\n",
       "      <td>0.443662</td>\n",
       "      <td>0.419689</td>\n",
       "      <td>0.397895</td>\n",
       "      <td>0.396358</td>\n",
       "      <td>0.547771</td>\n",
       "      <td>0.294737</td>\n",
       "      <td>0.460383</td>\n",
       "      <td>0.250633</td>\n",
       "      <td>0.462482</td>\n",
       "      <td>0.318945</td>\n",
       "      <td>0.254317</td>\n",
       "      <td>0.610871</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2007</th>\n",
       "      <td>1.025013</td>\n",
       "      <td>0.751509</td>\n",
       "      <td>0.746114</td>\n",
       "      <td>0.966316</td>\n",
       "      <td>0.908940</td>\n",
       "      <td>0.764331</td>\n",
       "      <td>0.663158</td>\n",
       "      <td>0.944911</td>\n",
       "      <td>1.389873</td>\n",
       "      <td>0.875036</td>\n",
       "      <td>0.776978</td>\n",
       "      <td>0.494505</td>\n",
       "      <td>0.882657</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2008</th>\n",
       "      <td>0.828632</td>\n",
       "      <td>1.466801</td>\n",
       "      <td>1.076126</td>\n",
       "      <td>0.966316</td>\n",
       "      <td>1.317219</td>\n",
       "      <td>1.210191</td>\n",
       "      <td>1.200000</td>\n",
       "      <td>1.369880</td>\n",
       "      <td>1.002532</td>\n",
       "      <td>1.298102</td>\n",
       "      <td>1.083933</td>\n",
       "      <td>1.144427</td>\n",
       "      <td>1.514236</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2009</th>\n",
       "      <td>1.178286</td>\n",
       "      <td>1.557344</td>\n",
       "      <td>1.126345</td>\n",
       "      <td>0.852632</td>\n",
       "      <td>1.174172</td>\n",
       "      <td>1.592357</td>\n",
       "      <td>1.547368</td>\n",
       "      <td>1.315149</td>\n",
       "      <td>1.048101</td>\n",
       "      <td>1.442628</td>\n",
       "      <td>1.105516</td>\n",
       "      <td>1.243328</td>\n",
       "      <td>1.436583</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "County  Barnstable  Berkshire   Bristol     Dukes     Essex   Hampden  \\\n",
       "2005      1.082491   0.597586  0.527302  1.724211  0.771854  0.751592   \n",
       "2006      0.498137   0.443662  0.419689  0.397895  0.396358  0.547771   \n",
       "2007      1.025013   0.751509  0.746114  0.966316  0.908940  0.764331   \n",
       "2008      0.828632   1.466801  1.076126  0.966316  1.317219  1.210191   \n",
       "2009      1.178286   1.557344  1.126345  0.852632  1.174172  1.592357   \n",
       "\n",
       "County  Hampshire  Middlesex  Nantucket   Norfolk  Plymouth   Suffolk  \\\n",
       "2005     0.715789   0.708281   0.660759  0.659562  0.774580  0.621664   \n",
       "2006     0.294737   0.460383   0.250633  0.462482  0.318945  0.254317   \n",
       "2007     0.663158   0.944911   1.389873  0.875036  0.776978  0.494505   \n",
       "2008     1.200000   1.369880   1.002532  1.298102  1.083933  1.144427   \n",
       "2009     1.547368   1.315149   1.048101  1.442628  1.105516  1.243328   \n",
       "\n",
       "County  Worcester  \n",
       "2005     0.603106  \n",
       "2006     0.610871  \n",
       "2007     0.882657  \n",
       "2008     1.514236  \n",
       "2009     1.436583  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Prep Lyme Disease Incidence report\n",
    "import pandas as pd\n",
    "# https://www.cdc.gov/lyme/resources/ld-Case-Counts-by-County-00-16.csv\n",
    "lyme = pd.read_csv(\"ld-Case-Counts-by-County-00-16.csv\")\n",
    "MA = lyme.loc[lyme['Stname'] == 'Massachusetts']\n",
    "MA = MA.drop(['Stname', 'STCODE', 'CTYCODE'], 1)\n",
    "\n",
    "# remove county from county name\n",
    "MA['Ctyname'] = MA['Ctyname'].str.split(' ').str[0]\n",
    "# set index and make equal to that of weather report\n",
    "MA = MA.rename(index = str, columns = {'Ctyname':'County'})\n",
    "MA.set_index('County', drop = True, inplace = True)\n",
    "\n",
    "# remove Massachusetts from county names\n",
    "MA = MA.drop(['Massachusetts'], axis = 0)\n",
    "years = list(range(2000, 2017, 1))\n",
    "MA.columns = years\n",
    "\n",
    "# Weather data only available for 2005 to 2013. Cut. \n",
    "years = [2000, 2001, 2002, 2003, 2004, 2014, 2015, 2016]\n",
    "MA = MA.drop(labels= years, axis=1)\n",
    "\n",
    "# Data for Franklin county is so small it jumps wildly and will skew group results. Cut. \n",
    "MA = MA.drop(labels= 'Franklin', axis=0)\n",
    "MA = MA.T\n",
    "Countymean = MA.mean() #  Barnstable    208.777778 checks out\n",
    "\n",
    "# Normalize winter temps to mean of each County over time period\n",
    "MA = MA/Countymean # Barnstable 2005 = 1.08, 2006 = 0.49 checks out\n",
    "# Get mean and standard deviation for normalized winter temps\n",
    "MAmean = list(MA.mean(axis = 1)) \n",
    "MAstd = list(MA.std(axis = 1))\n",
    "MA.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>County</th>\n",
       "      <th>Barnstable</th>\n",
       "      <th>Berkshire</th>\n",
       "      <th>Bristol</th>\n",
       "      <th>Dukes</th>\n",
       "      <th>Essex</th>\n",
       "      <th>Hampden</th>\n",
       "      <th>Hampshire</th>\n",
       "      <th>Middlesex</th>\n",
       "      <th>Nantucket</th>\n",
       "      <th>Norfolk</th>\n",
       "      <th>Plymouth</th>\n",
       "      <th>Suffolk</th>\n",
       "      <th>Worcester</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2005</th>\n",
       "      <td>33.0</td>\n",
       "      <td>24.0</td>\n",
       "      <td>30.0</td>\n",
       "      <td>33.0</td>\n",
       "      <td>28.0</td>\n",
       "      <td>27.0</td>\n",
       "      <td>27.0</td>\n",
       "      <td>27.0</td>\n",
       "      <td>33.0</td>\n",
       "      <td>29.0</td>\n",
       "      <td>28.0</td>\n",
       "      <td>31.0</td>\n",
       "      <td>27.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2006</th>\n",
       "      <td>36.0</td>\n",
       "      <td>28.0</td>\n",
       "      <td>35.0</td>\n",
       "      <td>37.0</td>\n",
       "      <td>33.0</td>\n",
       "      <td>31.0</td>\n",
       "      <td>32.0</td>\n",
       "      <td>32.0</td>\n",
       "      <td>36.0</td>\n",
       "      <td>34.0</td>\n",
       "      <td>34.0</td>\n",
       "      <td>35.0</td>\n",
       "      <td>32.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2007</th>\n",
       "      <td>34.0</td>\n",
       "      <td>24.0</td>\n",
       "      <td>32.0</td>\n",
       "      <td>34.0</td>\n",
       "      <td>30.0</td>\n",
       "      <td>28.0</td>\n",
       "      <td>27.0</td>\n",
       "      <td>29.0</td>\n",
       "      <td>34.0</td>\n",
       "      <td>32.0</td>\n",
       "      <td>31.0</td>\n",
       "      <td>32.0</td>\n",
       "      <td>27.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2008</th>\n",
       "      <td>35.0</td>\n",
       "      <td>25.0</td>\n",
       "      <td>34.0</td>\n",
       "      <td>36.0</td>\n",
       "      <td>31.0</td>\n",
       "      <td>29.0</td>\n",
       "      <td>28.0</td>\n",
       "      <td>31.0</td>\n",
       "      <td>35.0</td>\n",
       "      <td>33.0</td>\n",
       "      <td>33.0</td>\n",
       "      <td>35.0</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2009</th>\n",
       "      <td>32.0</td>\n",
       "      <td>24.0</td>\n",
       "      <td>30.0</td>\n",
       "      <td>33.0</td>\n",
       "      <td>28.0</td>\n",
       "      <td>28.0</td>\n",
       "      <td>26.0</td>\n",
       "      <td>29.0</td>\n",
       "      <td>33.0</td>\n",
       "      <td>31.0</td>\n",
       "      <td>30.0</td>\n",
       "      <td>32.0</td>\n",
       "      <td>27.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "County  Barnstable  Berkshire  Bristol  Dukes  Essex  Hampden  Hampshire  \\\n",
       "2005          33.0       24.0     30.0   33.0   28.0     27.0       27.0   \n",
       "2006          36.0       28.0     35.0   37.0   33.0     31.0       32.0   \n",
       "2007          34.0       24.0     32.0   34.0   30.0     28.0       27.0   \n",
       "2008          35.0       25.0     34.0   36.0   31.0     29.0       28.0   \n",
       "2009          32.0       24.0     30.0   33.0   28.0     28.0       26.0   \n",
       "\n",
       "County  Middlesex  Nantucket  Norfolk  Plymouth  Suffolk   Worcester  \n",
       "2005         27.0       33.0     29.0      28.0      31.0       27.0  \n",
       "2006         32.0       36.0     34.0      34.0      35.0       32.0  \n",
       "2007         29.0       34.0     32.0      31.0      32.0       27.0  \n",
       "2008         31.0       35.0     33.0      33.0      35.0       30.0  \n",
       "2009         29.0       33.0     31.0      30.0      32.0       27.0  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# record of average temperatures over winter months Jan, Feb, Mar.  \n",
    "# source: https://w2.weather.gov/climate/xmacis.php?wfo=box\n",
    "#Weather station associated with county was identified and data manually collected. \n",
    "weather = pd.read_csv('MA_County_Winter_Lows.csv')\n",
    "weather.set_index('County', drop = True, inplace = True)\n",
    "\n",
    "# Remove station information \n",
    "weather = weather.drop(labels = 'Station', axis=1)\n",
    "weather = weather.drop('Average Temp for (Jan-Feb-Mar)', axis = 0)\n",
    "\n",
    "# Flip to have years as columns and \n",
    "weather = weather.T\n",
    "\n",
    "# Data for Franklin county incidence is so small it jumps wildly and will skew group results. Cut. \n",
    "weather = weather.drop(labels= 'Franklin', axis=1)\n",
    "\n",
    "# get mean for each county \n",
    "CountymeanWeather = weather.mean() \n",
    "\n",
    "# Normalize winter temps to mean of each County over time period\n",
    "#weather = weather/CountymeanWeather #\n",
    "\n",
    "# Get mean change for each year\n",
    "weathermean = list(weather.mean(axis = 1)) \n",
    "weatherstd = list(weather.std(axis = 1))\n",
    "y_plot = range(len(weathermean))\n",
    "years = list(range(2005, 2014, 1))\n",
    "weather.head()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "import matplotlib.pyplot as plt\n",
    "fig, ax1 = plt.subplots()\n",
    "\n",
    "\n",
    "COLOR = 'orange'\n",
    "ax1.set_ylabel('Normalized Mean Temp in MA Counties', color = COLOR)  \n",
    "ax1.bar(y_plot, MAmean, yerr = MAstd, color = COLOR)\n",
    "ax1.tick_params(axis='y', color = COLOR)\n",
    "ax1.set_xticks(range(len(years)), minor=False)\n",
    "ax1.set_xticklabels(years, fontdict=None, minor=False)\n",
    "\n",
    "ax2 = ax1.twinx()  # instantiate second axes that shares axis with ax1\n",
    "\n",
    "COLOR = 'brown'\n",
    "ax2.set_title(\"Cold Winters Do Not Directly Affect Lyme Disease\")\n",
    "ax2.set_xlabel('Year')\n",
    "ax2.set_ylabel('Mean Normalized Incidence/100K', color = COLOR)\n",
    "ax2.plot(weathermean, color = COLOR, linewidth = 5.0)\n",
    "ax2.tick_params(axis = 'y', labelcolor = COLOR)\n",
    "ax2.errorbar(range(len(years)), weathermean, yerr = weatherstd, ecolor = COLOR, fmt = 'none')\n",
    "\n",
    "plt.show()\n",
    "fig.savefig('Assignment.png')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# No futher statistical analysis was made as the trends of the weather and lyme disease incidence rate \n",
    "# clearly do not follow each other. "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}