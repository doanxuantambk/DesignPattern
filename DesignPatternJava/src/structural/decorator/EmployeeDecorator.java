package structural.decorator;

import java.util.Date;

public abstract class EmployeeDecorator implements EmployeeComponent {
    protected EmployeeComponent employeeComponent;

    public EmployeeDecorator(EmployeeComponent employeeComponent) {
        this.employeeComponent = employeeComponent;
    }

    @Override
    public String getName() {
        return employeeComponent.getName();
    }

    @Override
    public void join(Date joinDate) {
        employeeComponent.join(joinDate);
    }

    @Override
    public void terminate(Date terminateDate) {
        employeeComponent.terminate(terminateDate);
    }
}
