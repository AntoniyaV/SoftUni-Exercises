from project.dog import Dog
from project.cat import Cat
from project.kitten import Kitten
from project.tomcat import Tomcat


dog = Dog("Doggo", 3, "Male")
cat = Cat("Tom", 4, "Male")
kitten = Kitten("Blacky", 2)
tomcat = Tomcat("Jeff", 2)

print(dog)
print(dog.make_sound())
print(cat)
print(cat.make_sound())
print(kitten)
print(kitten.make_sound())
print(tomcat)
print(tomcat.make_sound())