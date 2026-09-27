import pandas as pd
import numpy as np

# Dataset containing missing values
data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit"],
    "Marks": [85, np.nan, 78, 92, np.nan],
    "Age": [20, 21, np.nan, 21, 20],
    "Branch": ["CSE", "CSE", "IT", np.nan, "IT"]
}

df = pd.DataFrame(data)

print("----- Original Dataset -----")
print(df)


# Identify missing values
print("\n----- Missing Values -----")
print(df.isnull())


# Count missing values
print("\n----- Missing Values Count -----")
print(df.isnull().sum())


# Remove rows containing missing values
removed_df = df.dropna()

print("\n----- After Removing Missing Rows -----")
print(removed_df)


# Fill missing values
filled_df = df.copy()

filled_df["Marks"] = filled_df["Marks"].fillna(
    filled_df["Marks"].mean()
)

filled_df["Age"] = filled_df["Age"].fillna(
    filled_df["Age"].mean()
)

filled_df["Branch"] = filled_df["Branch"].fillna("Unknown")

print("\n----- After Filling Missing Values -----")
print(filled_df)