package structural.flyweight;

import java.util.ArrayList;
import java.util.List;

public class GameApp {
    private static List<ISoldier> soldiers = new ArrayList<>();
    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();
        createSoldier(5, "A", 1);
        createSoldier(5, "B", 5);
        createSoldier(3, "B", 2);
        createSoldier(1, "A", 3);
        long endTime = System.currentTimeMillis();
        System.out.println("-----------");
        System.out.println("Total soldiers made:" + soldiers.size());
        System.out.println("Total time to worked:" + (endTime - startTime)/1000);
        System.out.println("Total type of sodiers made :"+ SoldierFactory.getTotalOfSoldier());
    }

    private static void createSoldier(int numberOfSoldier, String soldierName, int numberOfStar){
        for(int i = 1; i <= numberOfSoldier; i++){
            Context star = new Context("Soldier" + (soldiers.size() + 1), numberOfStar);
            ISoldier soldier = SoldierFactory.createSoldier(soldierName);
            soldier.promote(star);
            soldiers.add(soldier);
        }
    }
}
