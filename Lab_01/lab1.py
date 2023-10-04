list = [
    {"name": "Bob", "phone": "0631234567", "age": "20", "email": "bob@example.com"},
    {"name": "Emma", "phone": "0631234567", "age": "22", "email": "emma@example.com"},
    {"name": "Jon", "phone": "0631234567", "age": "21", "email": "jon@example.com"},
    {"name": "Zak", "phone": "0631234567", "age": "19", "email": "zak@example.com"}
]

def printAllList():
    for elem in list:
        strForPrint = (f"Student name is {elem['name']}, Phone is {elem['phone']}, Age is {elem['age']}, Email is {elem['email']}")
        print(strForPrint)
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
    for elem in list:
        if name == elem["name"]:
            elem["name"] = input("Please enter new name: ")
            elem["phone"] = input("Please enter new phone number: ")
            elem["age"] = input("Please enter new age: ")
            elem["email"] = input("Please enter new email: ")
            print("Element has been updated")
            break
    else:
        print("Element not found")

def main():
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ").lower()
        if choice == "c":
            print("New element will be created:")
            addNewElement()
            printAllList()
        elif choice == "u":
            print("Existing element will be updated:")
            updateElement()
            printAllList()
        elif choice == "d":
            print("Element will be deleted:")
            deleteElement()
            printAllList()
        elif choice == "p":
            print("List will be printed:")
            printAllList()
        elif choice == "x":
            print("Exit()")
            break
        else:
            print("Wrong choice")

if __name__ == "__main__":
    main()
