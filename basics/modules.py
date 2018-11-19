import basics.fibo
from basics.fibo import fib as fibonacci
from package1.package2 import module1
import sys

sys.path.append('/my/appended/path')
print('Modules can be load by import from:', sys.path)

print(basics.fibo.fib(10000))
print(fibonacci(10))

print('Fibo module items:', dir(fibonacci))  # dir() lists items defined in python shell
print('Fibo is a module:', basics.fibo)

module1.hello()
print('Package of module1: ', module1.__package__)
