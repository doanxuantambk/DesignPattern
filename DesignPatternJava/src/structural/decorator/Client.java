package structural.decorator;

public class Client {
    public static void main(String[] args) {
        System.out.println("--NORMAL EMPLOYEE:--");
        EmployeeComponent employee = new EmployeeConcreteComponent("Nguyen Van A");
        employee.showBasicInformation();
        employee.doTask();

        System.out.println();
        System.out.println("--TEAM LEADER EMPLOYEE:--");
        EmployeeComponent teamLeader = new TeamLeader(employee);
        teamLeader.showBasicInformation();
        teamLeader.doTask();

        System.out.println();
        System.out.println("--MANAGER EMPLOYEE:--");
        EmployeeComponent manager = new Manager(employee);
        manager.showBasicInformation();
        manager.doTask();

        System.out.println();
        System.out.println("--MANAGER AND TEAM LEADER EMPLOYEE:--");
        EmployeeComponent teamLeaderAnManager = new Manager(teamLeader);
        teamLeaderAnManager.showBasicInformation();
        teamLeaderAnManager.doTask();
    }
}
