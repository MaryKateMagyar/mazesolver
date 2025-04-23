from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width  # window width in pixels
        self.height = height  # window height in pixels

        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.geometry(f"{self.width}x{self.height}")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas()
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

class Point:
    def __init__(self, x, y):
        self.x = x  # the x-coordinate (horizontal) in pixels of the point
                    # x = 0 is the left of the screen
        self.y = y  # the y coordinate (vertical) in pixels of the point
                    # y = 0 is the top of the screen

class Line:
    def __init__(self, point1, point2):
        

def main():
    win = Window(800, 600)
    win.wait_for_close()

main()