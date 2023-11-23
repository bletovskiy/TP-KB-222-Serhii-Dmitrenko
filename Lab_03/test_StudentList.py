import unittest
from Student import Student
from StudentList import StudentList

class TestStudentListMethods(unittest.TestCase):

    def setUp(self):
        self.studentList = StudentList()
        self.student1 = Student("Bob", "123-456-7890", 20, "bob@example.com")
        self.student2 = Student("Derek", "987-654-3210", 22, "derek@example.com")

    def test_addStudent(self):
        self.studentList.addStudent(self.student1)
        self.assertEqual(len(self.studentList.students), 1)
        self.assertEqual(self.studentList.students[0].name, "Bob")

        self.studentList.addStudent(self.student2)
        self.assertEqual(len(self.studentList.students), 2)
        self.assertEqual(self.studentList.students[1].name, "Derek")

    def test_DeleteStudent(self):
        self.studentList.addStudent(self.student1)
        self.studentList.addStudent(self.student2)

        self.studentList.deleteStudent("Bob")
        self.assertEqual(len(self.studentList.students), 1)
        self.assertEqual(self.studentList.students[0].name, "Derek")

        self.studentList.deleteStudent("Alice")
        self.assertEqual(len(self.studentList.students), 1)

    def test_UpdateStudent(self):
        self.studentList.addStudent(self.student1)
        self.studentList.addStudent(self.student2)

        newStudent = Student("Bob", "999-999-9999", 21, "bob@example.com")
        self.studentList.updateStudent("Bob", newStudent)

        self.assertEqual(len(self.studentList.students), 2)
        self.assertEqual(self.studentList.students[0].phone, "999-999-9999")
        self.assertEqual(self.studentList.students[0].email, "bob@example.com")

        nonExistingStudent = Student("Alice", "111-111-1111", 25, "alice@example.com")
        self.studentList.updateStudent("Alice", nonExistingStudent)

        self.assertEqual(len(self.studentList.students), 2)

if __name__ == '__main__':
    unittest.main()