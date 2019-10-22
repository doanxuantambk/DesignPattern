from abc import abstractclassmethod, ABC

class User(ABC):
    def __init__(self, name) -> None:
        super().__init__()
        self._name = name
        self._mediator = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    @property
    def mediator(self):
        return self._mediator
    @mediator.setter
    def mediator(self, med):
        self._mediator = med

    @abstractclassmethod
    def send(self, msg):
        pass
    @abstractclassmethod
    def receive(self,msg):
        pass



