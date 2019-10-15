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


factory ={
    "Dog": Dog(),
    "Cat": Cat(),
    "Duck": Duck()
}

class AnimalFactory():

   @staticmethod
   def get_Animal(typ):
      targetclass = typ.capitalize()
      # return globals()[targetclass]()
      return factory[targetclass]
      # if targetclass == "Image":
      #     return Image()
      # elif targetclass == "Input":
      #     return Input()
      # elif targetclass == "Flash":
      #     return Flash()


# button_obj = AnimalFactory()
button = ['dog', 'cat', 'duck']
for b in button:
   AnimalFactory.get_Animal(b).sayHello()