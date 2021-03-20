from project.food import Vegetable, Fruit, Meat, Seed
from project.animals.birds import Hen, Owl
from project.animals.mammals import Mouse, Cat, Dog, Tiger


hen = Hen("Heny", 2, 25)
owl = Owl("Owly", 2.25, 27)
mouse = Mouse("Mousy", 0.6, "basement")
cat = Cat("Catsy", 3.5, "house")
dog = Dog("Doggo", 5, "yard")
tiger = Tiger("Tigeria", 7, "woods")

# print(hen)
# print(owl)
# print(mouse)
# print(cat)
# print(dog)
# print(tiger)
#
# print(hen.make_sound())
# print(owl.make_sound())
# print(mouse.make_sound())
# print(cat.make_sound())
# print(dog.make_sound())
# print(tiger.make_sound())
#
veg = Vegetable(5)
meat = Meat(3)
fruit = Fruit(6)
seed = Seed(10)
#
# print(owl.feed(fruit))
# print(mouse.feed(seed))
# print(cat.feed(fruit))
# print(dog.feed(veg))
# print(tiger.feed(seed))
#
# hen.feed(seed)
# owl.feed(meat)
# mouse.feed(fruit)
# cat.feed(veg)
# dog.feed(meat)
# tiger.feed(meat)
#
# print(hen)
# print(owl)
# print(mouse)
# print(cat)
# print(dog)
# print(tiger)

# owl = Owl("Pip", 10, 10)
# print(owl)
# meat = Meat(4)
# print(owl.make_sound())
# owl.feed(meat)
# veg = Vegetable(1)
# print(owl.feed(veg))
# print(owl)

# hen = Hen("Harry", 10, 10)
# veg = Vegetable(3)
# fruit = Fruit(5)
# meat = Meat(1)
# print(hen)
# print(hen.make_sound())
# hen.feed(veg)
# hen.feed(fruit)
# hen.feed(meat)
# print(hen)

