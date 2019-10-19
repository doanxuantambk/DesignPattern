package behavioral.chainOfResponsibility.leaveReq;

public class Director extends Approver {
    @Override
    boolean canApprove(int numberOfDays) {
        return numberOfDays > 5;
    }

    @Override
    void doApproving(LeaveRequest request) {
        System.out.println("Leave request approved for " + request.getDays() + " by Director");
    }
}
