package behavioral.command.document;

import java.util.Stack;

public class DocumentInvoker {
    private Stack<Command> undoCommands = new Stack<>();
    private Stack<Command> redoCommands = new Stack<>();
    private Document document = new Document();

    public void undo() {
        System.out.println("****Thu hien undo");
        if(!undoCommands.isEmpty()){
            Command cm = undoCommands.pop();
            cm.undo();
            redoCommands.push(cm);

        } else {
            System.out.println("Nothing to undo");
        }


    }

    public void redo() {
        System.out.println("****Thu hien redo");
        if(!redoCommands.isEmpty()){
            Command cm = redoCommands.pop();
            cm.redo();
            undoCommands.push(cm);
        } else {
            System.out.println("Nothing to redo");
        }

    }
    public void write(String text){
        System.out.println("****Thu hien write");
        Command cm = new DocumentEditorCommand(document, text);
        undoCommands.push(cm);
        redoCommands.clear();
    }
    public void read(){
        System.out.println("****Thu hien read");
        sleep();
        document.readDocument();
    }
    public void sleep(){
        try{
            Thread.sleep(1000);
        }catch (Exception ex){
            ex.printStackTrace();
        }
    }
}
