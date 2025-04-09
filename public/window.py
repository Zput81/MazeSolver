from tkinter import Tk, BOTH, Canvas
from Line import Line
from Point import Point

class Window:
    def __init__(self, width, height):
        self.__root = Tk()

        self.__root.title("Maze Solver")

        self.__canvas = Canvas(self.__root, width=width, height=height)

        self.__canvas.pack(fill=BOTH, expand=1)

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

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

def main():
    win = Window(800, 600)

    point1 = Point(50, 50)
    point2 = Point(200, 100)
    point3 = Point(100, 200)

    line1 = Line(point1, point2)
    line2 = Line(point2, point3)

    win.draw_line(line1, "red")
    win.draw_line(line2, "blue")

    win.wait_for_close()

if __name__ == "__main__":
    main()