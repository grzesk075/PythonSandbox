print("Hello World")

sentence = """Multi line
sentence with parameters p1=%d, p2=%s""" % (25, 'abc')

if True:
    # block 1
    
    print('Block 1')
    print("true " + sentence)
    
    # end of block 1
else:
    print("Block 2")
    print("false")

import sys; sep = '==='; sys.stdout.write('\n' + sep + '\n')  # semicolons only in line

a, b, c = 1, 1.2, 'john smith'
del a, b
a = c[0:4]
print(a)  #john

nothing = None
print('Null concept is named:', nothing, sep=' ', end='\n\n')

inp = input('Write sth.:\n')
print(inp)

input('Any key for exit\n')
