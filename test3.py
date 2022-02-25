class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def myfunc(self):
		self.age = input('what is your age: ')
		print("Hello my name is " + self.name)
		print('and my age is ' + str(self.age))

p1 = Person("filbert", 36)
p1.myfunc()
