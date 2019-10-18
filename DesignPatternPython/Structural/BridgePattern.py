from abc import abstractmethod,ABC

class Account(ABC):
    @abstractmethod
    def openAccount(self):
        pass

class CheckingAccount(Account):
    def openAccount(self):
        print("Checking Account")

class SavingAccount(Account):
    def openAccount(self):
        print("Saving Account")

class Bank:
    account: Account
    def __init__(self, account):
        self.account = account

    @abstractmethod
    def createAccount(self):
        pass

class VietcomBank(Bank):
    def __init__(self, account):
        super().__init__(account)

    def createAccount(self):
        print("Open your account at VietcomBank is a")
        self.account.openAccount()


class TPBank(Bank):
    def __init__(self, account):
        super().__init__(account)

    def createAccount(self):
        print("Open your account at TPBank is a")
        self.account.openAccount()

if __name__ == "__main__":
    vietcombank = VietcomBank(SavingAccount())
    vietcombank.createAccount()

    tpbank = TPBank(CheckingAccount())
    tpbank.createAccount()