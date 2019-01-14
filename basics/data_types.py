import sys

int_huge = 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
int_small = -3

print('Empty int is an object int instance and takes many bytes dependent on the machine: ', sys.getsizeof(int()))
print('Variable %s of type %s has size in bytes %d' % ('int_huge', type(int_huge), sys.getsizeof(int_huge)))
print('Variable %s of type %s has size in bytes %d' % ('int_small', type(int_small), sys.getsizeof(int_small)))

print('int_huge =', int_huge)
print('int_small =', int_small)

print('int maxsize in bytes is sys.maxsize =', sys.maxsize)  # dependents of available memory

print('double precision float IEEE-754 is implement in Python3 with all limitations')
print('0.1 * 0.1 =', 0.1 * 0.1)

float_huge = 1234567890123456789012345678901234567890.123456789012345678901234567890123456789012345678901234567890
float_small = -3.0

print('Empty float is an object float instance and takes many bytes dependent on the machine: ', sys.getsizeof(float()))
print('Variable %s of type %s has size in bytes %d' % ('float_huge', type(float_huge), sys.getsizeof(float_huge)))
print('Variable %s of type %s has size in bytes %d' % ('float_small', type(float_small), sys.getsizeof(float_small)))

print('float_huge =', float_huge)
print('float_small =', float_small)
