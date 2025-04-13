from Cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        self.__x1 = x1
        self.__y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self.seed = seed
    
    def _create_cells(self):
        
        self._cells = []

        for row in range(self.num_rows):
            row_cells = []
            for col in range(self.num_cols):

                x1 = self.__x1 + col * self.cell_size_x
                y1 = self.__y1 + row * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y

                cell = Cell(x1, y1, x2, y2, self._win, False)

                row_cells.append(cell)

                self._draw_cell(cell)

            self._cells.append(row_cells)
           
    def _draw_cell(self, cell):
        if self._win is not None:
            cell.draw()

            self._animate()

    def _animate(self):
        
        if self._win is not None:
           
            self._win.redraw()
            
        time.sleep(0.05)

    def _get_directions(self):
        return [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        self._draw_cell(entrance_cell)
        
        exit_cell = self._cells[self.num_rows-1][self.num_cols-1]
        exit_cell.has_bottom_wall = False
        self._draw_cell(exit_cell)

    def _break_walls_r(self, i, j):
        
        self._cells[i][j].visited = True
        
        
        moves = self._get_directions()
        random.shuffle(moves)
        
        for move in moves:
            i_neighbor = i + move[0]
            j_neighbor = j + move[1]

            if 0 <= i_neighbor < self.num_rows and 0 <= j_neighbor < self.num_cols and not self._cells[i_neighbor][j_neighbor].visited:        
                
                if i_neighbor == i - 1:
                    self._cells[i][j].has_top_wall = False
                    self._cells[i_neighbor][j_neighbor].has_bottom_wall = False

                elif i_neighbor == i + 1:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i_neighbor][j_neighbor].has_top_wall = False
            
                elif j_neighbor == j - 1:
                    self._cells[i][j].has_left_wall = False
                    self._cells[i_neighbor][j_neighbor].has_right_wall = False
            
                elif j_neighbor == j + 1:
                    self._cells[i][j].has_right_wall = False
                    self._cells[i_neighbor][j_neighbor].has_left_wall = False

                self._cells[i][j].draw()
                self._cells[i_neighbor][j_neighbor].draw()
                self._win.redraw()
                
                self._break_walls_r(i_neighbor, j_neighbor)
        

    def _reset_cells_visited(self):
        for row in self._cells:
            for i in row:
                i.visited = False

    def generate_maze(self):
        
        self._create_cells()
        
        self._break_entrance_and_exit()
        
        self._break_walls_r(0,0)
        
        self._reset_cells_visited()

    def solve(self):
        
        result = self._solve_r(i=0, j=0)
        
        return result
    def _solve_r(self, i, j):
        
        self._animate()
        
        self._cells[i][j].visited = True
        
        if i == self.num_rows - 1 and j == self.num_cols - 1:
            
            return True
        
        moves = self._get_directions()

        for direction in moves:
            new_i = i + direction[0]
            new_j = j + direction[1]

            if 0 <= new_i < self.num_rows and 0 <= new_j < self.num_cols:
                if (direction == (-1,0) and not self._cells[i][j].has_top_wall) or \
                   (direction == (1,0) and not self._cells[i][j].has_bottom_wall) or \
                   (direction == (0,-1) and not self._cells[i][j].has_left_wall) or \
                   (direction == (0,1) and not self._cells[i][j].has_right_wall):
                    
                    if not self._cells[new_i][new_j].visited:
                        
                        self._cells[i][j].draw_move(self._cells[new_i][new_j])
                        
                        if self._solve_r(new_i, new_j):
                            return True
                        else:
                            self._cells[i][j].draw_move(self._cells[new_i][new_j], undo=True)
                    
        return False