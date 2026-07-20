class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def details(self):
        print("\nPerson Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
