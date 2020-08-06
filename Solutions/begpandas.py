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

# # Explore, Visualize, and Predict using Pandas & Jupyter
#
# ### Learn to import, explore, and tweak your data
#
# Matt Harrison (@\_\_mharrison\_\_)
#
# The pandas library is very popular among data scientists, quants, Excel junkies, and Python developers because it allows you to perform data ingestion, exporting, transformation, and visualization with ease. But if you are only familiar with Python, pandas may present some challenges. Since pandas is inspired by Numpy, its syntax conventions can be confusing to Python developers.
#
# If you have questions on Python syntax, check out https://github.com/mattharrison/Tiny-Python-3.8-Notebook
#
# Much of this content is based on my Pandas books:
# * [*Learning the Pandas Library*](https://www.amazon.com/Learning-Pandas-Library-Munging-Analysis/dp/153359824X/ref=sr_1_3?ie=UTF8&qid=1505448275&sr=8-3&keywords=python+pandas)
# * *Pandas 1.x Cookbook*



# # Jupyter Intro
#
# Jupyter notebook is an environment for combining interactive coding and text in a webbrowser. This allows us to easily share code as well as narrative around that code. An example that was popular in the scientific community was [the discovery of gravitational waves.](https://losc.ligo.org/s/events/GW150914/GW150914_tutorial.html)
#
# The name Jupyter is a rebranding of an open source project previously known as iPython Notebook. The rebranding was to emphasize that although the backend is written in Python, it supports various *kernals* to run other languages, including Julia (the "Ju" portion), Python ("pyt"), and R ("er"). All popular *data science* programming languages.
#
# The architecture of Jupyter includes a server running various kernals. Using a *notebook* we can interact with a kernal. Typically we use a webbrowser to do this, but there are other iterfaces, such as an emacs mode (ein).
#
# ## Using Jupyter
#
# After we create a notebook, we are presented with a page with an empty cell. The cell will have a blue outline, ane the text:
#
#     In [ ]: 
#     
# on the side. The blue outline indicates that we are in *command mode*. There are two modes in Jupyter, command mode and *edit mode*.
#
# To enter edit mode simply hit the enter or return key. You will notice that the outline will change to green. In edit mode, with a Python kernel, we can type Python code. Type:
#
#     print("hello world")
#     
# You will notice that unlike a normal Python REPL, this will note print anything after hitting return again. To *execute* the cell, you need to hold down control and hit enter (``C-Enter``). This will run the code, print the results of the cell and put you back into edit mode.     
#
# ## Edit Mode
#
# To enter *Edit Mode* you need to click on a cell or hit enter when it is surrounded by the blue outline. You will see that it goes green if you are in edit mode. In edit mode you have basic editing functionality. A few keys to know:
#
# * Ctr-Enter - Run cell (execute Python code, render Markdown)
# * ESC - Go back to command mode
# * TAB - Tab completion
# * Shift-TAB - Bring up tooltip (ESC to dismiss)
#
#
# ## Command Mode
#
# *Command Mode* gives to the ability to create, copy, paste, move, and execute cells. A few keys to know:
#
# * h - Bring up help (ESC to dismiss)
# * b - Create cell below
# * a - Create cell above
# * c - Copy cell
# * v - Paste cell below
# * Enter - Go into Edit Mode
# * m - Change cell type to Markdown
# * y - Change cell type to code
# * ii - Interrupt kernel
# * 00 - Restart kernel
#
# ## Cell Types
#
# * Code
# * Markdown
#
#
# ## Markdown
#
# Can make *italicized*, **bold**, and ``monospaced text``:
#
#     Can make *italicized*, **bold**, and ``monospaced text``
#
#
# Headers:
#
#     # H1
#     ## H2
#     ### H3
#  
# Lists:
#
#     * First item
#     * Second item
#     
# Code:
#
#     If you indent by four spaces you have code:
#     
#         def add(x, y):
#             return x + yt
#     
# ## Cell Magic
#
# type and run ``%lsmagic`` in a cell.
#
# Common magics include:
#
# * ``%%time`` - time how long it takes to run cell
# * ``%matplotlib inline`` - show matplotlib plots
#
#
# ## IPython Help
# Add ? after function, method, etc for documentation (can also run shift-tab 4 times in notebook). Add ?? after function, method, etc to see the source.

# # Setup

# +
import pandas as pd
import matplotlib
import numpy as np

pd.__version__, matplotlib.__version__, np.__version__
# -

# test for unicode
'\N{SNAKE}'

import sys
sys.getdefaultencoding() 

sys.version

# # Pandas Intro
#
# ## Installation
#
# Presumably, you have pandas installed if you ran the cell after **Setup** successfully. The Anaconda distribution is a common way to get the Python scientific stack up and running quickly on most platforms. Running ``pip install pandas`` works as well.

# +
# pandas has two main datatypes: a Series and a DataFrame
# A Series is like a column from a spreadsheet

s = pd.Series([0, 4, 6, 7])

# +
# A DataFrame is like a spreadsheet

df = pd.DataFrame({'name': ['Fred', 'Johh', 'Joe', 'Abe'], 'age': s})
# -

# We can do tab completion on objects that exist (shift tab brings up tooltip)
# ?? brings up source
df.

# # Datasets
#
# For this class we will look at some time series data. The class will look at Central Park weather. The assignments will deal with El Nino data.
#
# ## Central Park
#
#
# https://pastebin.com/vaB6QQGp
#
# ## El Nino
#
# https://archive.ics.uci.edu/ml/datasets/El+Nino

# %matplotlib inline
# I typically start with imports like this including the matplotlib magic 
# for most notebooks
import pandas as pd
import numpy as np 

# # Getting Data
# There are various ``pd.read_`` functions for ingesting data

# not necessary if you started jupyter from the project directory
# %ls ../data/
# should have central-park-raw.csv

# +
# if you execute this cell it will bring up a tooltip due to
# the ? at the end. You can also hit shift-tab 4 times
# if your cursor is after the v
# Hit escape to dismiss the tooltip
# pd.read_csv?
# -

# let's load the data and treat column 0 as a date
nyc = pd.read_csv('../data/central-park-raw.csv', parse_dates=[0])
# Jupyter will print the result of the last command
nyc

# dataframes can get big, so only show the first bit
nyc.head()

# ## Getting Data Exercise
#
# For your assignment, you will look at El Nino data.
#
# The [website](https://archive.ics.uci.edu/ml/datasets/El+Nino)  states:
#
#     The data is stored in an ASCII files with one observation per line. Spaces separate fields and periods (.) denote missing values.
#
# * Create a ``nino`` variable with the data from the ``../data/tao-all2.dat.gz`` file (use ``pd.read_csv``)
# * Use the ``names`` variable for the initial column names (taken from website). They are:
#
#  * obs
#  * year
#  * month
#  * day
#  * date 
#  * latitude
#  * longitude
#  * zon.winds
#  * mer.winds
#  * humidity
#  * air temp.
#  * s.s.temp.
#
# * Replace empty values (``.``) with ``NaN``. 
# * Pull the year, month, and date columns into a single variable using the ``parse_dates`` parameter (see the ``pd.read_csv`` docs for info on this).
#
# FYI, zonal winds are along east/west axis. Meridonal winds are north/south.

# +
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
nino
# -



# # Inspecting Data

# Interesting aside, the columns are actually an Index 
nyc.columns

# If is good to know if columns have a [correct] type, (object could mean string)
nyc.dtypes

# we can also see how much space is taken up
nyc.info()

# just view the first 10 rows
nyc.head(10)

# a better option might be sampling
nyc.sample(10)

# Transposing the data often makes it easier to view
nyc.T  # nyc.transpose()

# Here is the size (num rows, num cols)
nyc.shape

# We can inspect the index
nyc.index

# We can use the .set_index method to use another column as the index
nyc.set_index('EST')

# undo .set_index with .reset_index
nyc.set_index('EST').reset_index()

# I would prefer to write the last one like
(nyc
 .set_index('EST')
 .reset_index()
)

# ## Inspecting Data Exercise
#
# Now it is your turn to inspect the El Nino data.
#  
# * What are the columns of the dataframe?
# * What are the types of the columns?
# * How would you print the first 10 rows of data?
# * How would you transpose the data?
# * What is the shape of the data?
# * How would we inspect the index?

nino.columns

nino.dtypes

nino.head(10)

nino.head().T

nino.shape

nino.index



# # Tweak Data
#
#   *In Data Science, 80% of time spent prepare data, 20% of time spent complain about need for  prepare data.*
#   
#   -@bigdataborat
#   
# Let's see how we spend 80% of our time.  
#

# I like to start by inspecting the columns. Pandas will try to 
# infer types from CSV files, but doesn't always do the right thing.
# Sometimes the data is just messy.
nyc.dtypes


# See those spaces in front of some of the Columns?
# Remove spaces from front/end of column names
# Use underscores to enable attribute access/jupyter completion
# We are going to use methods that return dataframes
def fix_col(colname):
    return colname.strip().replace(' ', '_')
nyc.rename(columns=fix_col)

# For non-numeric columns, .value_counts gives us 
# counts of the data. One would think that 
# PrecipitationIn should be numeric....
nyc.PrecipitationIn.value_counts()

# There is a "T" in there. Trace? 
# Convert "T" to 0.001
nyc.PrecipitationIn.replace("T", '0.001')

# Convert to numeric data
nyc.assign(PrecipitationIn = pd.to_numeric(nyc.PrecipitationIn.replace("T", '0.001')))

nyc[' Events'].value_counts()

# can perform string operations on string columns off of the "str" attribute
nyc[' Events'].str.upper()

# Looks like the type of this column is mixed
type(nyc[' Events'][0])

set(nyc[' Events'].apply(type))

# Replace nan with ''
nyc.assign(**{' Events': nyc[' Events'].fillna('')})

# Replace nan with ''
(nyc
 .assign(**{' Events': nyc[' Events'].fillna('')})
 .dtypes)

# convert inches to cm
# If we multiply a column (Series), we are *broadcasting*
# the operation to every cell
nyc.PrecipitationIn * 2.54


# convert PrecipitationIn
nyc2 = (nyc.assign(PrecipitationIn = pd.to_numeric(nyc.PrecipitationIn.replace("T", '0.001'))))

# +
# can also apply an arbitrary function, though this will be slow as it is not vectorized
#   map - works with a dictionary (mapping value to new value),  series (like dict), function
#   apply - only works with function as a parameter. Allows extra parameters
#   aggregate (agg) - works with function or list of functions. If reducing function, returns a scalar.
#   transform - wraps agg and won't do a reduction
def to_cm(val):
    return val * 2.54

nyc2.PrecipitationIn.transform(to_cm)

# -

# %%timeit
nyc2.map(to_cm)

# %%timeit
nyc2.PrecipitationIn.transform(to_cm)

# %%timeit
nyc2.PrecipitationIn*2.54

# can add and drop columns (axis=1 means along the columns axis)
# Note that we can access some columns with attribute access
# We can only set w/ attribute access on an existing column!
(nyc
 .assign(State='NYC')
 .drop(['State'], axis=1)
)


# +
# Prefer to write .drop like this
(nyc
 .assign(State='NYC')
 .drop(columns=['State'])
 
)

# -

# can use pd.to_datetime to convert a column to a datetime
date_str = nyc.EST.astype(str)
pd.to_datetime(date_str)



# +
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

nyc2 = tweak_nyc(nyc)
nyc2


# -

# ## Tweak Data Exercise
# With the nino dataset make a `tweak_nino` dataset that:
# * Replace the periods and spaces in the column names with underscores
# * The temperatures are stored as Celsius. Create a new column, ``air_temp_F``, using Fahrenheit
#   (Tf = Tc*9/5 + 32)
# * The wind speed is in meters per second. Create new columns,  adding ``_mph``, that uses miles per hour ( 1 MPS = 2.237 MPH )
# * Convert the ``date`` column to a date type.
# * Drop the obs column

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

tweak_nino(nino)
# -


