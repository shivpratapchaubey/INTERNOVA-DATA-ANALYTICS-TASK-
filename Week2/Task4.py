import pandas as pd

# Create a Pandas Series
marks = pd.Series([85, 90, 78, 92, 88])

print("Pandas Series:")
print(marks)


# Create DataFrame
data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit"],
    "Branch": ["CSE", "CSE", "IT", "CSE", "IT"],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("\nStudent DataFrame:")
print(df)


# Column names
print("\nColumn Names:")
print(df.columns)


# Index
print("\nIndex:")
print(df.index)


# Add a new column
df["Result"] = ["Pass", "Pass", "Pass", "Pass", "Pass"]

print("\nUpdated DataFrame:")
print(df)