from abc import ABC, abstractclassmethod
class Animal(object):
   @abstractclassmethod
   def sayHello(self):
      pass

class Dog(Animal):
   def sayHello(self):
       print("Dog say Gogo")

class Cat(Animal):
   def sayHello(self):
       print("Cat say Memo")

class Duck(Animal):
   def sayHello(self):
       print("Duck say Quoac Quoc")

class AnimalFactory():

   @staticmethod
   def getAnimal(typ):
      targetclass = typ.capitalize()
      return globals()[targetclass]()
      # if targetclass == "Image":
      #     return Image()
      # elif targetclass == "Input":
      #     return Input()
      # elif targetclass == "Flash":
      #     return Flash()


# button_obj = AnimalFactory()
animals = ['dog','dog', 'cat', 'duck']
for b in animals:
   animal = AnimalFactory.getAnimal(b)
   print(animal)
   animal.sayHello()