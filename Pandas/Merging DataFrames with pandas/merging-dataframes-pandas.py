#-----------------------------------------------------------------------
# Course: Mergind DataFrames with Pandas
# Link: https://learn.datacamp.com/courses/merging-dataframes-with-pandas
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# Tools for pandas data import
#-----------------------------------------------------------------------
import pandas as pd
dataframe = pd.read_csv(filepath)
dataframe = pd.read_excel(filepath)
dataframe = pd.read_html(filepath)
dataframe = pd.read_json(filepath)

# Loading separate files - loop (1)
filenames = ['sales-jan-2015.csv', 'sales-feb-2015.csv']
dataframes = []
for f in filenames:
	dataframes.append(pd.read_csv(f))

# Loading separate files - loop (2)	
filenames = ['sales-jan-2015.csv', 'sales-feb-2015.csv']
dataframes = [pd.read_csv(f) for f in filenames]

# Loading separate files - loop/glob (3)
from glob import glob
filenames = glob('sales*.csv') # Match all files in the current directory 
dataframes = [pd.read_csv(f) for f in filenames]

# Making a copy
gold = pd.read_csv(path)
medals = gold.copy()