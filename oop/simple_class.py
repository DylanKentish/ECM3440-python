# simple_class.py

class Counter:
    # Attributes
    count : int = 0

    # Methods
    def increment(self) -> int:
        self.count += 1
        return self.count
    
    def decrement(self) -> int:
        self.count -= 1
        return self.count

    def reset(self) -> None:
        self.count = 0

    @staticmethod
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
