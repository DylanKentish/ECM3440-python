import asyncio
import sys
#import selectors
#import tty
import threading

in_count = 0

async def print_screen():
    global in_count
    out_count = 0
    while True:
        await asyncio.sleep(1)
        scr = f""
        for row in range(20):
            scr += f"{row:02}\n"
        print(scr, end="")
        print(f"{in_count:04} {out_count:04}")
        out_count += 1

async def update_game():
    global in_count
    while True:
        await asyncio.sleep(0.1)
        in_count += 1
        #print("*",end="")
            

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
