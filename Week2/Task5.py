import pandas as pd

# Read CSV file
df = pd.read_csv("students.csv")

# First 5 rows
print("----- First 5 Rows -----")
print(df.head())

# Last 5 rows
print("\n----- Last 5 Rows -----")
print(df.tail())

# Number of rows and columns
print("\nShape of Dataset:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns)

# Data types
print("\nData Types:")
print(df.dtypes)

# Dataset information
print("\n----- Dataset Information -----")
df.info()

# Statistical description
print("\n----- Statistical Description -----")
print(df.describe())