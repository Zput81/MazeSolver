from window import Window
from Line import Line
from Point import Point
from Cell import Cell
from Maze import Maze




def main():
    win = Window(800, 600)

    x1 = 50
    y1 = 50

    num_rows = 5
    num_cols = 5
    cell_size_x = 50
    cell_size_y = 50

    maze = Maze(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win)

    maze.generate_maze()
    
    maze.solve()

    win.wait_for_close()

if __name__ == "__main__":
    main()