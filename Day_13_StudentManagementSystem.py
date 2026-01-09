students = []


def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }
students.append(student)
    print("Student added successfully\n")


def view_students():
    if not students:
        print("No students found\n")
        return

    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")
    print()

