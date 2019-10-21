from abc import abstractmethod, ABC

class Item:
    def __init__(self, title, url) -> None:
        super().__init__()
        self.__url = url
        self.__title = title

    def getTitle(self):
        return self.__title
    def setTitle(self, title):
        self.__title = title
    def getUrl(self):
        return self.__url
    def setUrl(self,url):
        self.__url = url

    def __repr__(self) -> str:
        return str(self.__dict__)

class Iterator(ABC):
    @abstractmethod
    def hasNext(self):
        pass
    @abstractmethod
    def next(self):
        pass

menuItems =[]
class Menu:

    def __init__(self) -> None:
        global menuItems
        menuItems =[]

    def addItem(self,item):
        menuItems.append(item)
    def iterator(self):
        return MenuIterator()
    @staticmethod
    def getItems():
        return menuItems

class MenuIterator(Iterator):
    def __init__(self):
        self.__currentIndex = 0

    def hasNext(self):
        return self.__currentIndex < len(Menu.getItems())

    def next(self):
        self.__currentIndex = self.__currentIndex+1
        return Menu.getItems()[self.__currentIndex-1]

if __name__ == "__main__":
    menu = Menu()
    menu.addItem(Item("a1","http://localhost:1"))
    menu.addItem(Item("a2","http://localhost:2"))
    itera = menu.iterator()
    while(itera.hasNext()):
        ite = itera.next()
        print(ite)