#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""To create an ascii painting made up of several smaller parts."""

import json


def extend_canvas(canvas, art, pos_x, pos_y):
    """Ensure the canvas is large enough."""
    c_x = len(canvas[0])
    c_y = len(canvas)
    a_x = len(art[0]) + pos_x
    a_y = len(art) + pos_y
    if a_y > c_y:
        print((a_y - c_y))
        #print([""] * (a_y - c_y))
        #canvas.extend([""] * (a_y - c_y))
    if a_x > c_x:
        for i, row in enumerate(canvas):
            canvas[i] = row + " " * (a_x - c_x)

    return canvas


def merge_graphics(canvas, art, pos_x, pos_y):
    """Merge two graphics into one."""
    #extend_canvas(canvas, art, pos_x, pos_y)
    if canvas == []:
        canvas = art
        return canvas

    for i, row in enumerate(art, start=pos_y):
        row_len = len(row)
        part_a = canvas[i][0:pos_x]
        part_b = row
        part_c = canvas[i][pos_x + row_len:]
        canvas[i] = part_a + part_b + part_c
    return canvas


def canvas_to_string(canvas):
    """Convert canvas multi-list to string."""
    str1 = ""
    for row in canvas:
        str1 += "".join(row) + "\n"
    return str1


def create_from_dict(config, verbose=False):
    """Create artwork from a configuration item."""
    canvas = []
    for part in config["parts"]:
        if verbose:
            print(part)
        with open(part["file"]) as f:
            graphic = f.readlines()
            graphic = [line.strip("\n") for line in graphic]
            canvas = merge_graphics(
                canvas, graphic,
                part["pos_x"], part["pos_y"]
            )

    str1 = canvas_to_string(canvas)
    str1 += "\n" + config["title"]
    return str1


def create_from_file(filename, verbose=False):
    """Load JSON with details of artwork."""
    with open(filename) as f:
        config = json.load(f)
        if verbose:
            print(config)

    return create_from_dict(config, verbose)


if __name__ == "__main__":
    pass
