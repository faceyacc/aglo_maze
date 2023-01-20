from graphics import Window
from cell import Cell
def main():
    win = Window(800, 600)


    cell_1 = Cell(window=win)
    cell_1.draw(550, 550, 300, 300)
    
    cell_2 = Cell(window=win)
    cell_2.draw(100, 100, 200, 200)

    cell_1.draw_move(cell_2)


    win.wait_for_close()


if __name__ == "__main__":
    main()