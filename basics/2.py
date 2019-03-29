import sys

print('Encoding of file should be UTF-8')
print('Length of arguments: ', len(sys.argv))
print("Argument 0 (command without arguments):", sys.argv[0])

if len(sys.argv) > 1:
    print('First argument:', sys.argv[1])
else:
    print('No arguments')

# complex numbers and exponentiation (liczby zespolone i potęgowanie)
print('j^2=', 1j**2)  # (-1+0j)

# iterable type as a result from range and turning it into list
table = list(range(1, 4))
print('Range converted to list:', table)  # [1, 2, 3]

word = 'słowo'
print('Slice operation on str:', word[1:3])  # ło
print('Turning str to list and slicing it:', list(word)[1:3])  # ['ł', 'o']
del word  # removing variable

print('Formatting string {0}={val}'.format('arg0', val='abc'))  # Formatting string arg0=abc

# void statement as a placeholder when command is mandatory
pass


def fibonacci(n=100):
    """Returns a list containing the Fibonacci series up to n (default 100)."""
    result = []  # list
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


print('Fibonacci series up to 100:', fibonacci(), '\n')
print('Fibonacci series up to 500:', fibonacci(500), '\n')  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
print('Fibonacci doc:', fibonacci.__doc__, '\n')  # Fibonacci doc: Returns a list containing the Fibonacci series up to n (default 100).

pattern = 'abcde'
for s in ('a', 'e'):
    print('For loop:', s)
    if s not in pattern:
        break
else:
    print('Loop was not broken.')


def concat(*args, sep='/'):  # * means varargs, afterwards variables have names
    return sep.join(args)


concat.a = 4  # function can have attributes but it is not recomended
    
print('Concat using varargs: ', concat('a', 'b', 'c', sep='.'))  #  a.b.c

array = [1, 2, 3]
print('Unpacking from ', array, ' array->list:', *array)  # Unpacking from  [1, 2, 3]  array->list: 1 2 3

# Dictionaries are like association tables, keys are immutable and order is arbitrary
dictionary = {"n": 10}
print('Changing dictionary to keyword arguments with ** operator:', fibonacci(**dictionary))  # fibonacci(n=10)

from typing import (List, Tuple, Dict,
                    Callable, Set)  # line continuation inside parentheses
my_list_with_type_hine: List[str] = list()
my_list_with_type_hine.append('abc')

sumFunction = lambda x, y: x+y
print('Lambda function:', sumFunction(4, 6))  # 10

tuples = [(1, 'a'), (2, 'b'), (3, 'c')]  # list of tuples
tuples.sort(key=lambda p: -p[0])
print('Sorted tuples descending:', tuples)  # [(3, 'c'), (2, 'b'), (1, 'a')]


def fun(ham: str, eggs: str = 'eggs') -> str:  # -> None for void return
    """Annotation and types of function"""
    print("Annotations:", fun.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


print(fun.__doc__, ':', fun.__annotations__)  # Annotation and types of function : {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}

# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print('Squares list (using list comprehensions - generator expressions):', [x**2 for x in range(0, 10)])

# [(1, 2), (1, 3), (1, 4), (3, 1), (3, 2), (3, 4), (5, 1), (5, 2), (5, 3), (5, 4)]
print('Combination in tuple list - generator expression:', [(x, y) for x in [1, 3, 5] for y in range(1, 5) if x != y])

t = 1,2,3,4  # tuple (1, 2, 3, 4)
a,_,_,_ = t  # a = 1

letters = ['a', 'b', 'c', 'd']
b_idx = letters.index('b')  # 1
letters[0:2]  # ['a', 'b']
letters[-1:]  # ['d']
letters[-2:]  # ['c', 'd']
letters[-2:-1]  # ['c']

# yield keyword instead of return keyword is used for create generator, which is also an iterator
import random


def randomgen(s):
    for i in range(len(s)):
        yield random.choice(s)


for c in randomgen('abcde'):
    print('Randomized string by generator:', c)

# Tuples are immutable
tuple = 1, 2, 3  # packing a tuple
x, y, z = tuple  # unpacking a tuple

# list is an array and implements also queues functionality
print('Set is unique:', set('abracadabra'))  # {'c', 'r', 'b', 'd', 'a'}
print('Operations on sets |-^& and comprehensions:', {1, 2, 3} & {2, 3, 4})  # {2, 3}

it = iter('abcde')
print('Iterator', it)  # Iterator <str_iterator object at 0x03113410>
for c in it:
    print(c)


class MyIterator:
    def __init__(self):
        self.count = 0
    
    def __next__(self):
        self.count += 1
        if self.count == 10:
            raise StopIteration
        return self.count

    def __iter__(self):
        return self


for i in MyIterator():
    print('__next__ over iterator:', i)


def inc(i):
    """Increments number.
    Simple types like int, str are passed to function by value (value is copied to new memory slot).
    Class instances and e.g. lists are passed by reference."""
    i += 1
    return i


num = 8
print('Num incremented:', inc(num), ' and argument is unchanged:', num)

help(inc)
