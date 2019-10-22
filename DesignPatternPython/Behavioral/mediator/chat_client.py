from Behavioral.mediator.chat_mediator_impl import ChatMediatorImp
from Behavioral.mediator.user_impl import UserImpl

def main():
    mediator = ChatMediatorImp("Group_AI_ChatBot")
    admin = UserImpl("admin")
    user1 = UserImpl("user1")
    user2 = UserImpl("user2")
    user3 = UserImpl("user3")

    mediator.addUser(admin)
    mediator.addUser(user1)
    mediator.addUser(user2)
    mediator.addUser(user3)

    admin.send("Hi all")
    user1.send("Hi admin")

if __name__ == "__main__":
    main()