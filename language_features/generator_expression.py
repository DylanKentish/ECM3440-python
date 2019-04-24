# Generator comprehensions can be returned  by functions. i.e. the comprehension 
# is returned, not the result of the comprehension.
def my_generator(x):
    return ("n is " + str(n) for n in range(x))

# Create an instance of the generator.
gen = my_generator(5)

# When using a generator in a while loop use next() to yield the next element.
print("with next " + next(gen))

# More usual, is to use a for loop. Note this only yields the remaining elements.
for s in gen:
    print("in for loop " + s)
