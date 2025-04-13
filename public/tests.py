import unittest
from Maze import Maze
from Cell import Cell

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        
        m1._create_cells()
        
        self.assertEqual(len(m1._cells), num_rows,)
        self.assertEqual(len(m1._cells[0]), num_cols,)

    def test_break_entrance_and_exit(self):
        test_maze = Maze(0, 0, 3, 3, 10, 10)
        test_maze._create_cells()

        test_maze._break_entrance_and_exit()

        entrance_cell = test_maze._cells[0][0]
        self.assertFalse(entrance_cell.has_top_wall, "Entrance wall should be broken")

        exit_cell = test_maze._cells[2][2]
        self.assertFalse(exit_cell.has_bottom_wall, "Exit wall should be broken")

    def test_reset_cells_visited(self):
        test_maze = Maze(0, 0, 3, 3, 10, 10)
        test_maze._create_cells()

        test_maze._break_entrance_and_exit()
        test_maze._break_walls_r(0,0)
        
        test_maze._reset_cells_visited()

        for row in test_maze._cells:
            for cell in row:
                assert not cell.visited, "Cell still marked as visited after reset"



if __name__ == "__main__":
    unittest.main()