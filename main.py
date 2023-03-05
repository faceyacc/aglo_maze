from graphics import Window
from cell import Cell
from maze import Maze
def main():

    screen_x = 600
    screen_y = 500
    margin = 20
    num_rows = 8
    num_cols = 9 
    cell_size_x = 55
    cell_size_y = 55
    # testing



    win = Window(screen_x, screen_y)

    m1 = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win=win)
    m1.solve()


    win.wait_for_close()


if __name__ == "__main__":
    main()