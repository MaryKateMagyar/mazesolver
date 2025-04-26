import unittest
from main import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells2(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_3(self):
        num_cols = 20
        num_rows = 25
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_cell_walls_initialization(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for i in range(num_cols):
            for j in range(num_rows):
                cell = m1._cells[i][j]
                if cell is m1._cells[0][0]:
                    self.assertTrue(cell.has_left_wall)
                    self.assertTrue(cell.has_right_wall)
                    self.assertTrue(cell.has_bottom_wall)
                elif cell is m1._cells[num_cols - 1][num_rows - 1]:
                    self.assertTrue(cell.has_left_wall)
                    self.assertTrue(cell.has_right_wall)
                    self.assertTrue(cell.has_top_wall)
                else:
                    self.assertTrue(cell.has_left_wall)
                    self.assertTrue(cell.has_right_wall)
                    self.assertTrue(cell.has_top_wall)
                    self.assertTrue(cell.has_bottom_wall)

    def test_cell_dimensions(self):
        cell_size_x = 15
        cell_size_y = 20
        m1 = Maze(0, 0, 5, 5, cell_size_x, cell_size_y)
        cell = m1._cells[2][3]
        self.assertEqual((cell._x2 - cell._x1), cell_size_x)
        self.assertEqual((cell._y2 - cell._y1), cell_size_y)

    def test_entrance_exit_broken(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        entrance = m1._cells[0][0]
        exit = m1._cells[-1][-1]
        self.assertFalse(entrance.has_top_wall)
        self.assertFalse(exit.has_bottom_wall)

if __name__ == "__main__":
    unittest.main()