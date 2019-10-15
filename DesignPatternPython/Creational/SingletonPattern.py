class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    """ Python khong co private constructor"""
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is singleton")
        else:
            Singleton.__instance = self

s2 = Singleton()
print(s2)

s = Singleton.getInstance()
print(s)

s2 = Singleton.getInstance()
print(s2)



