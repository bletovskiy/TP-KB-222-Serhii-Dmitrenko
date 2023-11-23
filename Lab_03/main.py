from StudentList import StudentList
from Utils import Utils
from Student import Student

def main():
    studentList = StudentList()
    while True:
        choice = input("Please specify the action \nC - Create \nU - Update \nD - Delete \nP - Print \nX - Exit \nL - Load \nS - Save \n   Enter: ")
        match choice.lower():
            case "c":
                print("New element will be created:")
                student = Student(input("Enter name: "), input("Enter phone: "), input("Enter age: "), input("Enter email: "))
                studentList.addStudent(student)
            case "u":
                print("Existing element will be updated")
                name = input("Enter student name to update: ")
                studentList.updateStudent(name, input("Enter new name: "), input("Enter new age: "), input("Enter new phone: "), input("Enter new email: "))
            case "d":
                print("Element will be deleted")
                name = input("Enter student name to delete: ")
                studentList.deleteStudent(name)
            case "p":
                print("List will be printed")
                print(studentList)
            case "x":
                print("Leaving...")
                break
            case "l":
                file = input("Enter CSV file name: ")
                studentList = Utils.addFile(file, studentList)
            case "s":
                file = input("Enter CSV file name: ")
                Utils.saveFile(file, studentList)

if __name__ == "__main__":
    main()