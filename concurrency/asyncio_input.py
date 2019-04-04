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

    def __repr__(self) -> str:
        out = ""
        for row in self.data:
            out += "".join(row) + "\n"
        return out 

class Snake:
    def __init__(self, head, len):
        self.data = [head]
        for i in range(len-1):
            xy = self.data[-1]
            xy = (xy[0],xy[1]+1)
            self.data.append(xy)

    def draw(self, scr:Screen) -> None:
        for xy in self.data:
            scr.draw(xy,"#")
        return


in_count = 0
scr = Screen(20,20)
snk = Snake((3,1),3)

async def print_screen():
    global in_count, scr
    out_count = 0
    while True:
        await asyncio.sleep(0.05)
        scr.clear()
        scr.draw((in_count%20,in_count%20),"*")
        snk.draw(scr)
        print(scr)
        print(f"{in_count:04} {out_count:04}")
        out_count += 1

async def update_game():
    global in_count
    while True:
        await asyncio.sleep(0.2)
        in_count += 1

            

async def main():
    task1 = asyncio.create_task(print_screen())
    task2 = asyncio.create_task(update_game())
    await task1
    await task2

class inputThread (threading.Thread):
    def run(self):
        while True:
            a = input()
            print(f"you typed: {a}")
            if a == "q":
                break

thread1 = inputThread()
thread1.start()
asyncio.run(main())
print("loop done")
thread1.join()
