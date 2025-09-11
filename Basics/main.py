# importing pandas library as pd
import pandas as pd

# reading the csv file /loading the csv file
df = pd.read_csv("myntra.csv")

# printing the last 5 rows of the dataframe using tail() func
print(df.tail())

# printing the first 2 rows of the dataframe using head() func
print(df.head(2))

# gives info / overview od all features 
print(df.info())

# describe the table in short
print(df.describe())