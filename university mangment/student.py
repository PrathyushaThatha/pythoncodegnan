from person import Person
class Student(Person):
    def __init__(self, name, age, gender, course, branch, email, marks=0):
        super().__init__(name, age, gender)
        self.course = course
        self.branch = branch
        self.email = email
        self.marks = marks
    def percentage(self):
        return self.marks
    def details(self):
        print("\nStudent Details")
        super().details()
        print("Course:", self.course)
        print("Branch:", self.branch)
        print("Email:", self.email)
        print("Percentage:", self.percentage())
