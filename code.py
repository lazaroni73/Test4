class Student:
    def __init__(self,name,items):
        self.name = name
        self.items = items
    def average (self):
        return sum(self.grades) / len(self.grades)

        

student = Student("Vesko",(50,100,200))
student2 = Student("Bob",(50,200,350))
student3 = Student("Vesko",(50,200,400))
print(student3.average())
    