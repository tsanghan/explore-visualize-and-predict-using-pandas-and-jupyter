# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %matplotlib inline 
import matplotlib
import numpy as np
import pandas as pd

# +
### Data transformation from previous notebooks
nyc = pd.read_csv('../data/central-park-raw.csv', parse_dates=[0])
# put it all in a function
def fix_col(colname):
    return colname.strip().replace(' ', '_')

def tweak_nyc(df_):
    return (df_
            .rename(columns=fix_col)
            .assign(PrecipitationIn = pd.to_numeric(df_.PrecipitationIn.replace("T", '0.001')),
                    Events=lambda df2: df2['Events'].fillna(''),
                    PrecipitationCm=lambda df2:df2.PrecipitationIn * 2.54)
           )

nyc = tweak_nyc(nyc)
nyc
# -

# # Basic Stats
#
# A nice feature of pandas is that you can quickly inspect data and get summary statistics.

# The describe method gives us basic stats. The result is a Data Frame
nyc.describe()

# Remember transpose
nyc.describe().T


# to view non-numeric data pass include='all'
nyc.describe(include='all').T

# Various aggregation methods (max, mean, median, min, mad, skew, kurtosis, autocorr,
#   nunique, sem, std, var)
# and properties (hasnans, is_monotonic, is_unique)
nyc.Max_Humidity.max()

nyc.Max_Humidity.quantile(.2)

nyc.Max_Humidity.quantile([.2,.3])

nyc.Max_Humidity.min()

nyc.Mean_Humidity.corr(nyc.Mean_TemperatureF)


# ## Load Lab Data
# https://archive.ics.uci.edu/ml/datasets/El+Nino

# +
def fix_nino_col(name):
    return name.rstrip('.').replace('.', '_').replace(' ', '_')
def tweak_nino(df_):
    return (df_
           .rename(columns=fix_nino_col)
           .assign(air_temp_F=lambda df2:df2.air_temp*9/5+32,
                   zon_winds_mph=lambda df2:df2.zon_winds / 2.237,
                   mer_winds_mph=lambda df2:df2.mer_winds / 2.237,
                   date=pd.to_datetime(df_.date, format='%y%m%d')
                  )
            .drop(columns='obs')
           )

names = '''obs
year
month
day
date
latitude
longitude
zon.winds
mer.winds
humidity
air temp.
s.s.temp.'''.split('\n')

nino = pd.read_csv('../data/tao-all2.dat.gz', sep=' ', names=names, na_values='.',
                  parse_dates=[[1,2,3]])

nino = tweak_nino(nino)
# -

# ## Basic Stats Exercise
# With the nino dataset:
#
# * *Describe* the data
# * Choose a column
#   * Print out the max, min, and mean
# * Correlate (``corr``) the temperature column with the date column (might need to use ``.astype('int64')`` method)

nino.describe()

nino.describe().T

nino.air_temp.agg(['max', 'min', 'mean'])

nino.date.corr(nino.air_temp)

nino.date.astype(int).corr(nino.air_temp)

(nino.date - nino.date.min()).dt.days.corr(nino.air_temp)

nino









# # Plotting
#
# Pandas has built-in integration with Matplotlib. Other libraries such as Seaborn also support plotting DataFrames and Series. This is not an in depth intro to Matplotlib, but their website and gallery are great for finding more information

# histograms are a quick way to visualize the distribution
nyc.Mean_Humidity.hist()

# Notice the output. Get rid of it by assigning to an "ignored" variable
_ = nyc.Mean_Humidity.hist()



# add in figsize=(width,height) to boost size
nyc.Mean_Humidity.hist(figsize=(8,6))

# If we use the .plot method we can add title and other attributes
nyc.Mean_Humidity.plot.hist(title='Avg Humidity', figsize=(8, 6))



nyc.plot(x='EST', y='Mean_Humidity')

nyc.plot(x='EST', y='Mean_Humidity', figsize=(12, 6) )

# Can resample columns, since our index is a date we can use *Offset Aliases*
# see https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases
nyc.set_index('EST').Mean_Humidity.resample('M').mean().plot(figsize=(10, 6)) 

# Can resample columns, since our index is a date we can use *Offset Aliases*
# see https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases
(nyc
 .set_index('EST')
 .Mean_Humidity
 .resample('M')
 .mean()
 .plot(figsize=(10, 6)) 
)

# Can resample columns, since our index is a date we can use *Offset Aliases*
# see https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases
(nyc
 .set_index('EST')
 .Mean_Humidity
 .resample('2W')
 .mean()
 .plot(figsize=(10, 6)) 
)

# Plot all the things (may be useful or just art)
nyc.set_index('EST').plot(figsize=(12,6))

nyc.plot.scatter(x='Max_TemperatureF', y='Max_Humidity', alpha=.5, 
        figsize=(10, 6))

nyc.Max_TemperatureF.corr(nyc.Max_Humidity)

# ## Plotting Exercise
# With the nino dataset:
# * Plot a histogram of air temp
# * Plot a scatter plot of latitude and longitude
#

nino.air_temp.plot.hist()

nino.air_temp.plot.hist()





# # Filtering

# +
# When we apply a conditional operator to a series we get back a series of True/False values
# We call this a "mask", which we can use to filter (similar to Photoshop)
# all EST in 2000's
m2000 = nyc.EST.dt.year >= 2000

# below 2010
lt2010 = nyc.EST.dt.year < 2010


# -

# The "and" operation looks at whether the operands are truthy or falsey
# This is a case where normal Python syntax doesn't work
nyc[m2000 and lt2010]

# & does bitwise comparisons - which is what we want
nyc[m2000 & lt2010]

# beware if you embed the operations, the bitwise operator binds more tightly to the integers
nyc[nyc.EST.dt.year >= 2000 & nyc.EST.dt.year < 2010]

# beware if you embed the operations, the bitwise operator binds more tightly to the integers
nyc[(nyc.EST.dt.year >= 2000) & (nyc.EST.dt.year < 2010)]

m_dec = nyc.EST.dt.month == 12
nyc[m_dec]

# Can use loc to filter out based on index value, also takes a boolean index
# In fact, you should use .loc instead as a matter of habit (you won't see warnings)
nyc.loc[m_dec]

# Can use loc to filter out based on index value, also takes a boolean index
# 2nd option in index op is column names (: to include everything)
nyc.loc[m_dec, [x for x in nyc.columns if 'Max' in x]]

# loc note:
# can use set_index and sort_index to do quick lookups (if you sort you get quick lookups)
nyc.set_index('Events').sort_index().head()

(nyc
 .set_index('Events')
 .sort_index()
 .loc['Fog']
)

# Can use iloc to filter out based on index location (or position)
# 2nd option in index op is column indices
nyc.iloc[5:10, [2, 5, -2]]  


# Can use iloc to filter out based on index location
# 2nd option in index op is column indices
nyc.iloc[:, [2, 5, -2]]  







# ## Filtering Exercise
# Using the nino dataframe:
# * Create a mask, ``m80``, that all years >= 1980 and < 1990
# * Create a mask, ``m90``, that all years >= 1990 and < 2000
# * Create a mask, ``lon120``, that has all longitudes > 120
# * Create a mask, ``lat0``, that has latitudes > -2 and < 2
# * Create a dataframe, ``df80``, that has only those values in ``m80`` and ``lon120`` and ``lat0``
# * Create a dataframe, ``df90``, that has only those values in ``m90`` and ``lon120`` and ``lat0``
#

m80 = (nino.date.dt.year >= 1980) & (nino.date.dt.year < 1990)
m90 = (nino.date.dt.year >= 1990) & (nino.date.dt.year < 2000)

lon120 = nino.longitude > 120
lat0 = (nino.latitude > -2) & (nino.latitude < 2)

df80 = nino[m80 & lon120 & lat0]
df90 = nino[m80 & lon120 & lat0]

nino.query('date.dt.year >= 1980 and date.dt.year < 1990 and longitude > 120 and latitude > -2 and latitude < 2')






# # Dealing with NaN

nyc.isna()

nyc.isna().any()

nyc.isna().any(axis=0)

# find rows that have null data
# fish create a mask
nyc.isna().any(axis=1)

# count missing trick
nyc.isna().sum()

# percent missing trick
nyc.isna().mean().mul(100)

nyc[nyc.isna().any(axis=1)]

missing_df = nyc.isna() 
nyc[missing_df.Max_TemperatureF]

nyc.loc[2218:2221]

nyc.Max_TemperatureF.fillna(nyc.Max_TemperatureF.mean()).loc[2218:2221]

# The .interpolate method will do linear interpolation by default
nyc.Max_TemperatureF.interpolate().loc[2218:2221]

# forward fill
nyc.Max_TemperatureF.ffill().loc[2218:2221]

# forward fill
nyc.Max_TemperatureF.bfill().loc[2218:2221]

# tack on a plot to visualize
nyc.Max_TemperatureF.bfill().loc[2218:2221].plot()

#dropping rows with missing data
nyc.dropna()



# ## Dealing with NaN Exercise
# With the nino dataset:
# * Find the rows that have null data
# * Find the columns that have null data
# * It looks like the ``zon_winds`` has some missing values, use summary stats or plotting to determine how to fill in those values

nino.isna().any(axis=1)


nino.isna().any(axis=0)


nino.isna().mean(axis=0).mul(100)


nino[nino.isna().zon_winds]

nino.isna().corr().style.background_gradient(cmap='RdBu', vmin=-1, vmax=1)

nino.corr().style.background_gradient(cmap='RdBu', vmin=-1, vmax=1)

nino.plot.scatter(x='mer_winds', y='air_temp', alpha=.1)

(nino
 .sample(2000)
 .plot.scatter(x='mer_winds', y='air_temp', alpha=.1)
)

nino.zon_winds.hist()

nino.zon_winds.fillna(nino.zon_winds.median()).hist()



# # Grouping
#
# Pandas allows us to perform aggregates calculations over grouped portions of ``Series`` or ``DataFrames``. The ``.groupby`` method is the low level workhorse that enables this.

# We can group by a column, but if it has unique values it isn't useful
nyc.groupby('EST').mean()['CloudCover']

# We can group by a column, but if it has unique values it isn't useful
(nyc
 .groupby('EST')
 .mean()
 ['CloudCover']
)

# Let's get the average cloud cover each month
(nyc
 .groupby(nyc.EST.dt.month)
 .mean()
 ['CloudCover']
)

# The previous aggregated over every month, 
# what if we want to group by year and month?
(nyc
 .groupby([nyc.EST.dt.year, nyc.EST.dt.month])
 .mean()
 ['CloudCover']
)

# The previous aggregated over every month, 
# what if we want to group by year and month?
(nyc
 .groupby([nyc.EST.dt.year, nyc.EST.dt.month])
 .mean()
 ['CloudCover']
 .plot()
)

# To fix date/index can use grouper
(nyc
 .groupby(pd.Grouper(key='EST', freq='M'))
 .mean()
 ['CloudCover']
 .plot()
)

# With the .agg method we can apply many functions
(nyc
 .groupby(pd.Grouper(key='EST', freq='M'))
 .agg(['mean', 'max', 'count'])
)

# Pull out a column
(nyc
 .groupby(pd.Grouper(key='EST', freq='M'))
 .agg(['mean', 'max', 'count'])
 .Mean_TemperatureF
)

# Then Plot
(nyc
 .groupby(pd.Grouper(key='EST', freq='M'))
 .agg(['mean', 'max', 'count'])
 .Mean_TemperatureF
 .plot()
)





# ## Grouping Exercise
# With the nino dataset:
# * Find the mean temperature for each year
# * Find the count of entries for each year
# * Find the max temperature for each year

nino.groupby(nino.date.dt.year).air_temp.mean()

nino.groupby(nino.date.dt.year).air_temp.mean().plot()

nino.groupby(nino.date.dt.year).size()

nino.groupby(nino.date.dt.year).air_temp.max()



# # Pivoting

nyc.pivot_table(index=[nyc.EST.dt.year.rename('year'), nyc.EST.dt.month],
                aggfunc=[np.max, np.count_nonzero],
               values=['Max_Humidity', 'Max_Dew_PointF'])

nyc.pivot_table(index=[nyc.EST.dt.year.rename('year'), nyc.EST.dt.month],
                aggfunc=[np.max, np.count_nonzero],
               values=['Max_Humidity', 'Max_Dew_PointF']).plot(figsize=(14,6))

# Fix x-axis with grouper
nyc.pivot_table(index=pd.Grouper(key='EST', freq='m'), #[nyc.EST.dt.year.rename('year'), nyc.EST.dt.month],
                aggfunc=[np.max, np.count_nonzero],
               values=['Max_Humidity', 'Max_Dew_PointF']).plot(figsize=(14,6))

# Back to multi-index....
# We can "unstack" to pull a left index into a column (0 is the left most index)
(nyc
 .pivot_table(index=[nyc.EST.dt.year.rename('year'), nyc.EST.dt.month], 
              aggfunc=[np.max, np.count_nonzero],
              values=['Max_Humidity', 'Max_Dew_PointF'])
 .unstack(0)
)

# We can "unstack" to pull a left index into a column (1 is the 2nd index)
(nyc
 .pivot_table(index=[nyc.EST.dt.year.rename('year'), nyc.EST.dt.month], 
              aggfunc=[np.max, np.count_nonzero],
              values=['Max_Humidity', 'Max_Dew_PointF'])
 .unstack(1)
)

# Just use one value and one aggregation
(nyc
 .pivot_table(index=[nyc.EST.dt.year.rename('year'), nyc.EST.dt.month], 
              aggfunc=np.max,
              values='Mean_TemperatureF')
 .unstack(1)
)

# Just use one value and one aggregation
(nyc
 .pivot_table(index=[nyc.EST.dt.year.rename('year'), nyc.EST.dt.month], 
              aggfunc=np.max,
              values='Mean_TemperatureF')
 .unstack(1)
 .plot(cmap='jet', figsize=(10,6))
)

# Just use one value and one aggregation
(nyc
 .pivot_table(index=[nyc.EST.dt.year.rename('year'), nyc.EST.dt.month], 
              aggfunc=np.max,
              values='Mean_TemperatureF')
 .unstack(0)
 .plot(cmap='viridis', figsize=(10,6))
)

# ## Pivoting Exercise
# With the nino dataset:
# * Pivot the nino data using the ``.pivot_table`` method. Group by year and month, the ``air_temp`` column. Reduce using the ``max``, ``min``, and ``np.mean`` functions. (You will either need to create a month column or use ``year_month_day.dt.month``)
# * Plot a line plot of the previous pivot table

nino.pivot_table(index=[nino.date.dt.year, nino.date.dt.month], aggfunc=[np.max, 'min', np.mean], values='air_temp')

(nino
 .pivot_table(index=[nino.date.dt.year, nino.date.dt.month], aggfunc=[np.max, 'min', np.mean], values='air_temp')
 .plot()
)

# fix x-axis
(nino
 .pivot_table(index=pd.Grouper(key='date', freq='m'), aggfunc=[np.max, 'min', np.mean], values='air_temp')
 .plot()
)





# ## Pivoting Bonus Exercise
#
# * Using ``.groupby`` we can sometimes perform the same operation as pivot tables. Pivot the nino data using the ``.groupby`` method. Group by year and month, the ``air_temp_`` column. Reduce using the ``max``, ``min``, and ``np.mean`` functions using ``.groupby``. (Hint: Use the ``.agg`` method on the result of the group by)
# * Use ``.unstack`` to see the mean ``air_temp_`` by year

(nino
 .groupby([nino.date.dt.year, nino.date.dt.month])
 .air_temp
 .agg(['max', 'min', np.mean])
 )

(nino
 .groupby([nino.date.dt.year, nino.date.dt.month])
 .air_temp
 .agg(['max', 'min', np.mean])
 .unstack()
 ['mean']
 )

(nino
 .groupby([nino.date.dt.year, nino.date.dt.month])
 .air_temp
 .agg(['max', 'min', np.mean])
 .unstack()
 ['mean']
 .plot(cmap='viridis')
 )









