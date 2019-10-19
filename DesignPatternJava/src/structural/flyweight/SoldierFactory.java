package structural.flyweight;

import java.util.HashMap;
import java.util.Map;

public class SoldierFactory {
    private static final Map<String, ISoldier> soldiers = new HashMap<>();

    private SoldierFactory() {
    }
    public static synchronized ISoldier createSoldier(String name){
        ISoldier soldier;
        if(soldiers.containsKey(name)){
            soldier = soldiers.get(name);
        } else {
            waitingForCreateASoldier();
            soldier = new Soldier(name);
            soldiers.put(name, soldier);
        }
        return soldier;
    }
    public static int getTotalOfSoldier(){
        return soldiers.size();
    }
    private static void  waitingForCreateASoldier(){
        try{
            Thread.sleep(3000);
        }catch (Exception ex){
            ex.printStackTrace();
        }
    }
}
