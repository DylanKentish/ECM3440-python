from dataclasses import dataclass

@dataclass
class Thing:
    a : int = 0
    b : str = "hello"

t1 = Thing()
t2 = Thing(1,"world")
t3 = Thing(0, "hello")

# datclass gives us an __eq__ method
if t1 == t3:
    print("They're equal")

# dataclass also give us a printable string version
# using the __repr__ method
print(t1)

