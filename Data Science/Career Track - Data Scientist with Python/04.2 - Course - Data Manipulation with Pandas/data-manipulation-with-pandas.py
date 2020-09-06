#----------------------------------------------------------------------
# Course: Data Manipulation with pandas
# Link: https://campus.datacamp.com/courses/data-manipulation-with-pandas/
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# DataFrame methods and variables
#----------------------------------------------------------------------
import pandas as pd

print(dogs) # DataFrame
dogs.head()	# Return first few rows of the DataFrame
dogs.info() # Display the names of the columns and data types
dogs.shape  # Show the structure in a pair (rows, columns)
dogs.describe() # Show numerical statistics abou the DataFrame
dogs.values	# Show the contents of the DataFrame in array format 
dogs.columns # Show the names of the columns
dogs.index 	# Show row numbers or row names
dogs.sample(3) # Gives a random sample of 3 rows

# There should be one -- and preferably only one -- obvious way to do it.
# - The Zen of Python by Tim Peters, Item 13

#----------------------------------------------------------------------
# Sorting
#----------------------------------------------------------------------
dogs.sort_values("weight_kg") # Sort by column "weight_kg"
dogs.sort_values("weight_kg", ascending=False) # Sort by column "weight_kg" from heaviest to lightest dog

dogs.sort_values(["weight_kg", "height_cm"]) # Sort by column "weight_kg" and them by "height_cm"
dogs.sort_values(["weight_kg", "height_cm"], ascending=[True, False]) # Sort by column "weight_kg" (ascending) and them by "height_cm" (descending)

#----------------------------------------------------------------------
# Subsetting / Selecting columns
#----------------------------------------------------------------------
dogs["breed"] # Show column "breed"
dogs[["breed", "height_cm"]] # Show columns "breed" and "height_cm"

columns_selection = ["breed", "height_cm"]
dogs[columns_selection] # Show columns "breed" and "height_cm"

#----------------------------------------------------------------------
# Subsetting rows
#----------------------------------------------------------------------
dogs["height_cm"] > 50 # Return True or False for each element in height_cm
dogs[dogs["height_cm"] > 50] # Show only the dogs taller than 50 cm
dogs[dogs["breed"] == "Labrador"] # Show only Labrador dogs
dogs[dogs["date_of_birth"] > "2015-01-01"] # Show only dogs born after the infomed date

is_lab = dogs["breed"] == "Labrador"
is_brown = dogs["color"] == "Brown"
dogs[is_lab & is_brown] # Only Labrador brown dogs
dogs[ (is_lab = dogs["breed"]) & (is_brown = dogs["color"]) ] # Only Labrador brown dogs

is_black_or_brown = dogs["color"].isin(["Black", "Brown"])
dogs[is_black_or_brown] # Show onlye black and brown dogs

#----------------------------------------------------------------------
# New columns / Adding a new column
#----------------------------------------------------------------------
dogs["height_m"] = dogs["height_cm"] / 100

#----------------------------------------------------------------------
# Summary statistics
#----------------------------------------------------------------------
dogs["height_cm"].mean()
dogs["height_cm"].median()
dogs["height_cm"].mode()
dogs["height_cm"].min()	# smallest dog
dogs["height_cm"].max() # heighest dog
dogs["height_cm"].var()
dogs["height_cm"].std()	# Desvio padrão
dogs["height_cm"].sum()
dogs["height_cm"].quantile()

def pct30(column):
	return column.quantile(0.3)
def pct40(column):
	return column.quantile(0.4)
dogs["weight_kg"].agg(pct30)	# Return the 30th percentile of the dogs weights
dogs["weight_kg"].agg([pct30, pct40])		# Return the 30th and 40th percentile of the dogs weights
dogs["weight_kg"].agg([pct30, np.median])	# Return the 30th and median of the dogs weights
dogs[["weight_kg", "height_cm"]].agg(pct30)

dogs["height_cm"].cumsum() # Cumulative sum
dogs["height_cm"].cummax() 
dogs["height_cm"].cummin() 
dogs["height_cm"].cumprod() 

#----------------------------------------------------------------------
# Summarize categorical data - Counting
#----------------------------------------------------------------------
vet_visits.drop_duplicates(subset="name") # Filter data showing only onde occurency for unique name in column "name"

unique_dogs = vet_visits.drop_duplicates(subset=["name", "breed"])
unique_dogs["breed"].value_counts() # Count the number of dogs for each breed
unique_dogs["breed"].value_counts(sort=True) # Count the number of dogs for each breed, show the result sorted in descending order
unique_dogs["breed"].value_counts(normalize=True) # Show the counting into proportions of the total
unique_dogs["breed"].value_counts(sort=True, normalize=True)


#----------------------------------------------------------------------
# Grouped summary statistics 
#----------------------------------------------------------------------
dogs[dogs["color"] == "Black"]["weight_cm"].mean()	# Mean weight of black dogs

dogs.grouby("color")["weight_kg"].mean()	# Returns the mean weight for each dog color
dogs.groupby("color")["weight_kg"].agg([min, max, sum])
dogs.groupby(["color", "breed"])["weight_kg"].mean()
dogs.groupby(["color", "breed"])[["weight_kg", "height_cm"]].mean()

airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum() # Show multiple columns 

import numpy as np
sales_stats = sales.groupby("type")["weekly_sales"].agg([np.min, np.max, np.mean, np.median]) # For each store type, aggregate weekly_sales: get min, max, mean, and median
unemp_fuel_stats = sales.groupby("type")[["unemployment", "fuel_price_usd_per_l"]].agg([np.min, np.max, np.mean, np.median])


#----------------------------------------------------------------------
# Pivot Tables - Alternative way to group by
#----------------------------------------------------------------------
dogs.pivot_table(values="weight_kg", index="color")	# Value columns is the values to summarize, and index is the column to group by

import numpy as np
dogs.pivot_table(values="weight_kg", index="color", aggfunc=np.median)
dogs.pivot_table(values="weight_kg", index="color", aggfunc=[np.median, np.mean])

dogs.pivot_table(values="weight_kg", index="color", columns="breed") # group by columns "color" and "breed"
dogs.pivot_table(values="weight_kg", index="color", columns="breed", fill_value=0) # Missing values are filled with 0
dogs.pivot_table(values="weight_kg", index="color", columns="breed", fill_value=0, margins=True) # Add extra column with the mean for each row


#----------------------------------------------------------------------
# Explicit indexes
#----------------------------------------------------------------------
dogs.columns
dogs.index
dogs_ind = dogs.set_index("name") # Set column as index
dogs_ind.reset_index() 
dogs_ind.reset_index(drop=True) # Remove a coluna de índice

# Accessing values
dogs[dogs["name"].isin(["Bella", "Stella"])] # One way of doing it

dogs_ind = dogs.set_index("name") # Second way of doing it
dogs_ind.loc[["Bella", "Stella"]] # Show only fdgs "Bella" and "Stella"

dogs_ind2 = dogs.set_index("breed")
dogs_ind2.loc["Labrador"] # Show only Labrador dogs

dogs_ind3 = dogs.set_index(["breed", "color"]) # Creates indexes with multiple values
dogs_ind3.loc[["Labrador", "Chihuahua"]] # Subset just the first level of indexes
dogs_ind3.loc[[("Labrador", "Brown"), ("Chihuahua", "Tan")]] # Subset registries in both levels if indexes
dogs_ind3.sort_index()
dogs_ind3.sort_index(level="breed") # Sort by level "breed"
dogs_ind3.sort_index(level=["color", "breed"], ascending=[True, False])


#----------------------------------------------------------------------
# Slicing and subsetting with .loc and .iloc
#----------------------------------------------------------------------

# Sort the index before slicing
dogs_srt = dogs.set_index(["breed", "color"]).sort_index()
dogs_srt.loc["Chow Chow":"Poodle"] # Does slicing on the outer index level ("breed") - Poodle is included in the results

dogs_srt.loc["Tan":"Grey"] # Returns empty result. Does not slice inner index level
dogs_srt.loc[("Labrador", "Brown"):("Schnauzer", "Grey")] # To slice inner index level it's necessary the use of tuples, including outer level index

# Slicing columns
dogs_srt.loc[:, "name":"height_cm"]

# Examples
dogs = dogs.set_index("date_of_birth").sort_index() # Date of brith is index
dogs.loc["2014":"2016"] # Partial slicing the index also works. SLice from 2014 to 2015

# Use of iloc
dogs.iloc[2:5, 1:4] 

#----------------------------------------------------------------------
# Working with pivot tables
#----------------------------------------------------------------------

dogs_height_by_breed_vs_color = dog_pack.pivot_table("height_cm", index="breed", columns="color")
dogs_height_by_breed_vs_color.loc["Chow Chow":"Poodle"] # Using loc

dogs_height_by_breed_vs_color.mean(axis="index")
dogs_height_by_breed_vs_color.mean(axis="columns")

# Example 1
# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c", index=["country", "city"], columns="year")

# Example 2
# Subset in both directions at once
temp_by_country_city_vs_year.loc[("Egypt", "Cairo"):("India", "Delhi"), "2005":"2010"]

# Example 3
# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean(axis="index")

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()]) 


#----------------------------------------------------------------------
# Visualizing data
#----------------------------------------------------------------------
import matplotlib.pyplot as plt

# Bar plot
dog_pack["height_cm"].hist(bins=10)
dogs_pack[["height_cm", "weight_kg"]].hist() # Plot histogram for multiple variables
plt.show()

avg_weight_by_breed = dog_pack.groupby("breed")["weight_kg"].mean()
avg_weight_by_breed.plot(kind="bar", title="Mean Weight by Dog Breed")
plt.show()

# Line plot
sully.plot(x="date", y="weight_kg", kind="line") 
sully.plot(x="date", y="weight_kg", kind="line", rot=45) # Rotate 45º the x axis labels for better reading
plt.show()

# Scatter plot
dog_pack.plot(x="height_cm", y="weight_kg", kind="scatter")

# Layering plots
dog_pack[dog_pack["sex"]=="F"]["height_cm"].hist(alpha=0.7)
dog_pack[dog_pack["sex"]=="M"]["height_cm"].hist(alpha=0.7) # Alpha to make layers translucid
plt.legend(["F", "M"])	# Add label for each color
plt.show()


#----------------------------------------------------------------------
# Missing Values
#----------------------------------------------------------------------
dogs.isna() # Check for missing values. True for missing values
dogs.isna().any() # True if there is any missing values in that column
dogs.isna().sum() # Show the number of missing values per column

import matplotlib.pyplot as plt
dogs.isna().sum().plot(kind="bar")
plt.show()

dogs.dropna() # Remove the rows that have missing values
dogs.fillna(0) # Fill missing values with zero


#----------------------------------------------------------------------
# Creating DataFrames
#----------------------------------------------------------------------
# Create dictionary
my_dict = {
	"key1": value1,
	"key2": value2,
	"key3": value3
}
print(my_dict["key1"]) # Show value "value1"

# Create list of dictionaries by row
list_of_dicts = [
	{"name": "Ginger", "breed": "Dachshund", "height_cm": 22,
		"weight_kg": 10, "date_of_birth": "2019-03-14"},
	{"name": "Scout", "breed": "Dalmatian", "height_cm": 59,
		"weight_kg": 25, "date_of_birth": "2019-05-09"} # Each row is a dictionary
]
new_dogs = pd.DataFrame(list_of_dicts)
print(new_dogs)

# Create dictionary of lists by column
dict_of_lists = {
	"name": ["Ginger", "Scout"],
	"breed": ["Dachshund", "Dalmatian"],
	"height_cm": [22, 59],
	"weight_kg": [10, 25],
	"date_of_birth": ["2019-03-14",
	"2019-05-09"]
}
new_dogs = pd.DataFrame(dict_of_lists)


#----------------------------------------------------------------------
# Reading and writing CSVs
#----------------------------------------------------------------------

# Input: new_dogs.csv
name,breed,height_cm,weight_kg,d_o_b
Ginger,Dachshund,22,10,2019-03-14
Scout,Dalmatian,59,25,2019-05-09

# Reading CSV file
import pandas as pd
new_dogs = pd.read_csv("new_dogs.csv")

# Writing CSV file
new_dogs["bmi"] = new_dogs["weight_kg"] / (new_dogs["height_cm"] / 100) ** 2
new_dogs.to_csv("new_dogs_with_bmi.csv")

# Output: new_dogs_with_bmi.csv
name,breed,height_cm,weight_kg,d_o_b,bmi
Ginger,Dachshund,22,10,2019-03-14,206.611570
Scout,Dalmatian,59,25,2019-05-09,71.818443















