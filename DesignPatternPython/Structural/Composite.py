from abc import abstractmethod

class FileComponent:
    @abstractmethod
    def showProperty(self):
        pass

    @abstractmethod
    def totalSize(self):
        pass

class FileLeaf(FileComponent):
    def __init__(self, name, size):
        super().__init__()
        self.__name = name
        self.__size = size

    def showProperty(self):
        print("FileLeaf[name=%s, size=%s]" %(self.__name, self.__size))

    def totalSize(self):
        return self.__size

class FolderComposite(FileComponent):
    __files = []

    def showProperty(self):
        for f in self.__files:
            f.showProperty()

    def totalSize(self):
        total = 0
        for f in self.__files:
            total += f.totalSize()
        return total

    def __init__(self, files) -> None:
        super().__init__()
        self.__files = files

if __name__ == "__main__":
    file1 = FileLeaf("File 1",10)
    file2 = FileLeaf("File 2",5)
    folder = FolderComposite([file1, file2])
    folder.showProperty()
    print("Total size: %s" %(folder.totalSize()))
