from abc import abstractmethod, ABC
from datetime import datetime
import time

class ISoldier(ABC):

    @abstractmethod
    def promote(self,context):
        pass

class Context:
    def __init__(self, id, star):
        self.__id = id
        self.__star =star
    def getId(self):
        return id
    def setId(self,id):
        self.__id = id
    def getStar(self):
        return self.__star
    def setStar(self,star):
        self.__star = star

class Soldier(ISoldier):
    def __init__(self,name):
        self.__name = name
        print("Soldier is created ! -- %s"%(name))

    def promote(self, context):
        print("%s %s promoted %s"%(self.__name,context.getId(),context.getStar()))

soldiers ={}
class SoldierFactory:

    @staticmethod
    def createSoldier(name):
        if soldiers.get(name) != None:
            return soldiers.get(name)
        else:
            time.sleep(3)
            soldier = Soldier(name)
            soldiers[name] = soldier
            return soldier

    @staticmethod
    def getTotalOfSoldier():
        return len(soldiers)


soldierList = []
def createSoldier(numberOfSoldier, soldierName, numberOfStar):
    for i in range(numberOfSoldier):
        context = Context("Soldier%s"%(len(soldierList) + 1) , numberOfStar)
        soldier = SoldierFactory.createSoldier(name=soldierName)
        soldier.promote(context)
        soldierList.append(soldier)

if __name__ == "__main__":
    start = datetime.utcnow()
    createSoldier(5, "A", 1)
    createSoldier(5, "B", 5)
    createSoldier(3, "B", 2)
    createSoldier(1, "A", 3)
    end = datetime.utcnow()
    print("Total soldier made: %s"%(len(soldiers)))
    print("Total time to worked: %s"%(end - start).total_seconds())
    print("Total type of soldiers made: %s"%(SoldierFactory.getTotalOfSoldier()))



