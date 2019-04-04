import asyncio
import sys
import selectors
import tty

sel = selectors.DefaultSelector()
sel.register(sys.stdin, selectors.EVENT_READ)


# This is messy, need another thread here.
async def get_input(msg):
    while True:
        await asyncio.sleep(0)
        print(" \b",end="")
        events = sel.select(0)
        if events:        
            ch = sys.stdin.read(1)[0]
            print(msg, ch)

async def print_message(msg):
    print(msg + "   ",end="")
    while True:
        for ch in "|/-\\":
            await asyncio.sleep(0.2)
            print(f"\b\b{ch} ",end="")
            

async def main():
    tty.setcbreak(sys.stdin)
    task1 = asyncio.create_task(print_message('hello'))
    task2 = asyncio.create_task(get_input('hello'))
    await task1
    await task2

asyncio.run(main())