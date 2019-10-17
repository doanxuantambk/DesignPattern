package structural.decorator;

import java.util.Date;

public class Manager extends EmployeeDecorator {

    public Manager(EmployeeComponent employeeComponent) {
        super(employeeComponent);
    }
    public void createRequirement(){
        System.out.println(this.getName() + " create some requirements");
    }
    public void assignTask(){
        System.out.println(this.getName() + " assign the task");
    }

    public void manageProcess(){
        System.out.println(this.getName() + " manage process");
    }

    @Override
    public void doTask() {
        employeeComponent.doTask();
        createRequirement();
        assignTask();
        manageProcess();
    }
}
