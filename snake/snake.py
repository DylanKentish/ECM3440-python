# SNAKES GAME
# Use ARROW KEYS to play, SPACE BAR for pausing/resuming and Esc Key for exiting

import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

class Snake:
    _coords = [[4,10], [4,9], [4,8]]  # Initial snake co-ordinates

    def insert( self, pos, xy ):
        self._coords.insert(pos, xy)
    def y(self):
        return self._coords[0][0]
    def x(self):
        return self._coords[0][1]
    def len(self):
        return len(self._coords)
    def head(self,x=None,y=None):
        if x != None:
            self._coords[0][1] = x
        if y != None:
            self._coords[0][0] = y
        return self._coords[0]
    def coords(self):
        return self._coords

def main():

    curses.initscr()
    win = curses.newwin(20, 60, 0, 0)
    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)   # Do not wait for user input

    key = KEY_RIGHT                                                    # Initializing values
    score = 0

    snake = Snake()

    food = [10,20]                                                     # First food co-ordinates

    win.addch(food[0], food[1], '*')                                   # Prints the food

    while key != 27:                                                   # While Esc key is not pressed
        win.border(0)
        win.addstr(0, 2, 'Score : ' + str(score) + ' ')                # Printing 'Score' and
        win.addstr(0, 27, ' SNAKE ')                                   # 'SNAKE' strings
        win.timeout(150 - int(snake.len()/5)%120)                      # Increases the speed of Snake as its length increases

        prevKey = key                                                  # Previous key pressed
        event = win.getch()
        key = key if event == -1 else event


        if key == ord(' '):                                            # If SPACE BAR is pressed, wait for another
            key = -1                                                   # one (Pause/Resume)
            while key != ord(' '):
                key = win.getch()
            key = prevKey
            continue

        if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # If an invalid key is pressed
            key = prevKey

        # Calculates the new coordinates of the head of the snake. NOTE: len(snake) increases.
        # This is taken care of later at [1].
        snake.insert(0, [snake.y() + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake.x() + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

        # If snake crosses the boundaries, make it enter from the other side
        if snake.y() == 0: snake.head(y=18)
        if snake.x() == 0: snake.head(x=58)
        if snake.y() == 19: snake.head(y=1)
        if snake.x() == 59: snake.head(x=1)

        # Exit if snake runs over itself
        #if snake.coords[0] in snake.coords[1:]: break


        if snake.head() == food:                                            # When snake eats the food
            curses.beep()
            food = []
            score += 1
            while food == []:
                food = [randint(1, 18), randint(1, 58)]                 # Calculating next food's coordinates
                if food in snake.coords(): food = []
            win.addch(food[0], food[1], '*')
        else:
            last = snake.coords().pop()                                          # [1] If it does not eat the food, length decreases
            win.addch(last[0], last[1], ' ')
        win.addch(snake.y(), snake.x(), '#')

    curses.endwin()
    print("\nScore - " + str(score))

if __name__ == "__main__":
    main()
