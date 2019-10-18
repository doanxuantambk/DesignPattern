package structural.facade;

public class Client {
    public static void main(String[] args) {
        SubFacade.getInstance().getAllInforOfSub("h004_gftth_aaa");
        SubFacade.getInstance().getHistoryComplaintOfSub("h004_gftth_aaa");
    }
}
