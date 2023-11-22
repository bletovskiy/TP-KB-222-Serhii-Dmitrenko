import unittest
import os
from Utils import Utils
from StudentList import StudentList
from Student import Student

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_file.csv"
        self.student_list = StudentList()

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_file(self):
        with open(self.test_file, "w") as file:
            file.write("name,phone,age,email\nJohn Doe,123456789,20,john.doe@example.com")
        Utils.addFile(self.test_file, self.student_list)
        self.assertEqual(len(self.student_list.students), 1)

    def test_save_file(self):
        student = Student("John Doe", "123456789", 20, "john.doe@example.com")
        self.student_list.addStudent(student)
        Utils.saveFile(self.test_file, self.student_list)
        self.assertTrue(os.path.exists(self.test_file))

if __name__ == '__main__':
    unittest.main()