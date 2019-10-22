from Behavioral.mediator.user import User

class UserImpl(User):

    def __init__(self, name) -> None:
        super().__init__(name)

    def send(self, msg):
        print("-----")
        print("%s is sending message:%s"%(self.name, msg))
        self.mediator.sendMessage(msg, self)

    def receive(self, msg):
        print("%s receive the message:%s" %(self.name, msg))