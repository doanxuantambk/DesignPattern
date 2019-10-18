package structural.facade;

public class CmService {
    protected void getSubInfo(String account){
        System.out.println("Call CM Service to get sub info of:"+account);
    }

    protected void getSubType(String account){
        System.out.println("Call CM Service to get sub type of:"+account);
    }
}
