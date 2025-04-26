from tkinter import Tk, BOTH, Canvas
import time

class Window:
    def __init__(self, width, height):
        self.width = width  # window width in pixels
        self.height = height  # window height in pixels

        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.geometry(f"{self.width}x{self.height}")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(self.__root, height=self.height, width=self.width)
        self.canvas.pack()

        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x  # the x-coordinate (horizontal) in pixels of the point
                    # x = 0 is the left of the screen
        self.y = y  # the y coordinate (vertical) in pixels of the point
                    # y = 0 is the top of the screen

class Line:
    def __init__(self, point1, point2):
        self._x1 = point1.x
        self._y1 = point1.y
        self._x2 = point2.x
        self._y2 = point2.y

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self._x1, self._y1, self._x2, self._y2, 
            fill=fill_color, width=2
        )

class Cell:
    def __init__(
            self, point1, point2, window=None,
            has_left_wall=True, has_right_wall=True, 
            has_bottom_wall=True, has_top_wall=True
        ):
        self._win = window
        self._x1 = point1.x
        self._y1 = point1.y
        self._x2 = point2.x
        self._y2 = point2.y

        self.center_x = self._x1 + ((self._x2 - self._x1) / 2)
        self.center_y = self._y1 + ((self._y2 - self._y1) / 2)

        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

    def draw(self):
        if self._win:
            left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            if self.has_left_wall:
                self._win.draw_line(left_wall, "black")
            else:
                self._win.draw_line(left_wall, "#d9d9d9")

            if self.has_top_wall:
                self._win.draw_line(top_wall, "black")
            else:
                self._win.draw_line(top_wall, "#d9d9d9")

            if self.has_right_wall:
                self._win.draw_line(right_wall, "black")
            else:
                self._win.draw_line(right_wall, "#d9d9d9")

            if self.has_bottom_wall:
                self._win.draw_line(bottom_wall, "black")
            else:
                self._win.draw_line(bottom_wall, "#d9d9d9")
    
    def draw_move(self, to_cell, undo=False):
        point1 = Point(self.center_x, self.center_y)
        point2 = Point(to_cell.center_x, to_cell.center_y)
        path = Line(point1, point2)
        if undo is False:
            self._win.draw_line(path, "red")
        else: 
            self._win.draw_line(path, "gray")

class Maze:
    def __init__(
        self, x1, y1, 
        num_rows, num_cols,
        cell_size_x, cell_size_y, win=None
    ):
        self.win = win
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        
        self._create_cells()
        self._break_entrance_and_exit()
    
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            column = []
            self._cells.append(column)
            for j in range(self.num_rows):
                _x1 = self.x1 + (i * self.cell_size_x)
                _x2 = _x1 + self.cell_size_x
                _y1 = self.y1 + (j * self.cell_size_y)
                _y2 = _y1 + self.cell_size_y
                column.append(Cell(Point(_x1, _y1), Point(_x2, _y2), self.win))
                if self.win:
                    self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self.win:
            self.win.redraw()
            time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        exit = self._cells[-1][-1]

        entrance.has_top_wall = False
        self._draw_cell(0, 0)
        exit.has_bottom_wall = False
        self._draw_cell(-1, -1)



def main():
    win = Window(800, 600)
    maze = Maze(5, 5, 10, 10, 25, 25, win)
    win.wait_for_close()

if __name__ == "__main__":
    main()