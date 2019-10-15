from abc import ABC, abstractclassmethod
class Shape(object):
   @abstractclassmethod
   def draw(self):
      pass

class Circle(Shape):
   def draw(self):
       print("Inside Circle::draw() method.")

class Rectangle(Shape):
   def draw(self):
       print("Inside Rectangle::draw() method.")

class Square(Shape):
   def draw(self):
       print("Inside Square::draw() method.")

class ShapeFactory():
   @staticmethod
   def getShape(typ):
      targetclass = typ.capitalize()
      return globals()[targetclass]()
      # if targetclass == "Image":
      #     return Image()
      # elif targetclass == "Input":
      #     return Input()
      # elif targetclass == "Flash":
      #     return Flash()


# button_obj = ShapeFactory()
shapes = ['circle','rectangle', 'square']
for b in shapes:
   Shape = ShapeFactory.getShape(b)
   Shape.draw()