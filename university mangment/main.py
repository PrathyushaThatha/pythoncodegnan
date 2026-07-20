from university import University
u = University("VITS")
u.add_course("Python")
u.add_course("Java")
u.add_course("CSE")
sid1 = u.add_new_student(
    "Prathyusha", 21, "Female",
    "CSE", "Python",
    "prathyusha@gmail.com"
)
sid2 = u.add_new_student(
    "Rahul", 20, "Male",
    "ECE", "Java",
    "rahul@gmail.com"
)
eid1 = u.add_new_employee(
    "Ramesh", 35, "Male",
    "CSE", 50000,
    "Python", "Professor",
    "ramesh@gmail.com"
)
eid2 = u.add_new_employee(
    "Sita", 32, "Female",
    "ECE", 45000,
    "Java", "Lecturer",
    "sita@gmail.com"
)
print("University:", u.name)
print("Courses:", u.courses)

print("\nStudents:")
for student in u.students.values():
    student.details()
print("\nEmployees:")
for employee in u.employees.values():
    employee.details()
print("\nTotal Students:", u.total_students())
print("CSE Students:", u.total_students(branch="CSE"))
print("Female Students:", u.total_students(gender="Female"))
print("Total Employees:", u.total_employees())
u.remove_student(sid2)
u.remove_employee(eid2)
print("\nAfter Removing:")
print("Total Students:", u.total_students())
print("Total Employees:", u.total_employees())
