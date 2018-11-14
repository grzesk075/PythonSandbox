import random


class Dog:
    """The __doc__ of general dog class."""

    tricks = ['roll over', 'play dead']  # class variable shared by all instances (like static in java)
    
    def __init__(self, name):  # constructor
        self.name = name       # instance variable unique to each instance
        
    def play(self):
        print(self.name, ':', random.choice(Dog.tricks))  # Dog.tricks is equivalent for self.tricks


myDog = Dog('Spike')
yourDog = Dog('Buddy')

for i in range(2):
    myDog.play()
    Dog.play(myDog)  # equivalent to myDog.play()
    yourDog.play()
    print(i, '\n')

myDog.tricks.append('jump')
print('Appended to class variable (visible for all instances):', yourDog.tricks)

myDog.newDynamicFunction = lambda d: d.name  # append an dynamic function only to myDog instance
print('Execution of new function:', myDog.newDynamicFunction(myDog))  # works
# print(yourDog.newDynamicFunction(yourDog)) it doesn't work
print('MyDog features:', dir(myDog))
print('YourDog features:', dir(yourDog))
print('Dog features:', dir(Dog))


class Greyhound(Dog):  # inheritance ('chart' in polish)
    def __init__(self, name, speed):
        if not isinstance(speed, float):
            raise Exception('Speed must be a float number')
        self.speed = speed
        # we can run superclass constructor only explicitly - the equivalent is: Dog.__init__(self,name)
        super(Greyhound, self).__init__(name)
        # private only by convention (like 'self' is only a naming convention)
        # (___p three or more underscores are automatically mangled with _Greyhound___p)
        self._memberConsideredAsPrivate = []


hound = Greyhound('Fastie', 12.0)
print('Hound name:', hound.name)
print('Hound isinstance of Greyhound, Dog, type, object:', isinstance(hound, Greyhound), isinstance(hound, Dog),
      isinstance(hound, type), isinstance(hound, object))

type(hound)  # <class 'Greyhound'>
type(Greyhound)  # <class 'type'>
dir(Greyhound)  # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'play', 'tricks']
help(Dog)  # prints __doc__

'''
Use it as a multi-line comment in Python.
'''

'''
class Dog(object)
 |  The __doc__ of general dog class.
 |  
 |  Methods defined here:
 |  
 |  __init__(self, name)
 |  
 |  play(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  tricks = ['roll over', 'play dead']
'''
