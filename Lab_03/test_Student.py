import unittest
from Student import Student

class TestStudent(unittest.TestCase):
    def test_student_creation(self):
        student = Student("John Doe", "123456789", 20, "john.doe@example.com")
        self.assertEqual(student.name, "John Doe")
        self.assertEqual(student.phone, "123456789")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.email, "john.doe@example.com")

if __name__ == '__main__':
    unittest.main()