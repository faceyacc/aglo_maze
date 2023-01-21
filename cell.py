from graphics import Line, Point

class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._window = window
        self.visited = False
    
    # Getters for coordinates
    def get_x1(self):
        return self._x1
    
    def get_y1(self):
        return self._y1

    def get_x2(self):
        return self._x2

    def get_y2(self):
        return self._y2     

    def get_window(self):
        return self._window           

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.get_window().draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.get_window().draw_line(line, "white")            
            
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.get_window().draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.get_window().draw_line(line, "white")            
        
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.get_window().draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.get_window().draw_line(line, "white")            

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.get_window().draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.get_window().draw_line(line, "white")            

    def draw_move(self, to_cell, undo=False):
        if self.get_window() is None:
            return 

        # Get first cell's mid point
        first_cell_x = (self.get_x1() + self.get_x2()) / 2
        first_cell_y = (self.get_y1() + self.get_y2()) / 2
        first_cell_mid_point = Point(first_cell_x, first_cell_y)

        # Get second cell's mid point
        second_cell_x = (to_cell._x1 + to_cell._x2) / 2
        second_cell_y = (to_cell._y1 + to_cell._y2) / 2
        second_cell_mid_point = Point(second_cell_x, second_cell_y)
        fill_color = "red"

        if undo:
            fill_color = "grey"

        line = Line(first_cell_mid_point, second_cell_mid_point)
        self.get_window().draw_line(line, fill_color=fill_color)