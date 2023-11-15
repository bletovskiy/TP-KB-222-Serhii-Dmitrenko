import csv

list = [
    {"name": "Bob", "phone": "0631234567", "age": "20", "email": "bob@example.com"},
    {"name": "Emma", "phone": "0631234567", "age": "22", "email": "emma@example.com"},
    {"name": "Jon", "phone": "0631234567", "age": "21", "email": "jon@example.com"},
    {"name": "Zak", "phone": "0631234567", "age": "19", "email": "zak@example.com"}
]

def add(file):
    try:
        with open(file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                list.append(row)
        print("CSV file loaded succesfully")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def save(file):
    try:
        with open(file, 'w', newline='') as file:
            data = ["name", "phone", "age", "email"]
            writer = csv.DictWriter(file, fieldnames=data)
            writer.writeheader()
            for item in list:
                writer.writerow(item)
        print("CSV file saved successfully")
    except Exception as e:
        print(f"An error occurred: {e}")

def printAllList():
    for elem in list:
        StrForPrint ="  Student name: " +elem["name"] + "  Phone Number: " + elem["phone"] + "  Age: " + elem["age"] + "  Email: " + elem["email"]
        print(StrForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    age = (input("Please enter student age: "))
    email = input("Please enter student email: ")
    newItem = {"name": name, "phone": phone, "age": age, "email": email}

    insertPosition = 0
    for elem in list:
        if name > elem["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for elem in list:
        if name == elem["name"]:
            deletePosition = list.index(elem)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        del list[deletePosition]
        print("Element has been deleted")

def updateElement():
    name = input("Please enter name to be updated: ")
    for index, elem in enumerate(list):
        if name == elem["name"]:
            newName = input("Please enter new name: ")
            newPhone = input("Please enter new phone number: ")
            newAge = input("Please enter new age: ")
            newEmail = input("Please enter new email: ")
            updatedItem = {"name": newName, "phone": newPhone, "age": newAge, "email": newEmail}
            del list[index]
            insertPosition = 0
            for pos, elem in enumerate(list):
                if newName > elem["name"]:
                    insertPosition = pos + 1
                else:
                    break
            list.insert(insertPosition, updatedItem)
            print("Element has been updated")
            break
    else:
        print("Element not found")

def main():
    while True:
        choice = input("Please specify the action \nC - Create \nU - Update \nD - Delete \nP - Print \nX - Exit \nL - Load \nS - Save \n   Enter: ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Leaving...")
                break
            case "L" | "l":
                file = input("Enter CSV file name: ")
                add(file)
            case "S" | "s":
                file = input("Enter CSV file name: ")
                save(file)
main()