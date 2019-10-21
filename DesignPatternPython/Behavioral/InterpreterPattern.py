from abc import abstractmethod, ABC

class Context:

    def __init__(self, input) -> None:
        super().__init__()
        self.__input = input
        self.__output = 0

    def getInput(self):
        return self.__input
    def setInput(self,input):
        self.__input = input
    def getOutput(self):
        return self.__output
    def setOutput(self,output):
        self.__output = output

class Expression(ABC):
    def interpret(self,context):
        if len(context.getInput()) == 0:
            return
        if context.getInput().startswith(self.nine()):
            context.setOutput(context.getOutput() + 9 * self.multiplier())
            context.setInput(context.getInput()[2:])
        elif context.getInput().startswith(self.four()):
            context.setOutput(context.getOutput() + 4 * self.multiplier())
            context.setInput(context.getInput()[2:])
        elif context.getInput().startswith(self.five()):
            context.setOutput(context.getOutput() + 5 * self.multiplier())
            context.setInput(context.getInput()[1:])

        while context.getInput().startswith(self.one()):
            context.setOutput(context.getOutput() + 1 * self.multiplier())
            context.setInput(context.getInput()[1:])

    @abstractmethod
    def one(self):
        pass
    @abstractmethod
    def four(self):
        pass
    @abstractmethod
    def five(self):
        pass
    @abstractmethod
    def nine(self):
        pass
    def multiplier(self):
        pass

class ThousandExpression(Expression):
    def one(self):
        return "M"

    def four(self):
        return " "

    def five(self):
        return "D"

    def nine(self):
        return " "

    def multiplier(self):
        return 1000

class HundredExpression(Expression):
    def one(self):
        return "C"

    def four(self):
        return "CD"

    def five(self):
        return "D"

    def nine(self):
        return "CM"

    def multiplier(self):
        return 100

class TenExpression(Expression):
    def one(self):
        return "X"

    def four(self):
        return "XL"

    def five(self):
        return "L"

    def nine(self):
        return "XC"

    def multiplier(self):
        return 10

class OneExpression(Expression):
    def one(self):
        return "I"

    def four(self):
        return "IV"

    def five(self):
        return "V"

    def nine(self):
        return "IX"

    def multiplier(self):
        return 1
def convertRomanToNumber(roman):
    tree = []
    tree.append(ThousandExpression())
    tree.append(HundredExpression())
    tree.append(TenExpression())
    tree.append(OneExpression())
    myit = iter(tree)
    print(next(myit).one())

    context = Context(roman)
    for exp in tree:
        exp.interpret(context)
    print("%s = %s"%(roman, context.getOutput()))
if __name__ == "__main__":
    romans = ["IV","XII","CLIX","MMXVII","MMMDLIV"]
    for roman in romans:
        convertRomanToNumber(roman)