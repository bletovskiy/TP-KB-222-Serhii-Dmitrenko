import csv
from lab2 import *

list = []

def test_printAllList():
    list.append({"name": "Jon", "phone": "0631234567", "age" : "24", "email": "jon@example.com"})
    assert printAllList() == "Student name: Jon  Phone Number: 0631234567  Age: 24  Email: jon@example.com"
    list.clear

def test_addNewElement():
    addNewElement("Jon", "0631234567", "24", "jon@example.com")
    assert list == [{"name": "Jon", "phone": "0631234567", "age" : "24", "email": "jon@example.com"}]

def test_deleteElement():
    list.append({"name": "Jon", "phone": "0631234567", "age" : "24", "email": "jon@example.com"})
    deleteElement("Jon")
    assert list == []

def test_updateElement():
    list.append({"name": "Jon", "phone": "0631234567", "age" : "24", "email": "jon@example.com"})
    updateElement("John", "0631234567", "24", "jon@example.com")
    assert list == [{"name": "John", "phone": "0631234567", "age" : "24", "email": "jon@example.com"}]

def test_addCSV():
    list("test.csv")
    assert list == [{"name": "Jon", "phone": "0631234567", "age" : "24", "email": "jon@example.com"}]

def test_save():
    save("test.csv")
    with open("test.csv", 'r') as file:
        reader = csv.DictReader(file)
        assert list(reader) == [{"name": "Jon", "phone": "0631234567", "age" : "24", "email": "jon@example.com"}]