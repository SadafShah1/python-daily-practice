import json

FILE_NAME = "employees.json"

def load_employees():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_employees(employees):
    with open(FILE_NAME, "w") as file:
        json.dump(employees, file, indent=4)

def add_employee():
    employees = load_employees()

    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    department = input("Enter department: ")
    salary = input("Enter salary: ")

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    employees.append(employee)
    save_employees(employees)
    print("Employee added successfully")

def view_employees():
    employees = load_employees()
    if not employees:
        print("No employee records found")
        return

    for emp in employees:
        print("-------------------")
        print("ID:", emp["id"])
        print("Name:", emp["name"])
        print("Department:", emp["department"])
        print("Salary:", emp["salary"])

def main():
    while True:
        print("""
1. Add Employee
2. View Employees
3. Exit
""")
        choice = input("Choose option: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
