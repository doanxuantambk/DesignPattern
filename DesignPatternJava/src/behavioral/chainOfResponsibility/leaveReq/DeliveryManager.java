package behavioral.chainOfResponsibility.leaveReq;

public class DeliveryManager extends Approver {
    @Override
    boolean canApprove(int numberOfDays) {
        return numberOfDays <= 5;
    }

    @Override
    void doApproving(LeaveRequest request) {
        System.out.println("Leave request approved for "+request.getDays() + " by Delivery Manager");
    }
}
