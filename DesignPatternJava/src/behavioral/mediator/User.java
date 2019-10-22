package behavioral.mediator;

import java.util.Objects;

/**
 * @author tamdx
 */
public abstract class User {
    protected ChatMediator mediator;
    protected String name;

    public User(String name) {
        this.name = name;
    }

    public void setMediator(ChatMediator mediator) {
        this.mediator = mediator;
    }

    public String getName() {
        return name;
    }

    public abstract void send(String msg);

    public abstract void receive(String msg);

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof User)) return false;
        User user = (User) o;
        return Objects.equals(name, user.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name);
    }
}
