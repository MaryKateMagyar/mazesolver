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

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x  # the x-coordinate (horizontal) in pixels of the point
                    # x = 0 is the left of the screen
        self.y = y  # the y coordinate (vertical) in pixels of the point
                    # y = 0 is the top of the screen

class Line:
    def __init__(self, point1, point2):
        self.point1_x = point1.x
        self.point1_y = point1.y
        self.point2_x = point2.x
        self.point2_y = point2.y

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1_x, self.point1_y, self.point2_x, self.point2_y, 
            fill=fill_color, width=2
        )



def main():
    win = Window(800, 600)
    point1 = Point(100, 5)
    point2 = Point(1000, 86)
    point3 = Point(12, 890)
    point4 = Point(930, 322)
    line1 = Line(point1, point2)
    line2 = Line(point3, point1)
    win.draw_line(line1, "red")
    win.draw_line(line2, "black")
    win.wait_for_close()

main()