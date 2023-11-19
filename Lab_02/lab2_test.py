import unittest
import io
import os
import csv
from unittest.mock import patch

from lab2 import *

class TestYourScript(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_data.csv"
        self.test_data = [
            {"name": "John", "phone": "123-456-7890", "age": "25", "email": "john@example.com"},
            {"name": "Jane", "phone": "987-654-3210", "age": "30", "email": "jane@example.com"}
        ]

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add(self):
        with open(self.test_file, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["name", "phone", "age", "email"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.test_data)

        studentList = []
        updated_list = add(self.test_file, studentList)
        self.assertEqual(updated_list, self.test_data)

    def test_save(self):
        studentList = self.test_data
        save(self.test_file, studentList)
        self.assertTrue(os.path.exists(self.test_file))

    def test_printAllList(self):
        studentList = self.test_data
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            printAllList(studentList)
            output = mock_stdout.getvalue()
            self.assertIn("John", output)
            self.assertIn("Jane", output)

    def test_addNewElement(self):
        studentList = self.test_data
        with patch('builtins.input', side_effect=["New Student", "555-555-5555", "22", "new@student.com"]):
            addNewElement(studentList)
            self.assertEqual(len(studentList), 3)

    def test_deleteElement(self):
        studentList = self.test_data
        with patch('builtins.input', return_value="John"):
            deleteElement(studentList)
            self.assertEqual(len(studentList), 1)

    def test_updateElement(self):
        studentList = self.test_data
        with patch('builtins.input', side_effect=["John", "New John", "999-999-9999", "26", "newjohn@example.com"]):
            updateElement(studentList)
            self.assertEqual(studentList[0]["name"], "New John")


if __name__ == '__main__':
    unittest.main()