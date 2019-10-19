package behavioral.chainOfResponsibility.leaveReq;

public abstract class Approver {
    protected Approver nextApprover;

    public void setNext(Approver approver){
        this.nextApprover = approver;
    }

    public void approveLeave(LeaveRequest request){
        System.out.println("Checking permission for " + this.getClass().getSimpleName());

        if(this.canApprove(request.getDays())){
            this.doApproving(request);
        } else if(nextApprover != null){
            nextApprover.approveLeave(request);
        }
    }
    abstract boolean canApprove(int numberOfDays);
    abstract void doApproving(LeaveRequest request);

}
