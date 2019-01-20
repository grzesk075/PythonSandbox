"""
Yield is instead return.
This makes a function a generator.
The local variables are suspended until next execution by caller.
Function next() resumes from point after last yield.
"""


def intgen(value=0):
    yield value
    while True:
        value += 1
        yield value


my_generator = intgen(5)

for i in my_generator:
    print(i)
    if i >= 10:
        break


print(next(my_generator))
print(my_generator.send(20))  # works when value = yield exists in generator function
print(next(my_generator))
my_generator.close()
