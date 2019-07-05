# type-hints.py
# 

# Can declare type of variable
name : str = "michael"
# But don't have to
num = 2

# Also function arguments and return value
def my_func(my_arg:str, count:int=1) -> str:
    return my_arg*count

print(my_func("x"))
print(my_func(name,num))
# However, these are only type hints
# This still works, and prints 333
print(my_func(111,3))
