
students = []


def add_student():
    name = input("Enter student name: ").strip()
    roll_no = input("Enter roll number: ").strip()
    branch = input("Enter branch: ").strip()

    if not name or not roll_no or not branch:
        print("All fields are required.")
        return

    if any(s["roll_no"].lower() == roll_no.lower()
           for s in students):
        print("Roll number already exists.")
        return

    student = {
        "name": name,
        "roll_no": roll_no,
        "branch": branch
    }

    students.append(student)
    print("Student added successfully.")


def display_students():
    if not students:
        print("No student records available.")
        return

    print("\n--- All Student Records ---")
    for student in students:
        print("Name:", student["name"])
        print("Roll Number:", student["roll_no"])
        print("Branch:", student["branch"])
        print("-------------------------")


def search_student():
    name = input("Enter student name to search: ").strip()

    found = False
    for student in students:
        if student["name"].lower() == name.lower():
            print("Student Found:")
            print("Name:", student["name"])
            print("Roll Number:", student["roll_no"])
            print("Branch:", student["branch"])
            found = True

    if not found:
        print("Student not found.")


def delete_student():
    roll_no = input("Enter roll number to delete: ").strip()

    for student in students:
        if student["roll_no"].lower() == roll_no.lower():
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")


while True:
    print("\n===== Student Record Management =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by Name")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting Student Record Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
