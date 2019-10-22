package behavioral.mediator;

/**
 * @author tamdx
 */
public class UserImpl extends User {
    public UserImpl(String name) {
        super(name);
    }


    @Override
    public void send(String msg) {
        System.out.println("----");
        System.out.println(this.getName() + " is sending message:" + msg);
        mediator.sendMessage(msg, this);
    }

    @Override
    public void receive(String msg) {
        System.out.println(this.getName() + " received the message :"+msg);
    }
}
