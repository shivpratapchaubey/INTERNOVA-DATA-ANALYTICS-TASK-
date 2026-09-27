import pandas as pd

# First DataFrame
students1 = pd.DataFrame({
    "Student_ID": [101, 102, 103],
    "Name": ["Rahul", "Aman", "Priya"],
    "Branch": ["CSE", "CSE", "IT"]
})

# Second DataFrame
marks = pd.DataFrame({
    "Student_ID": [101, 102, 103],
    "Marks": [85, 90, 78]
})

print("----- Students DataFrame -----")
print(students1)

print("\n----- Marks DataFrame -----")
print(marks)


# MERGE
merged_df = pd.merge(
    students1,
    marks,
    on="Student_ID"
)

print("\n----- Merged DataFrame -----")
print(merged_df)


# CONCATENATE
df1 = pd.DataFrame({
    "Name": ["Rahul", "Aman"],
    "Marks": [85, 90]
})

df2 = pd.DataFrame({
    "Name": ["Priya", "Neha"],
    "Marks": [78, 92]
})

concatenated_df = pd.concat(
    [df1, df2],
    ignore_index=True
)

print("\n----- Concatenated DataFrame -----")
print(concatenated_df)


# GROUPBY
grouped = merged_df.groupby("Branch")["Marks"].mean()

print("\n----- Average Marks by Branch -----")
print(grouped)


# Aggregate values
aggregation = merged_df.groupby("Branch")["Marks"].agg(
    ["sum", "mean", "count", "min", "max"]
)

print("\n----- GroupBy Aggregation -----")
print(aggregation)


# PIVOT TABLE
pivot = pd.pivot_table(
    merged_df,
    values="Marks",
    index="Branch",
    aggfunc="mean"
)

print("\n----- Pivot Table -----")
print(pivot)