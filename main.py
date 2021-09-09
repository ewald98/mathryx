
from graphics import *

WIDTH = 800
HEIGHT = 600


class AbstractPosition:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_point(self):
        point_on_screen = Point(
            int((self.x + 1) * WIDTH / 2),
            int((self.y + 1) * HEIGHT / 2)
        )
        return point_on_screen


def draw_line(start: AbstractPosition, end: AbstractPosition, width: int):
    start_point = start.to_point()
    end_point = end.to_point()
    line = Line(start_point, end_point)
    line.setWidth(width)
    line.setOutline('white')
    line.draw(win)


if __name__ == '__main__':
    win = GraphWin('2D Plane', WIDTH, HEIGHT)
    win.setBackground('black')
    # win.yview() # make right side up coordinates!

    draw_line(
        AbstractPosition(-1, 0),
        AbstractPosition(1, 0),
        2
    )

    draw_line(
        AbstractPosition(0, -1),
        AbstractPosition(0, 1),
        2
    )

    win.getMouse()
    win.close()
