# String operations

text = "Python Programming"

print("Original:", text)
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Replace:", text.replace("Python", "Data"))
print("Find 'Programming':", text.find("Programming"))


# List operations

numbers = [30, 10, 20]

numbers.append(40)
numbers.remove(10)
numbers.sort()

print("\nList:", numbers)


# Tuple creation and indexing

student_tuple = ("Shiv", 20, "CSE")

print("Tuple:", student_tuple)
print("Tuple index 0:", student_tuple[0])


# Dictionary

student = {
    "name": "Shiv Pratap Chaubey",
    "branch": "CSE",
    "year": 4
}

print("Dictionary:", student)
print("Student Name:", student["name"])


# Set operations

skills = {"Python", "SQL"}

skills.add("MERN")
skills.remove("SQL")

print("Set:", skills)