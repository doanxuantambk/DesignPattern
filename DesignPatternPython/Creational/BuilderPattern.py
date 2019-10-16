from abc import abstractmethod

class BankAccount:
    def __init__(self, name, accountNumber, address, email, newsletter, mobileBanking):
        self.__name = name
        self.__accountNumber = accountNumber
        self.__address = address
        self.__email = email
        self.__newsletter = newsletter
        self.__mobileBanking = mobileBanking

    def getName(self):
        return self.__name

    def getAccountNumber(self):
        return self.__accountNumber

    def getAddress(self):
        return self.__address

    def getNewsletter(self):
        return self.__newsletter

    def getMobileBanking(self):
        return self.__mobileBanking

    class AccountBuilder:
        @abstractmethod
        def withName(self, name):
            pass

        @abstractmethod
        def withAccountNumber(self, accountNumber):
            pass

        @abstractmethod
        def withAddress(self, address):
            pass

        @abstractmethod
        def build(self):
            pass


    class BankAccountBuilder(AccountBuilder):
        def __init__(self):
            self.__name = ''
            self.__accountNumber = ''
            self.__address = ''
            self.__email = ''
            self.__newsletter = False
            self.__mobileBanking = False

        def withName(self, name):
            self.__name = name
            return self

        def withAccountNumber(self, accountNumber):
            self.__accountNumber = accountNumber
            return self
        def withAddress(self, address):
            self.__address = address
            return self

        def build(self):
            bankAccount = BankAccount(self.__name, self.__accountNumber, self.__address, self.__email, self.__newsletter, self.__mobileBanking)
            return bankAccount

if __name__ == "__main__":
    bObject = BankAccount.BankAccountBuilder()\
        .withAccountNumber("00842")\
        .withName("namdx")\
        .withAddress("Nam Dinh City")\
        .build()

    print(bObject.getName())
    print(bObject.getAccountNumber())
    print(bObject.getAddress())