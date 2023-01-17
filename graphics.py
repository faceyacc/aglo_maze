from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__root = Tk()

        # Set title
        self.__root.title("Maze Runner")

        # create a Canvas 
        self.__canvas = Canvas(self.__root, bg="white", width=self.__width, height=self.__height)

        # Pack the canvas 
        self.__canvas.pack(expand=1, fill=BOTH)        

        # Create data member to rep that the window is running 
        self.__window_running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)
          
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__window_running = True
        while self.__window_running:
            self.redraw()

    def close(self):
        self.__window_running = False
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, fill_color="red"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
        canvas.pack(expand=1, fill=BOTH)
