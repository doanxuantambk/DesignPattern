package behavioral.iterator;

import java.util.ArrayList;
import java.util.List;

public class Client {
    public static void main(String[] args) {
        Menu menu = new Menu();
        menu.addItem(new Item("tb_thue_bao","http://localhost:8081/thong_tin_tb.html"));
        menu.addItem(new Item("tra_cuu_cuoc","http://localhost:8081/tra_cuu_cuoc.html"));
        menu.addItem(new Item("lich_su_cuoc_goi","http://localhost:8081/cc/ls_cuocgoi.html"));
        Iterator<Item> iterator = menu.iterator();
        while (iterator.hasNext()){
            Item item = iterator.next();
            System.out.println(item.toString());
        }

        List<Item> lstItem = new ArrayList<>();
        lstItem.add(new Item("tb_thue_bao","http://localhost:8081/thong_tin_tb.html"));
        lstItem.add(new Item("tra_cuu_cuoc","http://localhost:8081/tra_cuu_cuoc.html"));
        lstItem.add(new Item("lich_su_cuoc_goi","http://localhost:8081/cc/ls_cuocgoi.html"));
        java.util.Iterator<Item> iterator1 = lstItem.iterator();
    }
}
