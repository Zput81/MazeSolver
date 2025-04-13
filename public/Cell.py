from Point import Point
from Line import Line

class Cell:
    def __init__(self, x1, y1, x2, y2, win, visited):
        
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        
        self.__win = win
        
        self.__visited = False
    
    @property
    def visited(self):
        return self.__visited
    
    @visited.setter
    def visited(self, value):
        self.__visited = value
    
    
    def draw(self):
        
        if self.__win is not None:
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x1, self.__y2)
            line = Line(p1, p2)
            if self.has_left_wall:
                self.__win.draw_line(line, "black")
            else:
                self.__win.draw_line(line, "white")
            
            p1 = Point(self.__x2, self.__y1)
            p2 = Point(self.__x2, self.__y2)
            line = Line(p1, p2)
            if self.has_right_wall:
                self.__win.draw_line(line, "black")
            else:
                self.__win.draw_line(line, "white")
            
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x2, self.__y1)
            line = Line(p1, p2)
            if self.has_top_wall:
                self.__win.draw_line(line, "black")
            else:
                self.__win.draw_line(line, "white")

            p1 = Point(self.__x1, self.__y2)
            p2 = Point(self.__x2, self.__y2)
            line = Line(p1, p2)
            if self.has_bottom_wall:
                self.__win.draw_line(line, "black")
            else:
                self.__win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        
        if undo:
            color = "gray"
        else:
            color = "red"

        center_self_x = (self.__x1 + self.__x2) / 2
        center_self_y = (self.__y1 + self.__y2) / 2
        
        center_to_x = (to_cell.__x1 + to_cell.__x2) / 2
        center_to_y = (to_cell.__y1 + to_cell.__y2) / 2

        p1 = Point(center_self_x, center_self_y)
        p2 = Point(center_to_x, center_to_y)

        line = Line(p1, p2)
        if self.__win is not None:
            self.__win.draw_line(line, color)