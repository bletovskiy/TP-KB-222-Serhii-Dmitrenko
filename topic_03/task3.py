#update()
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(dict1)

#del
dict3 = {'a': 1, 'b': 2, 'c': 3}
del dict3['b']
print(dict3)

#clear()
dict4 = {'a': 1, 'b': 2, 'c':3}
dict4.clear()
print(dict4)

#keys()
dict5 = {'a': 1, 'b': 2, 'c': 3}
keys = dict5.keys()
print(keys)

#values()
dict6 = {'a': 1, 'b': 2, 'c': 3}
values = dict6.values()
print(values)

#items()
dict7 = {'a': 1, 'b': 2, 'c': 3}
items = dict7.items()
print(items)