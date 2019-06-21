# function_decorator.py


def my_decorator(func):
    def wrapped_fn():
        print("begin")
        func()
        print("end")
    return (wrapped_fn)


@my_decorator
def do_something():
    for n in range(5):
        print(n)


if __name__ == "__main__":
    do_something()
