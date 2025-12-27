# Author: Owolabi
# Date: 10/02/2025
# Purpose: Python program to draw the string art.

from cs1lib import *

# Set Constants
OFFSET = 16
WIN_SIZE = 400

# draw lines in green
def draw_lines(x1, y1, x2, y2):
    set_stroke_color(0, 1, 0)
    set_stroke_width(1)
    draw_line(x1, y1, x2, y2)

# draw points in red
def draw_points(x1, y1, x2, y2):
    set_stroke_width(4)
    set_stroke_color(1, 0, 0)
    draw_point(x1, y1)
    draw_point(x2, y2)

# draw string art
def draw_string_art():
    set_clear_color(1, 1, 1)
    clear()

    # bottom right lines + top left lines
    for x in range(0, WIN_SIZE + 1, OFFSET):
        # bottom right
        draw_points(x, WIN_SIZE, WIN_SIZE, WIN_SIZE - x)
        draw_lines(x, WIN_SIZE, WIN_SIZE, WIN_SIZE - x)

        # top left
        draw_points(WIN_SIZE - x, 0, 0, x)
        draw_lines(WIN_SIZE - x, 0, 0, x)

    # top right lines + bottom left lines
    for y in range(0, WIN_SIZE + 1, OFFSET):
        # top right
        draw_points(WIN_SIZE, WIN_SIZE - y, WIN_SIZE - y, 0)
        draw_lines(WIN_SIZE, WIN_SIZE - y, WIN_SIZE - y, 0)

        # bottom left lines
        draw_points(0, y, y, WIN_SIZE)
        draw_lines(0, y, y, WIN_SIZE)

# Start the graphic
start_graphics(draw_string_art, width=WIN_SIZE, height=WIN_SIZE)
