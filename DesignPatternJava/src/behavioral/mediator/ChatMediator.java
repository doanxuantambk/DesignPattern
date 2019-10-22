package behavioral.mediator;

/**
 * @author tamdx
 */
public abstract class ChatMediator {
    public abstract void sendMessage(String msg, User user);
    public abstract void addUser(User user);
}
