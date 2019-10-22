from collections.abc import Iterable, Iterator

class MyCountIterable(Iterable):
    def __iter__(self):
        return MyCountIterator(self.value)

    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

class MyCountIterator(Iterator):
    def __next__(self):
        if self.index < self.value:
            Index = self.index
            self.index += 1
            return Index
        else:
            raise StopIteration()

    def __iter__(self):
        return self

    def __init__(self, value) -> None:
        super().__init__()
        self.value = value
        self.index = 0

firstCount = MyCountIterable(5)
list(firstCount)

firstCountIter = iter(firstCount)
try:
    while True:
        it = next(firstCountIter)
        print(it)
except StopIteration:
    pass