## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "phone":"0631234567", "email":"bob@example.com", "age":"19"},
    {"name":"Emma", "phone":"0631234567", "email":"emma@example.com", "age":"19"},
    {"name":"Jon",  "phone":"0631234567", "email":"jon@example.com", "age":"21"},
    {"name":"Zak",  "phone":"0631234567", "email":"zak@example.com", "age":"18"}
]

def printAllList():
    for elem in list:
        StrForPrint = "  Student name: " +elem["name"] + "  Phone Number: " + elem["phone"] + "  Email: " + elem["email"] + "  Age: " + elem["age"]
        print(StrForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Pease enter student email: ")
    age = input("Please enter student age: ")
    newItem = {"name": name, "phone": phone, "email": email, "age": age}
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    for elem in list:
        if elem["name"] == name:
            print(elem["name"] + " found. Please write the information")
            new_name = input("New name: ")
            new_phoneNumber = input("New phone number: ")
            new_email = input("New email: ")
            new_age = input("New age: ")

            elem["name"] = new_name
            elem["phone"] = new_phoneNumber
            elem["email"] = new_email
            elem["age"] = new_age

            print("Update successfully")
            return
    print("Not found")

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()