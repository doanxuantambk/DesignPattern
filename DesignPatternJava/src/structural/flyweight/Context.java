package structural.flyweight;

public class Context {
    private String id;
    private int start;

    public Context(String id, int start) {
        this.id = id;
        this.start = start;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public int getStart() {
        return start;
    }

    public void setStart(int start) {
        this.start = start;
    }
}
