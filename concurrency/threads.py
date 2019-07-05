# threads.py
import threading
import time

def say_after(delay, what):
    print(f"say_after started at {time.strftime('%X')}")
    time.sleep(delay)
    print(what)
    print(f"say_after finished at {time.strftime('%X')}")

def main():

    t1 = threading.Thread( target=say_after, args=(1, 'hello') )
    t2 = threading.Thread( target=say_after, args=(2, 'world') )

    print(f"main started at {time.strftime('%X')}")

    t1.start()
    t2.start()

    # Optionally wait for threads to end.
    # Try without these and see what happens.
    #t2.join()
    #t1.join()
    print(f"main finished at {time.strftime('%X')}")

main()

# Following code registers an exit handler.
# More than one exit handler is allowed, but all
# will run after the last thread has finished.
def exit_time():
     print(f"exit at {time.strftime('%X')}")

import atexit
atexit.register(exit_time)