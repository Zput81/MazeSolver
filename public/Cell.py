from Point import Point
from Line import Line

class Cell:
    def __init__(self, x1, y1, x2, y2, win):
        
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        
        self.__win = win

    def draw(self):
        if self.has_left_wall:
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x1, self.__y2)
            line = Line(p1, p2)
            self.__win.draw_line(line, "black")

        if self.has_right_wall:
            p1 = Point(self.__x2, self.__y1)
            p2 = Point(self.__x2, self.__y2)
            line = Line(p1, p2)
            self.__win.draw_line(line, "black")

        if self.has_top_wall:
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x2, self.__y1)
            line = Line(p1, p2)
            self.__win.draw_line(line, "black")

        if self.has_bottom_wall:
            p1 = Point(self.__x1, self.__y2)
            p2 = Point(self.__x2, self.__y2)
            line = Line(p1, p2)
            self.__win.draw_line(line, "black")

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
        self.__win.draw_line(line, color)