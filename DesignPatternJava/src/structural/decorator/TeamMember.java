package structural.decorator;

public class TeamMember extends EmployeeDecorator {
    public TeamMember(EmployeeComponent employeeComponent) {
        super(employeeComponent);
    }
    public void reportTask(){
        System.out.println(this.getName() + " report task to manager");
    }
    public void coordinateWithOther(){
        System.out.println(this.getName() + " coordinates with Others");
    }

    @Override
    public void doTask() {
        employeeComponent.doTask();
        reportTask();
        coordinateWithOther();
    }
}
