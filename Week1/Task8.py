filename = "introduction.txt"

introduction = """
My name is Shiv Pratap Chaubey.
I am a B.Tech Computer Science & Engineering student.
I am learning Python programming for Data Analytics.
"""

# Create and write to the file

with open(filename, "w") as file:
    file.write(introduction)

# Read the file

with open(filename, "r") as file:
    content = file.read()

print("File contents:")
print(content)