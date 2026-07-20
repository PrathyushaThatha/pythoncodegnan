from student import Student
from employee import Employee
class University:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.students = {}
        self.employees = {}
    def add_course(self, course):
        self.courses.append(course)
    def add_new_student(self, name, age, gender, branch, course, email):
        sid = len(self.students) + 1
        student = Student(name, age, gender, course, branch, email)
        self.students[sid] = student
        return sid
    def remove_student(self, sid):
        if sid in self.students:
            del self.students[sid]
            return "Student Removed"
        return "Student Not Found"
    def total_students(self, course=None, branch=None, gender=None):
        count = 0
        for student in self.students.values():
            if course and student.course != course:
                continue
            if branch and student.branch != branch:
                continue
            if gender and student.gender != gender:
                continue
            count += 1
        return count
    def add_new_employee(self, name, age, gender, dept, salary, subject, role, email):
        emp_id = len(self.employees) + 1
        employee = Employee(name, age, gender, dept, salary, subject, role, email)
        self.employees[emp_id] = employee
        return emp_id
    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            return "Employee Removed"
        return "Employee Not Found"
    def total_employees(self):
        return len(self.employees)
