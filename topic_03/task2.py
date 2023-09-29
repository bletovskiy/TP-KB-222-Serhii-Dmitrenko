#extend()
#The 'extend' function is used to add items from an iterated object (such as another list) to the end of the current list.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

#append(value)
#'append' adds the given value to the end of the list.
my_list = [1,2,3]
my_list.append(5)
print(my_list)

#insert(index, value)
#'insert' adds the value to the specified index position in the list.
list3 = [1, 2, 3]
list3.insert(1, 4)
print(list3)

#remove(value)
#'remove' removes the first occurrence of the specified val value from the list.
list4 = [1, 2, 3, 2]
list4.remove(2)
print(list4)

#clear()
#'clear' removes all items from the list, making it empty.
list5 = [1, 2, 3]
list5.clear()
print(list5)

#sort()
#'sort' sorts the list items in ascending order (default) or according to a custom key function.
list6 = [3, 1, 2]
list6.sort()
print(list6)

#reverse()
#'reverse' changes the order of the list items by reversing the list.
list7 = [1, 2, 3]
list7.reverse()
print(list7)

#copy()
#'copy' creates a surface copy of the list.
list8 = [1, 2, 3]
copied_list8 = list8.copy()
print(copied_list8)
