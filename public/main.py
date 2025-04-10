from window import Window
from Line import Line
from Point import Point
from Cell import Cell
from Maze import Maze

def main():
    win = Window(800, 600)

    x1 = 50
    y1 = 50

    num_rows = 10
    num_cols = 10
    cell_size_x = 50
    cell_size_y = 50

    maze = Maze(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win)

    maze._create_cells()

    win.wait_for_close()

if __name__ == "__main__":
    main()