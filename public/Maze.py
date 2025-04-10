from Cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.__x1 = x1
        self.__y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

    def _create_cells(self):
        self._cells = []

        for row in range(self.num_rows):
            row_cells = []
            for col in range(self.num_cols):

                x1 = self.__x1 + col * self.cell_size_x
                y1 = self.__y1 + row * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y

                cell = Cell(x1, y1, x2, y2, self.win)

                row_cells.append(cell)

                self._draw_cell(cell)

            self._cells.append(row_cells)

    def _draw_cell(self, cell):
        cell.draw()

        self._animate()

    def _animate(self):

        time.sleep(0.05)