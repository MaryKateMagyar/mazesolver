from tkinter import Tk, BOTH, Canvas

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
            self, window, point1, point2, 
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
        if self.has_left_wall:
            left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left_wall)
        if self.has_top_wall:
            top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top_wall)
        if self.has_right_wall:
            right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right_wall)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(bottom_wall)
    
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
        self, win, x1, y1, 
        num_rows, num_cols,
        cell_size_x, cell_size_y
    ):


def main():
    win = Window(800, 600)
    point1 = Point(10, 10)
    point2 = Point(30, 30)
    cell1 = Cell(win, point1, point2)
    cell1.draw()
    point3 = Point(50, 50)
    point4 = Point(100, 100)
    cell2 = Cell(win, point3, point4, has_right_wall=False)
    cell2.draw()
    cell1.draw_move(cell2)
    win.wait_for_close()

main()