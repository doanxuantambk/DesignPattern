package behavioral.interpreter.lama;

public class TenExpression extends Expression {
    @Override
    String one() {
        return "X";
    }

    @Override
    String four() {
        return "XL";
    }

    @Override
    String five() {
        return "L";
    }

    @Override
    String nine() {
        return "XC";
    }

    @Override
    int multiplier() {
        return 10;
    }
}
