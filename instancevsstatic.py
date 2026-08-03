class Student:
    college = "MIT ADT"

    def __init__(self, name):
        self.name = name

s1 = Student("Arya")
s2 = Student("Riya")

print(s1.name)
print(Student.college)