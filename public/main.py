from window import Window
from Line import Line
from Point import Point
from Cell import Cell


def main():
    win = Window(800, 600)

    cell1 = Cell(50, 50, 100, 100, win)

    cell2 = Cell(150, 50, 200, 100, win)
    cell2.has_right_wall = False

    cell3 = Cell(50, 150, 100, 200, win)
    cell3.has_bottom_wall = False
    cell3.has_left_wall = False

    cell1.draw()
    cell2.draw()
    cell3.draw()

    win.wait_for_close()

if __name__ == "__main__":
    main()