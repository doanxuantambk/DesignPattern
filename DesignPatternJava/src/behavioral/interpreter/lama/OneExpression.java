package behavioral.interpreter.lama;

public class OneExpression extends Expression {
    @Override
    String one() {
        return "I";
    }

    @Override
    String four() {
        return "IV";
    }

    @Override
    String five() {
        return "V";
    }

    @Override
    String nine() {
        return "IX";
    }

    @Override
    int multiplier() {
        return 1;
    }
}
