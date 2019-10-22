from abc import abstractclassmethod, ABC
from Behavioral.mediator.user import User

class ChatMediator(ABC):
    @abstractclassmethod
    def sendMessage(self, msg, user: User):
        pass
    @abstractclassmethod
    def addUser(self, user:User):
        pass