class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.assignatures = []

    def change_name(self, newName):
        self.name = newName

    def change_age(self, newAge):
        self.age = newAge

    def addNewAssignature(self, assignatureName):
        self.assignatures.append(assignatureName)
    
    def removeAssignature(self, assignatureName):
        self.assignatures.remove(assignatureName)

student1 = Student('Manuel', 28)
student2 = Student('Juan', 27)

# print(student1.name)
# print(student2.name)

# student1.change_name('Alex')

# print(student1.name, student1.age)
# print(student2.name, student2.age)

# student2.change_age(10)

# print(student1.name, student1.age)
# print(student2.name, student2.age)

print(student1.name, student1.assignatures)
print(student2.name, student2.assignatures)

student1.addNewAssignature('Portugues')

print(student1.name, student1.assignatures)
print(student2.name, student2.assignatures)

student1.removeAssignature('Portugues')

print(student1.name, student1.assignatures)
print(student2.name, student2.assignatures)

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.speak = f'{name} barks: Woof Woof'

    def bark(self):
        print(self.speak)
    
amy = Dog('Amy', 'Chilaquil')
bianca = Dog('Bianca', 'Sepa')

amy.bark()
bianca.bark()

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def accelerate(self):
        print('Run ruuuuun')

mustang = Car('Ford', 'mustang', '2020')
