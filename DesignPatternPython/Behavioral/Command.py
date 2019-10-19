from abc import abstractmethod,ABC

class Document:
    __lines =[]
    def write(self,text):
        self.__lines.append(text)

    def eraseLast(self):
        if self.__lines:
            self.__lines.pop()

    def readDocument(self):
        if not self.__lines:
            print("Document is empty")
        else:
            for txt in self.__lines:
                print(txt)

class Command(ABC):
    @abstractmethod
    def undo(self):
        pass
    def redo(self):
        pass

class DocumentEditorCommand(Command):
    def __init__(self, document, text) -> None:
        super().__init__()
        self.__document = document
        self.__text = text
        self.__document.write(text)

    def undo(self):
        self.__document.eraseLast()

    def redo(self):
        self.__document.write(self.__text)


class DocumentInvoker:
    __undoCommand = []
    __redoCommand = []
    __document = Document()

    def undo(self):
        if self.__undoCommand:
            cm = self.__undoCommand.pop()
            cm.undo()
            self.__redoCommand.append(cm)
        else:
            print("Nothing to undo")

    def redo(self):
        if self.__redoCommand:
            cm = self.__redoCommand.pop()
            cm.redo()
            self.__undoCommand.append(cm)
        else:
            print("Nothing to redo")

    def write(self,text):
        cm = DocumentEditorCommand(self.__document, text)
        self.__undoCommand.append(cm)
        self.__redoCommand.clear()

    def read(self):
        print("------------")
        self.__document.readDocument()


if __name__ == "__main__":
    documentInvoker = DocumentInvoker()
    documentInvoker.write("Dong thu 1")
    documentInvoker.read()
    documentInvoker.undo()
    documentInvoker.read()

    documentInvoker.redo()
    documentInvoker.read()
    documentInvoker.write("Dong thu 2")
    documentInvoker.read()
    documentInvoker.write("Dong thu 3")
    documentInvoker.read()
    documentInvoker.undo()
    documentInvoker.undo()
    documentInvoker.undo()
    documentInvoker.undo()