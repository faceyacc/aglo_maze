from graphics import Window
from cell import Cell
from maze import Maze
def main():
    win = Window(800, 600)

    Maze(20,20, 5, 5, 55, 55, win=win)


    win.wait_for_close()


if __name__ == "__main__":
    main()