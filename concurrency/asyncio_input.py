import asyncio
import sys
import selectors

sel = selectors.DefaultSelector()
sel.register(sys.stdin, selectors.EVENT_READ)

async def get_input(msg):
    print(msg + "   ",end="")
    await asyncio.sleep(0.1)
    while True:
        for ch in "|/-\\":
            print(f"\b\b{ch} ",end="")
        events = sel.select(0)
        if events:
            
            line = sys.stdin.readline()
            print(msg, line)
            break


loop = asyncio.get_event_loop()
loop.run_until_complete(get_input('Type your name'))
loop.close()