package behavioral.iterator;

import java.util.ArrayList;
import java.util.List;

public class Menu {
    private List<Item> menuItems = new ArrayList<>();

    public void addItem(Item item){
        menuItems.add(item);
    }
    public Iterator<Item> iterator(){
        return new MenuIterator();
    }

    class MenuIterator implements Iterator{
        private int currentIndex = 0;

        @Override
        public boolean hasNext() {
            return currentIndex < menuItems.size();
        }

        @Override
        public Object next() {
            return menuItems.get(currentIndex++);
        }
    }
}
