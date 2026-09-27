import pandas as pd

# Create DataFrame
data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha"],
    "Branch": ["CSE", "CSE", "IT", "CSE"],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# Process data
df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

# Export to CSV
df.to_csv("processed_students.csv", index=False)

print("\nData exported successfully.")


# Verify exported file
new_df = pd.read_csv("processed_students.csv")

print("\n----- Exported Data -----")
print(new_df)