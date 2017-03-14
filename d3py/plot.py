# Copyright (c) 2016 Jaakko Luttinen
# This file is released under the MIT license

"""
Some examples of D3.js graphs
"""

from d3py import core


def line_chart(x, y):

    # Build Javascript
    js = core.populate_template(
        core.read_lib('js', 'line_chart'),
        data=core.dict_to_json([dict(x=xi, y=yi) for (xi, yi) in zip(x, y)]),
        # x=core.array_to_json(x),
        # y=core.array_to_json(y),
        #width=width,
        #height=height,
        #colors=core.array_to_json(colors)
    )

    # Build CSS
    css = core.populate_template(core.read_lib('css', 'line_chart'))

    # Build graph HTML
    return core.graph(js, css)


def chord_diagram(data, width=950, height=500, colors=None):

    # Define default color cycle
    if colors is None:
        colors = [
            "#000000", "#FFDD89", "#957244", "#F26223"
        ]

    # Build Javascript
    js = core.populate_template(
        core.read_lib('js', 'chord_diagram'),
        data=core.array_to_json(data),
        width=width,
        height=height,
        colors=core.array_to_json(colors)
    )

    # Build CSS
    css = core.populate_template(core.read_lib('css', 'chord_diagram'))

    # Build graph HTML
    return core.graph(js, css)
