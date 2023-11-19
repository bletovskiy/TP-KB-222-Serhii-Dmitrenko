import csv

def add(file, studentList):
    with open(file, encoding="utf-8", newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(f"Read row: {row}")
            studentList.append({
                "name": row["name"],
                "phone": row["phone"],
                "age": row["age"],
                "email": row["email"],
            })
    return studentList

def save(file, studentList):
    try:
        with open(file, "w", newline="", encoding="utf-8") as saveFile:
            fieldnames = ["name", "phone", "age", "email"]
            writer = csv.DictWriter(saveFile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(studentList)
        print("File saved")
    except IOError as e:
        print(f"Error saving data to {file}: {e}")



def printAllList(studentList):
    for elem in studentList:
        StrForPrint ="  Student name: " +elem["name"] + "  Phone Number: " + elem["phone"] + "  Age: " + elem["age"] + "  Email: " + elem["email"]
        print(StrForPrint)
    return

def addNewElement(studentList):
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    age = (input("Please enter student age: "))
    email = input("Please enter student email: ")
    newItem = {"name": name, "phone": phone, "age": age, "email": email}

    studentList.append(newItem)
    studentList.sort(key=lambda student: student["name"])
    print("Element: add")
    

def deleteElement(studentList):
    name = input("Please enter name to be deleted: ")
    for student in studentList:
        if name == student["name"]:
            studentList.remove(student)
            print("Element: deleted")
            break
    else:
        print("Element: not found")

def updateElement(studentList):
    name = input("Please enter name to be updated: ")
    for student in studentList:
        if name == student["name"]:
            student["name"] = input("Enter new name: ")
            student["age"] = input("Enter new age: ")
            student["phone"] = input("Enter new phone number: ")
            student["email"] = input("Enter new email: ")
            studentList.sort(key=lambda student: student["name"])
            print("Element: updated")
            break
    else:
        print("Student not found")

def main():
    studentList = []
    while True:
        choice = input("Please specify the action \nC - Create \nU - Update \nD - Delete \nP - Print \nX - Exit \nL - Load \nS - Save \n   Enter: ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement(studentList)
                printAllList(studentList)
            case "U" | "u":
                print("Existing element will be updated")
                updateElement(studentList)
            case "D" | "d":
                print("Element will be deleted")
                deleteElement(studentList)
            case "P" | "p":
                print("List will be printed")
                printAllList(studentList)
            case "X" | "x":
                print("Leaving...")
                break
            case "L" | "l":
                file = input("Enter CSV file name: ")
                studentList = add(file,studentList)
            case "S" | "s":
                file = input("Enter CSV file name: ")
                save(file, studentList)
main()