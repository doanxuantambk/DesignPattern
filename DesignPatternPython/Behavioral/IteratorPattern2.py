import time
from collections.abc import Iterator, Iterable
def fib():
    a, b = 0, 1
    while b<100:
        yield b
        a, b = b, a+b

g = fib()
print("===Iterator 1")
for e in g:
    print(e)


print("===Iterator 2")
g2 = fib()
try:
    while True:
        x = next(g2)
        print(x)
except StopIteration:
    pass

def count_to(count):
    numbers = ["one", "two","three","four","five","six"]
    for number in numbers[:count]:
        yield number

count_to_two = lambda: count_to(2)
count_to_five = lambda: count_to(5)

def main():
    print("===Iterator 3")
    for n in count_to_two():
        print(n)

    print("===Iterator 4")
    try:
        itera = count_to_five()
        while True:
            it = next(itera)
            print(it)
    except StopIteration:
        pass



if __name__ == "__main__":
    main()
