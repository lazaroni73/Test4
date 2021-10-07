class Person:
 def __init__ (self, name, age):
    self.name = name
    self.age = age

 def myFunc(self):
    print(" Hello koch " + self.name, self.age)

p1 = Person("John", 36)
p1.myFunc()