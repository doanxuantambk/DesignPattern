package behavioral.interpreter.lama;

public class HundredExpression extends Expression {
    @Override
    String one() {
        return "C";
    }

    @Override
    String four() {
        return "CD";
    }

    @Override
    String five() {
        return "D";
    }

    @Override
    String nine() {
        return "CM";
    }

    @Override
    int multiplier() {
        return 100;
    }
}
