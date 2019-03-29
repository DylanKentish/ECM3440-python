# generator.py

# You're already familiar with range()
# range() is a generator

for n in range(3,13,3):
    print(n)

# We can write our own generators by using
# yield rather than return
def my_generator(count):
    n = 0
    while n < count:
        yield "n is " + str(n)
        n += 1

for s in my_generator(4):
    print(s)

for s in my_generator(5):
    print(s)
