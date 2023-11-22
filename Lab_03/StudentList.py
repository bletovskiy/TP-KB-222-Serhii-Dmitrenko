from Student import Student 

class StudentList:
    def __init__(self):
        self.students = []

    def addStudent(self, student):
        self.students.append(student)
        self.sortStudents()

    def deleteStudent(self, name):
        self.students = [student for student in self.students if student.name != name]
        self.sortStudents()

    def updateStudent(self, name, newName, newAge, newPhone, newEmail):
        for student in self.students:
            if name == student.name:
                student.name = newName
                student.age = newAge
                student.phone = newPhone
                student.email = newEmail
        self.sortStudents()

    def printAllStudents(self):
        for student in self.students:
            print(f"Student name: {student.name}  Phone Number: {student.phone}  Age: {student.age}  Email: {student.email}")

    def sortStudents(self):
        self.students.sort(key=lambda student: student.name)