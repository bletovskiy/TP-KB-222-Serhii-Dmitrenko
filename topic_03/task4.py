list = ["a", "bb", "ccc", "dddd"]
new_value = input("New value: ") 
index_to_insert = len(list)
for i in range(len(list)):
    if new_value < list[i]:
        index_to_insert = 1
        break

list.insert(index_to_insert, new_value)

print("Результат: ", list)