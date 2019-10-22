package behavioral.mediator;

import java.util.ArrayList;
import java.util.List;

/**
 * @author tamdx
 */
public class ChatMediatorImpl extends ChatMediator{
    private List<User> lstUser = new ArrayList<>();

    public ChatMediatorImpl(String groupName) {
        System.out.println("Start group chat "+groupName);
    }

    @Override
    public void sendMessage(String msg, User user) {
        lstUser.stream().filter(u-> !u.equals(user)).forEach(u->u.receive(msg));
    }

    @Override
    public void addUser(User user) {
        if(!lstUser.contains(user)){
            lstUser.add(user);
            user.setMediator(this);
        }
    }
}
