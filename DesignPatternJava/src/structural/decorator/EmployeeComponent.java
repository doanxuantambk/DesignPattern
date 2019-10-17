package structural.decorator;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public interface EmployeeComponent {
    String getName();
    void doTask();
    void join(Date joinDate);
    void terminate(Date terminateDate);

    default String formatDate(Date theDate){
        DateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
        return sdf.format(theDate);
    }

    default void showBasicInformation(){
        System.out.println("-------------------------");
        System.out.println("The basic information of "+ getName());
        join(Calendar.getInstance().getTime());

        Calendar calendar = Calendar.getInstance();
        calendar.add(Calendar.YEAR, 2);
        terminate(calendar.getTime());
    }
}
