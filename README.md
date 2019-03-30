# ECM3440-python

## Advanced Python examples and exercises

These examples assume a reasonable knowledge of Python, and are intended to extend your
knowledge to include language features used in web programming.

### Rationale

If you've learned Python as an introduction to programming you might at times
struggle to read and
understand Python code written by others. This is because Python has many features that aren't taught in
introductory courses, but are important when using web frameworks and other larger software
environments.

## Language features

### Type hints and linting

If you edit your Python scripts using an editor, or
IDE, that has Python editing features you will be aware that many programming errors,
particularly syntax errors, can be spotted by editors. This form of program checking is called 'linting' because the first such static testing program was called 'lint' as it found the 'fluff' in your programs.  

Like code reviews conducted by human reviewers there is no requirement that the program is complete or even that it is syntactically correct. 
Static testing isn't limited to finding syntax errors, which you
would find out about soon enough when they prevent your program from running. Linting can also
find semantic errors such as unreachable lines of code.

 As Python is a dynamically typed language, there is another sort of error that we encounter, the `TypeError`.  For example a common mistake is to write something like this:

```python
num = input("type a number ")
if num == 1:
    # do something
elif num == 2:
    # do something else
else:
    # etc
```

This is perfectly valid Python but the result of the `input()` function is
always a string, so this will not work as intended.

```python
num : int = input("type a number ")
if num == 1:
    # do something
elif num == 2:
    # do something else
else:
    # etc
```

By adding a *type hint*, in this case `: int`, we instruct the linter to check that all uses of the variable `num` are consistent with an integer type. When this code is linted the following error is shown:

```none
lint_fragment.py:1: error: Incompatible types in assignment (expression has type "str", variable has type "int")
```
Note that this is a linting error, in this case the output of the `mypy` program, not a Python interpreter error. The program will still run, and its behaviour is still
incorrect, but we now know there is an error to be fixed.

*Type hints* are especially useful for function signatures. Note that the return type is also hinted.  For functions that do not return a value use `-> None`.

```python
def my_func(my_arg:str, count:int=1) -> str:
```

#### Static checking tools

* <http://mypy-lang.org/>

* <https://www.pylint.org/>

* <https://code.visualstudio.com/docs/python/linting>

### Classes and decorators

Classes, or objects, are user defined *types*.  Unlike other object oriented languages, for example Java, all attributes and methods are *public*.  Here is a very simple example:

```python
class Counter:
    # Attributes
    count = 0

    # Methods
    def increment(self):
        self.count += 1
        return self.count

    def decrement(self):
        self.count -= 1
        return self.count

    def reset(self):
        self.count = 0
```

When designing your own classes it would be wise to make
use of *type hints*.  

Another feature of Python is
*decorators*. It is important to note that unlike *type hints*, *decorators* do change the behaviour of methods.  For example we can add a static method to our class.

```python
class Counter:
    # Attributes
    _count : int

    # Constructor
    def __init__(count : int = 0):
        self._count = count

    @staticmethod
    def sayHello():  # note, no 'self' argument
        print("hello")
        return
```

Another important method *decorator* is `@property`. See <https://docs.python.org/3.5/library/functions.html#property>



<https://realpython.com/python-metaclasses/>

### Generators and yield

You will be familiar with `range()`, which is often used in `for` loops like this:

```python
for n in range(3,13,3):
    print(n)
```

In Python We can write our own generators by using the `yield` keyword rather than  `return`, like this:

```python
def my_generator(count):
    n = 0
    while n < count:
        yield "n is " + str(n)
        n += 1

for s in my_generator(4):
    print(s)
```

<https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/>

### Miscellaneous new features

From time to time new features are added to the Python
language.  These new features rarely make earlier
features obsolete, as this would break many existing
programs. Instead new features typically provide
and easier or tidier way of doing common things.

#### F strings

An *f string* is a Python string literal with the letter *f* before the opening quote. Within the string the value of
named variables can be included using a simple brace
notation.

 <https://realpython.com/python-f-strings/>

**Exercise** - write an f string that prints the current time
using a 24 hour clock style, e.g. **08:30**.

#### Data classes

Another application of *decorators* is with the `dataclass` module.  Using the `@dataclass` decorator will automatically
create a constructor method `__init__`, and also `__repr__` and `__eq__` methods.

<https://realpython.com/python-data-classes/>


## Programming styles and patterns

Being familiar with the syntax of a programming language and the libraries of functions available is only a part of the skills needed to turn designs into
working software.  There are various programming styles, or idioms, and patterns that enable programmers to create high quality software.

### Pure functions and methods

It is worth noting that the methods of built in Python *types* such as `str` and `dict` are *pure*, by which it is meant that they have no side effects. Those new to Python are
sometimes caught out by this, especially the string methods such as `upper()`. For example:

```python
name = "Bob"
name.upper()
print(name)
```

This prints `Bob`, whereas this:

```python
print("Bob".upper())
```
gives `BOB`.

A corrected form of the first example is often given as:

```python
name = "Bob"
name = name.upper()
print(name)
```
This code recognizes that Python strings are *immutable*. The string methods such as `upper()` give new strings as return values.  One consequence of this is that we can write code such as this:

```python
label = "a&b".replace("&","_").upper().rjust(8)
```

This style of programming is called *functional programming*.

## Callbacks

In Python functions, and methods, are objects.  This means we can assign a function to a variable.


## Wrappers and decorators

When a decorator is applied
to a method or function it wraps the function in another function.

**Exercise** - write your own decorator which times the
execution of functions or methods.

## Concurrency

Programs that run continuously will generally need to accept new input, create output and perform some data transformation at the same time. This is called `concurrency` and can be achieved in numerous ways. This is a big subject with a lot of
theoretical and practical considerations.  For the purposes of designing and
developing business applications it isn't necessary to consider parallel computation of the type that might be used in scientific programming or 3D graphics.

### Coroutines

An event loop runs in a thread (typically the main thread) and executes all callbacks and Tasks in its thread. While a Task is running in the event loop, no other Tasks can run in the same thread. When a Task executes an await expression, the running Task gets suspended, and the event loop executes the next Task.
<https://docs.python.org/3/library/asyncio-dev.html>

<https://docs.python.org/3/library/asyncio-task.html>

### Threads

<https://pymotw.com/2/threading/>

<https://docs.python.org/3/library/threading.html>

### Multiprocessing

This is an alternative style of concurrency that uses capabilities built into the operating system.  It is effectively equivalent to running two, or more, copies of the Python interpreter, all running the same Python program but at any given time running different functions or using different data.

<https://docs.python.org/3/library/multiprocessing.html>


### More patterns

<https://github.com/faif/python-patterns>

## Building, testing and debugging

<https://docs.travis-ci.com/user/languages/python/>

<https://jeffknupp.com/blog/2016/12/09/how-python-linters-will-save-your-large-python-project/>

### Modules and packages

* ```__init__.py```

* pip
<https://pypi.org/project/pip/>

## APIs

For detailed information see
<https://docs.python.org/3/library/internet.html>

### `urllib`

The `urllib` package provides functions and classes for accessing Internet resources
using URLs.


### WSGI

The Web Server Gateway Interface (WSGI) is a standard interface between web server software and web applications written in Python. It's not something you need to know
the details of as there are Python frameworks that will do the hard work for you.

Frameworks like `bottle` and `flask` make it easy to process web *forms*, handle uploading and downloading of files, and other capabilities required of web sites.

`bottle` example

```python
from bottle import route, run

@route('/')
def home():
    return '<h1>Homepage</h1>'

@route('/hello/<name>')
def hello(name):
    return f'<b>Hello {name}</b>!'

run(host='localhost', port=8080)
```

<https://bottlepy.org/docs/dev/>

`flask` example

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Homepage</h1>'

@app.route('/hello/<name>')
def hello(name):
    return f'<b>Hello {name}</b>!'

app.run(host='localhost', port=8080)
```

<http://flask.pocoo.org/>


**Deployment** https://bottlepy.org/docs/dev/deployment.html


Video: You Don't Need That! <https://www.youtube.com/watch?v=imW-trt0i9I> Christopher Neugebauer


## Unit testing

Essential for TDD

### `unittest`

For examples of significant project that use ```unittest``` see,

* <https://github.com/django/django>

* <https://github.com/scrapy/scrapy>

* <https://github.com/faif/python-patterns>

Using ```pytest``` see,

* <https://github.com/pallets/flask>


## Where next?

There' always more to learn.

For data analysis see <https://pandas.pydata.org/>

For multidimensional data see <http://www.numpy.org/>

For machine learning <https://scikit-learn.org/stable/>

Or maybe write an arcade style game <http://arcade.academy/>

### Web functions and serverless

Google Appengine...

<https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/appengine/standard/firebase/firenotes/>

```sh
cd python-docs-samples/appengine/standard/firebase/firenotes
```

Example uses `flask`.

Mobile
<https://cloud.google.com/solutions/mobile/mobile-app-backend-services>

Java example <https://cloud.google.com/solutions/mobile/mobile-firebase-app-engine-flexible>

Azure...
<https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python>
<https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference>