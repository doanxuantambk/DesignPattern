package behavioral.mediator;

/**
 * @author tamdx
 */
public class ChatClient {
    public static void main(String[] args) {
        ChatMediator mediator = new ChatMediatorImpl("Group_AI_ChatBot");
        User admin = new UserImpl("admin");
        User user1 = new UserImpl("user1");
        User user2 = new UserImpl("user2");
        User user3 = new UserImpl("user3");

        mediator.addUser(admin);
        mediator.addUser(user1);
        mediator.addUser(user2);
        mediator.addUser(user3);

        admin.send("Hi all");
        user1.send("Hi admin");

    }
}
