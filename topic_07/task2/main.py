class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

students = [
    Student("Ivan", 21),
    Student("Marie", 25),
    Student("Hannah", 19),
    Student("George", 27),
    Student("Derek", 20),
]

sortStudents = sorted(students, key=lambda student: student.age)
for student in sortStudents:
    print(f"Name: {student.name}, Age: {student.age}")