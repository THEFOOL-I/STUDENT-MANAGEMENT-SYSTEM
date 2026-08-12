students = [
    {"ID": 101, "Name": "Aman", "Age": 20, "Course": "Python", "Marks": 85},
    {"ID": 102, "Name": "Riya", "Age": 21, "Course": "Data Science", "Marks": 90},
    {"ID": 103, "Name": "Rahul", "Age": 20, "Course": "Python", "Marks": 78}
]

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_student = {
            "ID": 104,
            "Name": "Neha",
            "Age": 21,
            "Course": "Machine Learning",
            "Marks": 88
        }

        students.append(new_student)
        print("Student added successfully.")

    elif choice == "2":
        print("\n--- All Student Records ---")

        for student in students:
            print("ID:", student["ID"])
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Course:", student["Course"])
            print("Marks:", student["Marks"])
            print("--------------------------")

    elif choice == "3":
        search = input("Enter Student ID or Name: ")
        found = False

        for student in students:
            if str(student["ID"]) == search or student["Name"].lower() == search.lower():
                print("\nStudent Found")
                print("ID:", student["ID"])
                print("Name:", student["Name"])
                print("Age:", student["Age"])
                print("Course:", student["Course"])
                print("Marks:", student["Marks"])
                found = True

        if found == False:
            print("Student not found.")

    elif choice == "4":
        student_id = int(input("Enter Student ID to update: "))
        found = False

        for student in students:
            if student["ID"] == student_id:
                student["Name"] = "Arjun"
                student["Age"] = 22
                student["Course"] = "Python"
                student["Marks"] = 92

                print("Student updated successfully.")
                found = True

        if found == False:
            print("Student not found.")

    elif choice == "5":
        student_id = int(input("Enter Student ID to delete: "))
        found = False

        for student in students:
            if student["ID"] == student_id:
                students.remove(student)
                print("Student deleted successfully.")
                found = True
                break

        if found == False:
            print("Student not found.")

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")