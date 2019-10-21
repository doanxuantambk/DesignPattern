package behavioral.interpreter.lama;

public abstract class Expression {
    void interpret(Context context) {
        if(context.getInput().length() == 0){
            return;
        }

        if(context.getInput().startsWith(nine())){
            context.setOutput(context.getOutput() + 9 * multiplier());
            context.setInput(context.getInput().substring(2));
        } else if(context.getInput().startsWith(four())){
            context.setOutput(context.getOutput() + 4 * multiplier());
            context.setInput(context.getInput().substring(2));
        } else if(context.getInput().startsWith(five())){
            context.setOutput(context.getOutput() + 5 * multiplier());
            context.setInput(context.getInput().substring(1));
        }
        while (context.getInput().startsWith(one())) {
            context.setOutput(context.getOutput() + 1 * multiplier());
            context.setInput(context.getInput().substring(1));
        }
    }

    abstract String one();

    abstract String four();

    abstract String five();

    abstract String nine();

    abstract int multiplier();

}
