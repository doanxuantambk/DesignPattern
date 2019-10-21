package behavioral.interpreter;

public class InterpreterEngineContext {
    public int add(String input){
        String[] token = interpret(input);
        int num1 = Integer.valueOf(token[0]);
        int num2 = Integer.valueOf(token[1]);
        return num1 + num2;
    }
    public int subtract(String input){
        String[] token = interpret(input);
        int num1 = Integer.valueOf(token[0]);
        int num2 = Integer.valueOf(token[1]);
        return num1 - num2;
    }

    private String[] interpret(String input){
        String str = input.replaceAll("[^0-9]", " ");
        str = str.replaceAll("( )+"," ").trim();
        return str.split(" ");
    }
}
