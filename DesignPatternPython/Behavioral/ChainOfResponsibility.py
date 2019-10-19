from abc import abstractmethod, ABC

class LeaveRequest:
    def __init__(self, days):
        self.__days = days

    def getDays(self):
        return self.__days

class Approver(ABC):
    _nextApprover: None

    def approveLeave(self, request):
        print("Checking permission for %s"%(type(self).__name__))
        if self.canProve(request.getDays()) == True:
            self.doApproving(request)
        elif self._nextApprover != None:
            self._nextApprover.approveLeave(request)

    def setNext(self, approver):
        self._nextApprover = approver

    @abstractmethod
    def canProve(self,numberOfDays):
        pass
    @abstractmethod
    def doApproving(self,request):
        pass

class Supervisor(Approver):
    def canProve(self, numberOfDays):
        return numberOfDays <=3

    def doApproving(self, request):
        print("Leaving request approved for %s days by Supervisor "%(request.getDays()))

class DeliveryManager(Approver):
    def canProve(self, numberOfDays):
        return numberOfDays <=5

    def doApproving(self, request):
        print("Leaving request approved for %s days by Delivery Manager "%(request.getDays()))

class Director(Approver):
    def canProve(self, numberOfDays):
        return numberOfDays >5

    def doApproving(self, request):
        print("Leaving request approved for %s days by Director "%(request.getDays()))

class LeaveRequestWorkFlow:
    @staticmethod
    def getApprover():
        supervisor = Supervisor()
        manager = DeliveryManager()
        director = Director()

        supervisor.setNext(manager)
        manager.setNext(director)
        return supervisor

if __name__ == "__main__":
    LeaveRequestWorkFlow.getApprover().approveLeave(LeaveRequest(3))
    print("----------------------")
    LeaveRequestWorkFlow.getApprover().approveLeave(LeaveRequest(5))
    print("----------------------")
    LeaveRequestWorkFlow.getApprover().approveLeave(LeaveRequest(9))
