### Classes and decorators

**Exercise** - write a decorator which times the execution of functions or methods.

### Generators and yield

```python
def my_generator(count):
    n = 0
    while n < count:
        yield "n is " + str(n)
        n += 1

for s in my_generator(4):
    print(s)
```

**Exercise** - rewrite my_generator() using a *generator expression*.

**Exercise** - rewrite my_generator() to return a *list* rather than using `yield`.

### F strings

**Exercise** - write an f string that prints the current time
using a 24 hour clock style, e.g. **08:30**.

### Data classes

**Exercise** - write a data class, then add your
own `__repr__` to return a string using
only upper case letters.
