import unittest
from StudentList import StudentList
from Student import Student

class TestStudentList(unittest.TestCase):
    def setUp(self):
        self.student_list = StudentList()

    def test_add_student(self):
        student = Student("John Doe", "123456789", 20, "john.doe@example.com")
        self.student_list.addStudent(student)
        self.assertIn(student, self.student_list.students)

    def test_delete_student(self):
        student = Student("John Doe", "123456789", 20, "john.doe@example.com")
        self.student_list.addStudent(student)
        self.student_list.deleteStudent("John Doe")
        self.assertNotIn(student, self.student_list.students)

    def test_update_student(self):
        student = Student("John Doe", "123456789", 20, "john.doe@example.com")
        self.student_list.addStudent(student)
        self.student_list.updateStudent("John Doe", "Jane Doe", 21, "987654321", "jane.doe@example.com")
        updated_student = self.student_list.students[0]
        self.assertEqual(updated_student.name, "Jane Doe")
        self.assertEqual(updated_student.age, 21)
        self.assertEqual(updated_student.phone, "987654321")
        self.assertEqual(updated_student.email, "jane.doe@example.com")

if __name__ == '__main__':
    unittest.main()