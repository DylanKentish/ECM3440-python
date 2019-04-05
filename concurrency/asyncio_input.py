import asyncio
import sys
import threading

class Screen:
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
        self.clear()

    def clear(self) -> None:
        # Use list of lists of one character strings
        # to form a mutable array of strings
        self.data = []
        for y in range(self.height):
            self.data.append([' '] * self.width)

    def draw(self, xy:tuple, c:str) -> None:
        self.data[xy[1]][xy[0]] = c[0]
        return

    def wrap_xy(self, xy:tuple) -> tuple:
        return (xy[0] % self.width, xy[1] % self.height) 

    def __repr__(self) -> str:
        out = ""
        for row in self.data:
            out += "".join(row) + "\n"
        return out 

class Snake:
    scr : Screen
    direction : int = 0 # up,right,down,left
    def __init__(self, scr, head, len):
        self.data = [head]
        self.scr = scr
        for i in range(len-1):
            xy = self.data[-1]
            xy = (xy[0],xy[1]+1)
            self.data.append(xy)

    def draw(self) -> None:
        for xy in self.data:
            self.scr.draw(xy,"#")
        return

    def add(self,head) -> None:
        self.data.insert(0,self.scr.wrap_xy(head))
        self.data.pop()

    def move(self,dir=0) -> None:
        ''' dir=1 (clockwise)
        or dir=-1 (counterclockwise) '''
        self.direction = (self.direction + dir)%4
        ## add new segment.
        head = self.data[0]
        if self.direction == 0:
            head = (head[0],head[1]-1)
        elif self.direction == 1:
            head = (head[0]+1,head[1])
        elif self.direction == 2:
            head = (head[0],head[1]+1)
        else:
            head = (head[0]-1,head[1])
        self.add(head)
        return
    
    def grow(self) -> None:
        return

in_count = 0
scr = Screen(60,20)
snk = Snake(scr,(3,1),4)
rotate = 0

async def print_screen():
    global in_count, scr
    out_count = 0
    while True:
        await asyncio.sleep(0.05)
        scr.clear()
        scr.draw((in_count%20,in_count%20),"*")
        snk.draw()
        print(scr)
        print(f"{in_count:04} {out_count:04}")
        out_count += 1

async def update_game():
    global in_count, rotate
    while True:
        await asyncio.sleep(0.1)
        snk.move(rotate)
        rotate = 0
        in_count += 1      

async def main():
    task1 = asyncio.create_task(print_screen())
    task2 = asyncio.create_task(update_game())
    await task1
    await task2

class inputThread (threading.Thread):
    def run(self):
        global rotate
        while True:
            a = input()
            print(f"you typed: {a}")
            if a == "q":
                break
            elif a == "b":
                rotate = -1
            elif a == "n":
                rotate = 1

thread1 = inputThread()
thread1.start()
asyncio.run(main())
print("loop done")
thread1.join()
