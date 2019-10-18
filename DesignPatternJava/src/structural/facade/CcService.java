package structural.facade;

public class CcService {
    public void getHistoryCalling(String account) {
        System.out.println("Call CC Service to get History calling of " + account);
    }

    public void getComplaintHistory(String account) {
        System.out.println("Call CC Service to get complain history of " + account);
    }
}
