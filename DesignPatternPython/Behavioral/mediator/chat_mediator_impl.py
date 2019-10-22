from Behavioral.mediator.chat_mediator import ChatMediator
from Behavioral.mediator.user import User
from typing import List


class ChatMediatorImp(ChatMediator):
    __lstUser: List[User] = []

    def __init__(self,groupName) -> None:
        super().__init__()
        print("%s group already created"%(groupName))

    def sendMessage(self, msg, user: User):
        [us.receive(msg) for us in list(filter(lambda u: u.name != user.name, self.__lstUser))]

    def addUser(self, user: User):
        users = list(filter(lambda u: u.name ==user.name, self.__lstUser))
        if not users:
            self.__lstUser.append(user)
            user.mediator = self