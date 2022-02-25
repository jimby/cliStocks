class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("My name is ", self.name)

p1 = Person('sammy', 36)
p1.myfunc()