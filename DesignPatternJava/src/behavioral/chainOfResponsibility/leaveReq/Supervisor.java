package behavioral.chainOfResponsibility.leaveReq;

public class Supervisor extends Approver {
    @Override
    boolean canApprove(int numberOfDays) {
        return numberOfDays <= 3;
    }

    @Override
    void doApproving(LeaveRequest request) {
        System.out.println("Leave request approved for " + request.getDays() + " by Supervisor");
    }
}
