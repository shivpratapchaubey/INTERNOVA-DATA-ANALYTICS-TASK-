import pandas as pd
import numpy as np

# ---------------------------------------
# STEP 1: Create Dataset
# ---------------------------------------

data = {
    "Name": [
        "Rahul", "Aman", "Priya", "Neha",
        "Rohit", "Anjali", "Vikas", "Pooja",
        "Karan", "Sneha"
    ],

    "Branch": [
        "CSE", "CSE", "IT", "CSE",
        "IT", "CSE", "IT", "CSE",
        "IT", "CSE"
    ],

    "Gender": [
        "Male", "Male", "Female", "Female",
        "Male", "Female", "Male", "Female",
        "Male", "Female"
    ],

    "Marks": [
        85, 90, 78, np.nan,
        88, 95, 72, 91,
        np.nan, 87
    ],

    "Attendance": [
        90, 95, 85, 88,
        92, 96, 80, 94,
        82, 91
    ]
}

df = pd.DataFrame(data)

print("===== ORIGINAL DATASET =====")
print(df)


# ---------------------------------------
# STEP 2: Data Inspection
# ---------------------------------------

print("\n===== DATASET INFORMATION =====")

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())

print("\nStatistical Summary:")
print(df.describe())


# ---------------------------------------
# STEP 3: Missing Values
# ---------------------------------------

print("\n===== MISSING VALUES =====")

print(df.isnull().sum())


# Fill missing Marks with mean

mean_marks = df["Marks"].mean()

df["Marks"] = df["Marks"].fillna(mean_marks)

print("\nAfter Handling Missing Values:")
print(df)


# ---------------------------------------
# STEP 4: Create Result Column
# ---------------------------------------

df["Result"] = np.where(
    df["Marks"] >= 40,
    "Pass",
    "Fail"
)

print("\n===== RESULT COLUMN =====")
print(df)


# ---------------------------------------
# STEP 5: Selecting Data
# ---------------------------------------

print("\n===== SELECTED COLUMNS =====")

print(df[["Name", "Branch", "Marks"]])


# ---------------------------------------
# STEP 6: Filtering Data
# ---------------------------------------

print("\n===== STUDENTS WITH MARKS > 85 =====")

high_scorers = df[df["Marks"] > 85]

print(high_scorers)


# Multiple conditions

print("\n===== CSE STUDENTS WITH MARKS > 85 =====")

cse_high_scorers = df[
    (df["Branch"] == "CSE") &
    (df["Marks"] > 85)
]

print(cse_high_scorers)


# ---------------------------------------
# STEP 7: Sorting
# ---------------------------------------

print("\n===== STUDENTS SORTED BY MARKS =====")

sorted_df = df.sort_values(
    "Marks",
    ascending=False
)

print(sorted_df)


# ---------------------------------------
# STEP 8: GroupBy Analysis
# ---------------------------------------

print("\n===== AVERAGE MARKS BY BRANCH =====")

branch_average = df.groupby(
    "Branch"
)["Marks"].mean()

print(branch_average)


print("\n===== AVERAGE ATTENDANCE BY BRANCH =====")

attendance_average = df.groupby(
    "Branch"
)["Attendance"].mean()

print(attendance_average)


# ---------------------------------------
# STEP 9: GroupBy Multiple Statistics
# ---------------------------------------

print("\n===== BRANCH-WISE ANALYSIS =====")

branch_analysis = df.groupby("Branch")["Marks"].agg(
    ["count", "mean", "min", "max"]
)

print(branch_analysis)


# ---------------------------------------
# STEP 10: Pivot Table
# ---------------------------------------

print("\n===== PIVOT TABLE =====")

pivot_table = pd.pivot_table(
    df,
    values="Marks",
    index="Branch",
    columns="Gender",
    aggfunc="mean"
)

print(pivot_table)


# ---------------------------------------
# STEP 11: Overall Statistics Using NumPy
# ---------------------------------------

marks_array = df["Marks"].to_numpy()

print("\n===== NUMPY ANALYSIS =====")

print("Mean Marks:", np.mean(marks_array))
print("Median Marks:", np.median(marks_array))
print("Maximum Marks:", np.max(marks_array))
print("Minimum Marks:", np.min(marks_array))
print("Standard Deviation:", np.std(marks_array))
print("Total Marks:", np.sum(marks_array))


# ---------------------------------------
# STEP 12: Find Top Student
# ---------------------------------------

top_student = df.loc[
    df["Marks"].idxmax()
]

print("\n===== TOP STUDENT =====")

print(top_student)


# ---------------------------------------
# STEP 13: Export Cleaned Dataset
# ---------------------------------------

df.to_csv(
    "cleaned_student_performance.csv",
    index=False
)

print("\nCleaned dataset exported successfully.")

print("\n===== FINAL DATASET =====")
print(df)