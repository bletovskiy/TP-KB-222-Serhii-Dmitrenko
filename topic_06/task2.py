getName = lambda student: student['Name']
getMark = lambda student: int(student['Mark'])

students = []
with open("student.txt", "r") as file:
    next(file)
    for line in file:
        parts = line.strip().split(',')
        if len(parts) == 2:
            name, mark = parts
            students.append({'Name': name, 'Mark': mark})
    
sortName = sorted(students, key=getName)
for student in sortName:
    print(f"Студент: {student['Name']}, Оцінка: {student['Mark']}")

print("----------------------------")

sortMark = sorted(students, key=getMark)
for student in sortMark:
    print(f"Студент: {student['Name']}, Оцінка: {student['Mark']}")
