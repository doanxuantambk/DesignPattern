from abc import abstractmethod
import copy
class Shape:
    __id = None
    __type = None


    def clone(self):
        pass

    def setId(self,id):
        self.__id = id

    def getId(self):
        return self.__id

    def setType(self,type):
        self.__type = type

    def getType(self):
        return self.__type

class Cycle(Shape):
    def __init__(self,id):
        self.setType("Cycle")
        self.setId(id)

    def clone(self):
        return copy.copy(self)


class Rectangle(Shape):
    def __init__(self, id):
        self.setType("Rectangle")
        self.setId(id)

    def clone(self):
        return copy.copy(self)

if __name__ == "__main__":
    cycle1 = Cycle(1);
    cycle2 = cycle1.clone();
    print("Doi tuong cycle1")
    print(cycle1)
    print("id: %s , type: %s"%(cycle1.getId(),cycle1.getType()))
    print("Doi tuong cycle2")
    print(cycle2)
    print("id: %s , type: %s" % (cycle2.getId(), cycle2.getType()))

    rectangle1 = Rectangle(1);
    rectangle2 = rectangle1.clone();
    print("Doi tuong rectangle1")
    print(rectangle1)
    print("id: %s , type: %s" % (rectangle1.getId(), rectangle1.getType()))
    print("Doi tuong rectangle2")
    print(rectangle2)
    print("id: %s , type: %s" % (rectangle2.getId(), rectangle2.getType()))