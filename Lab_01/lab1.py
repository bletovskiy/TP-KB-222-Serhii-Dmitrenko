import random

list = [
    {"id": "00001", "name": "Bob", "phone": "0631234567", "age": "20", "email": "bob@example.com"},
    {"id": "00002", "name": "Emma", "phone": "0631234568", "age": "22", "email": "emma@example.com"},
    {"id": "00003", "name": "Jon", "phone": "0631234569", "age": "21", "email": "jon@example.com"},
    {"id": "00004", "name": "Zak", "phone": "0631234570", "age": "19", "email": "zak@example.com"}
]

def printAllList():
    for elem in list:
        StrForPrint = "  Student ID: "+ elem["id"] +"  Student name: " +elem["name"] + "  Phone Number: " + elem["phone"] + "  Age: " + elem["age"] + "  Email: " + elem["email"]
        print(StrForPrint)
    return

def generateUniqueId():
    while True:
        unique_id = str(random.randint(10000, 99999))

        if not any(elem["id"] == unique_id for elem in list):
            return unique_id

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    age = input("Please enter student age: ")
    email = input("Please enter student email: ")
    
    unique_id = generateUniqueId()
    
    newItem = {"id": unique_id, "name": name, "phone": phone, "age": age, "email": email}
    
    list.append(newItem)
    print("New element has been added")

def deleteElement():
    id_to_delete = input("Please enter the ID of the student to be deleted: ")
    found = False

    for elem in list:
        if elem.get("id") == id_to_delete:
            list.remove(elem)
            print("Student with ID '{}' has been deleted.".format(id_to_delete))
            found = True
            break

    if not found:
        print("Student with ID '{}' was not found.".format(id_to_delete))

def updateElement():
    id_to_update = input("Please enter the ID of the student to be updated: ")
    found = False

    for elem in list:
        if elem.get("id") == id_to_update:
            print("Student found. Enter updated information:")
            new_name = input("New name: ")
            new_phone = input("New phone: ")
            new_age = input("New age: ")
            new_mail = input("New Email: ")

            elem["name"] = new_name
            elem["phone"] = new_phone
            elem["age"] = new_age
            elem["email"] = new_mail

            print("Student information updated.")
            found = True
            break

    if not found:
        print("Student with ID '{}' was not found.".format(id_to_update))

def main():
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ")
        
        if choice in ["C", "c"]:
            print("New element will be created:")
            addNewElement()
            printAllList()
        elif choice in ["U", "u"]:
            print("Existing element will be updated")
            updateElement()
            printAllList()
        elif choice in ["D", "d"]:
            print("Element will be deleted")
            deleteElement()
            printAllList()
        elif choice in ["P", "p"]:
            print("List will be printed")
            printAllList()
        elif choice in ["X", "x"]:
            break
        else:
            print("Wrong choice")

main()