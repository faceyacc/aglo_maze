from graphics import Window
from cell import Cell
def main():
    win = Window(800, 600)
    cell_1 = Cell(window=win)
    cell_1.has_bottom_wall = False
    cell_1.draw(200, 200, 300, 300)
    
    cell_2 = Cell(window=win)
    cell_2.has_right_wall = False
    cell_2.draw(400, 200, 500, 300)
    win.wait_for_close()


if __name__ == "__main__":
    main()