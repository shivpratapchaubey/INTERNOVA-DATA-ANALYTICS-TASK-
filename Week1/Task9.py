students = []


# Function to add student
def add_student():

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    branch = input("Enter branch: ")
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "roll_no": roll_no,
        "branch": branch,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully.\n")


# Function to display students
def display_students():

    if not students:
        print("No student records found.\n")
        return

    print("\n----- All Student Records -----")

    for student in students:

        print("Name   :", student["name"])
        print("Roll No:", student["roll_no"])
        print("Branch :", student["branch"])
        print("Marks  :", student["marks"])

        print("------------------------------")


# Function to search student
def search_student():

    name = input("Enter student name to search: ")

    found = False

    for student in students:

        if student["name"].lower() == name.lower():

            print("\nStudent Found:")
            print("Name   :", student["name"])
            print("Roll No:", student["roll_no"])
            print("Branch :", student["branch"])
            print("Marks  :", student["marks"])

            found = True
            break

    if not found:
        print("Student not found.\n")


# Function to delete student
def delete_student():

    roll_no = input("Enter roll number to delete: ")

    for student in students:

        if student["roll_no"] == roll_no:

            students.remove(student)

            print("Student deleted successfully.\n")

            return

    print("Student not found.\n")


# Main Menu

while True:

    print("\n===== Student Record Management System =====")

    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by Name")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")