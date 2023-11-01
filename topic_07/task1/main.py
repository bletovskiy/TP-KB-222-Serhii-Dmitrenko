class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Johny", 30)
person2 = Person("Jimmy", 25)

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

human = Human("Ivan", 45)
print(human)