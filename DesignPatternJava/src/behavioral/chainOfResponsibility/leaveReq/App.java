package behavioral.chainOfResponsibility.leaveReq;

public class App {
    public static void main(String[] args) {
        LeaveRequestWorkFlow.getApprover().approveLeave(new LeaveRequest(3));
        System.out.println("---");
        LeaveRequestWorkFlow.getApprover().approveLeave(new LeaveRequest(5));
        System.out.println("---");
        LeaveRequestWorkFlow.getApprover().approveLeave(new LeaveRequest(9));
    }
}