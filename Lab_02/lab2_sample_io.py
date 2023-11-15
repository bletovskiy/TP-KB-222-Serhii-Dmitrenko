'''
########## argv using #########
from sys import argv

print(f"Script name: {argv[0]}")
#print(f"Input parameter: {argv[1]}")
'''

'''
########## read from file ##########
file_name = argv[0]
with open(file_name, "r") as file:
    for line in file:
        print(f"line from file: {line}")
'''

'''
########## write to file ##########
file_name = argv[0]
with open(file_name, "a") as file:
    file.write("New student name,1231213")
'''

'''
########## read csv file ##########
import csv
file_name = argv[1]
students = []
with open(file_name) as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"Name":row["Name"], "Phone":row["Phone"]})

print(students)
'''

''' ########## read csv file ##########
import csv
with open("lab2_out.csv", "w", newline='') as csvfile:
    fieldnames = ["Name", "Age"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'Ihor', 'Age': '37'})
'''