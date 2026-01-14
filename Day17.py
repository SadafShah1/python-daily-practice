class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll}")
        print(f"Marks: {self.marks}")

    def is_pass(self):
        return self.marks >= 40


student1 = Student("Ali", "AI-101", 78)
student2 = Student("Sara", "AI-102", 35)

student1.display()
print("Pass:", student1.is_pass())

print()

student2.display()
print("Pass:", student2.is_pass())

