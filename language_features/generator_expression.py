# Generator expressions can be returned by functions. i.e. the generator
# is returned, not the result of the generator.
def my_generator(count):
    return("n is " + str(n) for n in range(count))

# Create an instance of the generator.
gen = my_generator(4)

# When using a generator in a while loop use next() to yield the next element.
print("with next " + next(gen))

# More usual, is to use a for loop. Note this only yields the remaining elements.
for s in gen:
    print("in for loop " + s)
