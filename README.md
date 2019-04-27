# ECM3440-python

## Advanced Python examples and exercises

These examples assume a reasonable knowledge of Python, and are intended to extend your
knowledge to include language features used in web programming.

### Rationale

If you've learned Python as an introduction to programming you might at times be confused by code written by others, or examples for the many Python libraries and frameworks. Python has many features that aren't taught in introductory courses, but are important when using larger software environments.

## More language features

From your introductory Python classes you should be familiar with
variables, built in types, statements, keywords, functions, modules and namespaces. I won't go back over those, instead I'll introduce some more Python language features that should help you create better
programs.

### Type hints and linting

If you edit Python scripts using an editor, or
IDE, that has Python editing features you will be aware that many programming errors,
particularly syntax errors, can be spotted by editors. This form of program checking is called 'linting' because the first such static testing program was called 'lint' as it found the 'fluff' in your programs.  

Like code reviews conducted by human reviewers there is no requirement that a program checked by a linter is complete, or even that it is syntactically correct. Liniting is therefore particularly useful when editing.

Static testing isn't limited to finding syntax errors, which you would find out about soon enough when they prevent your program from running. Linting can also find semantic errors such as unused variables and unreachable lines of code.


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
always a string, so this will not work as intended. However, if  we
add *type hints* to our program the linter can help us
avoid this mistake.

```python
# With type hint
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

Although static checking through an IDE is the most frequently used approach, linters and other static checking tools can be run from
the command line and also used as part of the software test, build,
and release activities.

Here are some tools for Python programmers.

* <http://mypy-lang.org/>

* <https://www.pylint.org/>

* <http://flake8.pycqa.org/en/latest/>

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

You might also encounter `@classmethod`. See <https://docs.python.org/3/library/functions.html#classmethod>

When a decorator is applied
to a method or function it wraps the function in another function.

**Exercise** - write your own decorator which times the
execution of functions or methods.

<https://realpython.com/python-metaclasses/>

### Generators and yield

You will be familiar with `range()`, which is often used in `for` loops like this:

```python
for n in range(3,13,3):
    print(n)
```

Although we might think of range() as returning a list, it actually produces a new value for each iteration of the `for` loop.  We call functions, or classes, like this *generators*.
In Python We can write our own generators by using the `yield` keyword rather than `return`, like this:

```python
def my_generator(count):
    n = 0
    while n < count:
        yield "n is " + str(n)
        n += 1

for s in my_generator(4):
    print(s)
```

**Exercise** - rewrite my_generator() without using
`yield`. Hint use a *list* and the `append()` method.

**Exercise** - rewrite my_generator() using a *generator expression*.

Further reading on generators 
<https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/>

### Miscellaneous new features

From time to time new features are added to the Python
language.  These new features rarely make earlier
features obsolete, as this would break many existing
programs. Instead new features typically provide
an easier, or tidier, way of doing common things.

#### F strings

An *f string* is a Python string literal with the letter *f* before the opening quote. Within the string the value of
named variables can be included using a simple brace
notation.

```python
today = "Monday"
tomorrow = "Tuesday"
print(f"1. Today is {today}, and tomorrow is {tomorrow}.")

```
 <https://realpython.com/python-f-strings/>

**Exercise** - write an f string that prints the current time
using a 24 hour clock style, e.g. **08:30**.

#### Data classes

Another application of *decorators* is with the `dataclass` module.  Using the `@dataclass` decorator will automatically
create a constructor method `__init__`, and also `__repr__` and `__eq__` methods.

<https://realpython.com/python-data-classes/>

**Exercise** - write a data class, then add your
own `__repr__` to return a string using
only upper case letters.

## Programming styles and patterns

Being familiar with the syntax of a programming language and the libraries of functions and classes available is only a part of the skills needed to turn designs into
working software.  There are various programming styles, or idioms, and patterns that enable programmers to create high quality software.

### Pure functions and methods

The methods of built-in Python *types* such as `str` and `dict` are usually *pure*, by which we mean that they have no side effects. Those new to Python are
sometimes caught out by this, especially when using the string methods such as `upper()`. For example:

```python
>>> name='Bob'
>>> name.upper() # Incorrect!
>>> name
'Bob'
```

The above code prints `Bob`, whereas this:

```python
>>> 'Bob'.upper()
'BOB'
```

gives `BOB`.  Once we are familiar with Python we know how
to use these string methods correctly but tend not to think
about why they work this way.

A corrected form of the first example is often given as:

```python
>>> name='Bob'
>>> name=name.upper()
>>> name
'BOB'
```

This code recognizes that Python strings are *immutable*. The string methods such as `upper()` give new strings as return values.  One consequence of this is that we can write code such as this:

```python
label = "a&b".replace("&","_").upper().rjust(8)
```

This style of programming is called *functional programming*, and requires that functions are *pure*.

### Callbacks

In Python functions, and methods, are objects.  This means we can assign a function to a variable and then call the function later using the variable.

```python
def func1(arg):
    print(f"func1 with arg {arg}")

def func2(arg):
    print(f"func2 with arg {arg}")

def caller(cb, msg):
    cb(msg)

caller(func1, "hello")
caller(func2, "bye")
```

References to functions can be passed as arguments to other functions, assigned to variables, or added to lists.

### More patterns

When programming in any object oriented language it is important not just to make use of re-usable components, but also to learn and make use of common design patterns.

See <https://github.com/faif/python-patterns>

## Multitasking and concurrency

Programs that run continuously will generally need to accept new input, create output and perform some data transformation at the same time.

When a computer system, or program, is performing two or more
operations at the same time it is called multitasking.  This is a big subject with a lot of
theoretical and practical considerations.
Multitasking
can be achieved in several ways, but there are two distinct
approaches to multitasking, *preemptive* and *non-preemptive*. It is important to note that neither of these approaches require multiple CPUs or *cores*.

### Preemptive multitasking

Preemptive multitasking is used by operating systems and some other
larger software systems to allow multiple programs, or tasks,
to run at the same time. Typically the programs running on such
a system have little control over when they are suspended to allow
other programs to run, although operating systems will usually
have a means of setting the priority of processes.

### Non-preemptive

Non-preemptive multitasking, or cooperative multitasking, requires
that the concurrent tasks periodically pause execution to allow
another task to execute. This is done by waiting in an idle state,
the wait could be for some external event, for example waiting
for a message to be received, or waiting for a timer.

### Coroutines and event loops

An event loop runs in a single thread, typically the main thread, and executes all callbacks and tasks in the one thread. These tasks are termed coroutines.

While a coroutine is running in the event loop, no other coroutine can run. When the running coroutine executes an `await` expression it gets suspended, and the event loop executes the next waiting task. This is a non-preemptive style of multitasking.

See
<https://docs.python.org/3/library/asyncio-dev.html>
and
<https://docs.python.org/3/library/asyncio-task.html>.


### Threads

Python provides two distinct models of preemptive multitasking, threads and *multiprocessing*.

Python threads are
implemented within the interpreter, and only one thread can
execute Python code at a time. Note this doesn't mean only
one function can be executing, as library calls often make calls
to operating system libraries, e.g. for reading and writing files.

<https://pymotw.com/2/threading/>

<https://docs.python.org/3/library/threading.html>

### Multiprocessing

Multiprocessing is an alternative style of concurrency that uses capabilities built into the operating system.  It is effectively equivalent to running two, or more, copies of the Python interpreter, all running the same Python program but at any given time running different functions or using different data.

<https://docs.python.org/3/library/multiprocessing.html>

### Futures

Futures are user defined objects
that are waited for using `await`.  

As the name
suggests, a *future* represents the result of an operation
that has not yet returned a value.

Note. In JavaScript *futures* are called *promises.


**Exercise** Read <https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python>

Explain what is meant by the following terms used in that document.

* global method

* non-blocking

* asynchronous coroutine

* relative import syntax

[GitHub repo <https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/azure-functions/functions-reference-python.md>]


## Modules and packages

### Modules

A Python module is a Python script that
provides functions, classes and variables that can be used by other
scripts by *importing*.

Python modules and the `import` statement ensure that items
declared in modules are in distinct *namespaces* using *dot notation*.

<https://docs.python.org/3/tutorial/modules.html>

### Packages

The use of modules and namespace can be taken further through
the use of *packages*.  A Python package is a collection of
Python modules. In practice this usually means a package is a
directory (or folder) containing several `.py` files and perhaps other
sub-directories.

When creating a package  it is important to create a file called ```__init__.py``` in each directory so that Python knows the directory
is a Python package. For more information on
creating packages see https://docs.python.org/3/tutorial/modules.html#packages

Packages are important for the distribution of
reusable Python libraries.

Pip is the package installer for Python.

**pip** <https://pypi.org/project/pip/>


<https://packaging.python.org/tutorials/packaging-projects/>

## Python libraries for the WWW

For detailed information see
<https://docs.python.org/3/library/internet.html>

### `urllib`

The `urllib` package provides functions and classes for accessing Internet resources
using URLs.

This fragment of code shows how JSON data can be read from a URL.
```python
api_url="http://echo.jsontest.com/name/mike/age/unknown"

with urllib.request.urlopen(api_url) as f:
    data_text:str = f.read().decode('utf-8')
    data = json.loads(data_text)
```

### WSGI

The Web Server Gateway Interface (WSGI) is a standard interface between web server software and web applications written in Python. It's not something you need to know
the details of, as there are Python frameworks that will do the hard work for you.

Frameworks like `bottle` and `flask` make it easy to process web *forms*, handle uploading and downloading of files, and other capabilities required of web sites. These frameworks
use decorators to associate callbacks with URL patterns. To read and understand such
programs it's necessary to be familiar with several programming idioms.

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


### logging

Logging libraries are almost universally used in server applications but can also make for better diagnostics of client applications too.

```python
import logging
logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)
## Levels are DEBUG, INFO, WARN, ERROR, CRITICAL

logger.debug()
logger.info()
logger.warn()
logger.error()
### Python also has
logger.critial()
### and for use in except blocks. Logs level is ERROR
logger.exception()
```

The Apache documentation provide some examples of the different logging levels.
<https://httpd.apache.org/docs/2.4/mod/core.html#loglevel>

* critical "socket: Failed to get a socket, exiting child"
* error "Premature end of script headers"
* warn "child process 1234 did not exit, sending another SIGHUP"
* notice "httpd: caught SIGBUS, attempting to dump core in ..."
* info "Server seems busy, (you may need to increase StartServers, or Min/MaxSpareServers)..."
* debug "Opening config file ..."

Note that Python logging does not have a "notice" level, which the Apache
documentation describes as "Normal but significant condition".

It is worth noting that Internet protocols use status codes with implied severity that will often relate to a logging level.  For example HTTP uses response codes where the initial digit corresponds various classes of success or failure in exchanging messages. <https://developer.mozilla.org/en-US/docs/Web/HTTP/Status>

* 1XX information
* 2XX success
* 3XX redirect
* 4XX client error (including 418, I'm a teapot)
* 5XX server error

FTP has similar status codes. Here are some examples.

* 125 Data connection already open; transfer starting
* 250 Requested file action okay, completed
* 332 Need account for login
* 430 Invalid username or password
* 534 Could Not Connect to Server - Policy Requires SSL

## Unit testing

Essential for TDD

### `unittest`

For examples of significant project that use ```unittest``` see,

* <https://github.com/django/django>

* <https://github.com/scrapy/scrapy>

* <https://github.com/faif/python-patterns>

Using ```pytest``` see,

* <https://github.com/pallets/flask>


## Building, testing and debugging

<https://docs.travis-ci.com/user/languages/python/>

<https://jeffknupp.com/blog/2016/12/09/how-python-linters-will-save-your-large-python-project/>


## Where next?

There' always more to learn.


For data analysis see <https://pandas.pydata.org/>

For multidimensional data see <http://www.numpy.org/>

For machine learning <https://scikit-learn.org/stable/>

Or maybe write an arcade style game <http://arcade.academy/>

<https://hackernoon.com/top-10-python-web-frameworks-to-learn-in-2018-b2ebab969d1a>

### Web functions and serverless

Google Appengine...

Use Flask with Google App Engine
<https://cloud.google.com/appengine/docs/standard/python3/building-app/writing-web-service>

<https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/appengine/standard/firebase/firenotes/>

<https://cloud.google.com/appengine/docs/standard/python/samples>


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