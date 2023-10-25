getName = lambda student: student['Name']
getMark = lambda student: student['Mark']

students = []
with open('students.txt', 'r') as file:
    for line in file:
        parts = line.strip().split(',')
        if len(parts) == 2:
            name, mark = parts
            students.append({'Name': name, 'Mark': int(mark)})

sortName = sorted(students, key=getName)
