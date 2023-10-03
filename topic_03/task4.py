list = ["e", "j", "p"]

while True:
    new_value = input("New value (or 'quit' to exit): ")
    
    if new_value == 'quit':
        break

    insert_index = 0

    for elem in list:
        if new_value > elem:
            insert_index += 1

    list.insert(insert_index, new_value)

    print("Result:", list) 