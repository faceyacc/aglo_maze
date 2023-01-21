import unittest
from maze import Maze

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
            num_rows
        )
    
    def test_maze_xlarge(self):
        num_cols = 1200
        num_rows = 1000
        m1 = Maze(0, 0, num_rows, num_cols, 3, 3)

        self.assertEqual(
            len(m1._cells),
            num_cols
        )

        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )


    def test_maze_break_entrance_and_exit(self):
        num_col = 12
        num_row = 10
        m1 = Maze(0, 0, num_row, num_col, 10, 10)

        self.assertEqual(
            m1._cells[0][0].has_top_wall, 
            False
        )
    
        self.assertEqual(
            m1._cells[num_col - 1][num_row-1].has_bottom_wall, 
            False
        )    


        


if __name__ == "__main__":
    unittest.main()