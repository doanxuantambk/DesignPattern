from abc import abstractmethod, ABC,ABCMeta
from datetime import datetime,date


class EmployeeComponent(metaclass=ABCMeta):

    @abstractmethod
    def getName(self):
        pass
    @abstractmethod
    def doTask(self):
        pass
    @abstractmethod
    def join(self, joinDate):
        pass
    @abstractmethod
    def terminate(self, terminateDate):
        pass
    def formatDate(self, theDate):
        aa.getId()
        return theDate.strftime("%d/%m/%Y")
    def showBasicInformation(self):
        print("------------------------------")
        print("The basic information of %s" %(self.getName()))
        now = datetime.now()
        self.join(now)
        terminateDate = date(now.year + 2, now.month, now.day)
        self.terminate(terminateDate)

class EmployeeConcreteComponent(EmployeeComponent):
    def __init__(self, name) -> None:
        super().__init__()
        self.__name = name

    def getName(self):
        return self.__name

    def doTask(self):
        pass

    def join(self, joinDate):
        print("%s join on %s" %(self.getName(),self.formatDate(joinDate)) )

    def terminate(self, terminateDate):
        print("%s terminate on %s" %(self.getName(),self.formatDate(terminateDate)) )

class EmployeeDecorator(EmployeeComponent):
    _employee:EmployeeComponent

    def __init__(self, employee) -> None:
        super().__init__()
        self._employee = employee

    def getName(self):
        self._employee.getName()

    def join(self, joinDate):
        self._employee.join(joinDate)

    def terminate(self, terminateDate):
        self._employee.terminate(terminateDate)

class Manager(EmployeeDecorator):

    def __init__(self, employee) -> None:
        super().__init__(employee)
    def createRequirement(self):
        print("%s create some requirements" %(self.getName()))
    def assignTask(self):
        print("%s assign task" % (self.getName()))
    def manageProcess(self):
        print("%s manage process" % (self.getName()))
    def doTask(self):
        self._employee.doTask()
        self.createRequirement()
        self.assignTask()
        self.manageProcess()

class TeamLeader(EmployeeDecorator):

    def __init__(self, employee) -> None:
        super().__init__(employee)
    def planning(self):
        print("%s is planning" %(self.getName()))
    def motivate(self):
        print("%s is motivating"%(self.getName()))
    def monitor(self):
        print("%s is monitor" %(self.getName()))

    def doTask(self):
        self._employee.doTask()
        self.planning()
        self.motivate()
        self.monitor()

if __name__ == "__main__":
    print("--NORMAL EMPLOYEE:----")
    employee = EmployeeConcreteComponent("Nguyen Van A")
    employee.showBasicInformation()
    employee.doTask()
    print()

    print("--TEAM LEADER EMPLOYEE:----")
    teamleader = TeamLeader(employee)
    teamleader.showBasicInformation()
    teamleader.doTask()
    print()

    print("--MANAGER EMPLOYEE:----")
    manager = Manager(employee)
    manager.showBasicInformation()
    manager.doTask()
    print()

    print("--TEAM LEADER AND MANAGER:----")
    teamLeaderAnManager = TeamLeader(manager)
    teamLeaderAnManager.showBasicInformation()
    teamLeaderAnManager.doTask()
