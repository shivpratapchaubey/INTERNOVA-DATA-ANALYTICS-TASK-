import pandas as pd

data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit"],
    "Branch": ["CSE", "CSE", "IT", "CSE", "IT"],
    "Marks": [85, 90, 78, 92, 88],
    "Age": [20, 21, 20, 21, 20]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# Select specific columns
print("\n----- Selected Columns -----")
print(df[["Name", "Marks"]])


# Select specific rows
print("\n----- Selected Rows -----")
print(df.iloc[0:3])


# Filter students with marks greater than 85
print("\n----- Marks Greater Than 85 -----")
print(df[df["Marks"] > 85])


# Multiple filtering conditions
print("\n----- CSE Students With Marks > 85 -----")

filtered = df[
    (df["Branch"] == "CSE") &
    (df["Marks"] > 85)
]

print(filtered)


# Sort ascending
print("\n----- Marks Ascending -----")
print(df.sort_values("Marks"))


# Sort descending
print("\n----- Marks Descending -----")
print(df.sort_values("Marks", ascending=False))