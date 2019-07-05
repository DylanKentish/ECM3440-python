# method_decorator.py

import functools

class hi_there(object):
    def __init__(self, func):
        print("We're getting ready...")
        self.func = func
 
    def __call__(self,*args):
        print("It's happening...", self.func.__name__)
        return self.func(*args)
    
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        print("An instance method...")
        return functools.partial(self.__call__, obj)

class Counter:
    # Attributes
    count : int = 0

    # Methods
    @hi_there
    def increment(self) -> int:
        self.count += 1
        return self.count
    
    @hi_there
    def decrement(self) -> int:
        self.count -= 1
        return self.count

    def reset(self) -> None:
        self.count = 0

    @staticmethod
    @hi_there
    def sayHello():  # note, no 'self' argument
        print("hello")
        return

items_a = Counter()

print(items_a.count)
print(items_a.increment())
print(items_a.decrement())
Counter.sayHello()
# Note calling static method from instance is allowed
# because we used @staticmethod decorator.
items_a.sayHello()
