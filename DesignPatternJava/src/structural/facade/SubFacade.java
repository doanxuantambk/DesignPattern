package structural.facade;

public class SubFacade {
    private CcService ccService;
    private CmService cmService;
    private static final SubFacade INSTANCE = new SubFacade();

    public static SubFacade getInstance() {
        return INSTANCE;
    }

    private SubFacade() {
        this.ccService = new CcService();
        this.cmService = new CmService();
    }

    public void getAllInforOfSub(String account){
        this.cmService.getSubInfo(account);
        this.cmService.getSubType(account);
    }

    public void getHistoryComplaintOfSub(String account){
        this.ccService.getComplaintHistory(account);
        this.ccService.getHistoryCalling(account);
    }

}
