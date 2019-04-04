import asyncio
import sys
import threading


class Screen:
    def __init__(self,width:int, height:int):
        self.width = width
        self.height = height
        self.clear()

    def clear(self) -> None:
        # Use list of lists of one character strings
        # to form a mutable array of strings
        self.data = [[' '] * self.width] * self.height

    def __repr__(self) -> str:
        out = ""
        for row in self.data:
            out += "".join(row) + "\n"
        return out 

in_count = 0
scr = Screen(20,20)

async def print_screen():
    global in_count, scr
    out_count = 0
    while True:
        await asyncio.sleep(0.1)
        print(scr)
        print(f"{in_count:04} {out_count:04}")
        out_count += 1

async def update_game():
    global in_count
    while True:
        await asyncio.sleep(0.01)
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
