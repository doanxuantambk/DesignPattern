package behavioral.command.document;

public class Client {
    public static void main(String[] args) {
        DocumentInvoker document = new DocumentInvoker();
        document.write("dong thu 1");
        document.read();
        document.undo();
        document.read();

        document.redo();
        document.read();
        document.write("Dong thu 2");
        document.read();
        document.write("Dong thu 3");
        document.read();
        document.undo();
        document.undo();
        document.undo();
        document.undo();
    }
}
