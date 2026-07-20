from person import Person
class Employee(Person):
    def __init__(self, name, age, gender, dept, salary, subject, role, email):
        super().__init__(name, age, gender)
        self.dept = dept
        self.salary = salary
        self.subject = subject
        self.role = role
        self.email = email
    def calculate_salary(self, workingdays):
        return self.salary * workingdays
    def add_subject(self, new_subject):
        self.subject = new_subject
    def details(self):
        print("\nEmployee Details")
        super().details()
        print("Department:", self.dept)
        print("Salary:", self.salary)
        print("Subject:", self.subject)
        print("Role:", self.role)
        print("Email:", self.email)
