from project.animal import Animal
from project.dog import Dog
from project.cat import Cat

animal = Animal()
dog = Dog()
cat = Cat()

print(animal.eat())
print(dog.eat(), dog.bark())
print(cat.eat(), cat.meow())