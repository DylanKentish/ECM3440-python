from dataclasses import dataclass

@dataclass
class Thing:
    a : int = 0
    b : str = "hello"

t1 = Thing()
t2 = Thing(1,"world")
t3 = Thing(0, "hello")

print(t1)
if t1 == t3:
    print("They're equal")