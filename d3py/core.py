# Copyright (c) 2016 Jaakko Luttinen
# This file is released under the MIT license

"""
Functions for handling HTML, Javascript and CSS snippets.
"""

import string
import random
from IPython.display import HTML, display
import os
import json
import numpy as np


def _get_random_id():
    """ Get a random (i.e., unique) string identifier"""
    symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(symbols) for _ in range(15))


def read_file(filename):
    """ Return the contents of a file as a string. """
    with open(filename) as f:
        str = f.read()
    return str


def get_lib_filename(category, name):
    """ Get a filename of a built-in library file. """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if category == 'js':
        filename = os.path.join('js', '{0}.js'.format(name))
    elif category == 'css':
        filename = os.path.join('css', '{0}.css'.format(name))
    elif category == 'html':
        filename = os.path.join('html', '{0}.html'.format(name))
    else:
        raise ValueError("Unknown category")
    return os.path.join(base_dir, 'lib', filename)


def read_lib(category, name):
    """ Get contents of a built-in library file. """
    return read_file(get_lib_filename(category, name))


def populate_template(template, **kwargs):
    """ Return a template string with filled argument values. """
    return string.Template(template).safe_substitute(kwargs)


def display_html(html):
    """ Display given HTML code string. """
    display(HTML(html))
    return


def output_notebook(
        d3js_url="//d3js.org/d3.v3.min",
        requirejs_url="//cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js",
        html_template=None
):
    """ Import required Javascript libraries to Jupyter Notebook. """

    if html_template is None:
        html_template = read_lib('html', 'setup')

    setup_html = populate_template(
        html_template,
        d3js=d3js_url,
        requirejs=requirejs_url
    )

    display_html(setup_html)
    return


def create_graph_html(js_template, css_template, html_template=None):
    """ Create HTML code block given the graph Javascript and CSS. """
    if html_template is None:
        html_template = read_lib('html', 'graph')

    # Create div ID for the graph and give it to the JS and CSS templates so
    # they can reference the graph.
    graph_id = 'graph-{0}'.format(_get_random_id())
    js = populate_template(js_template, graph_id=graph_id)
    css = populate_template(css_template, graph_id=graph_id)

    return populate_template(
        html_template,
        graph_id=graph_id,
        css=css,
        js=js
    )


def graph(js_template, css_template):
    """ Create and display a graph HTML given Javascript and CSS. """
    html = create_graph_html(js_template, css_template)
    return display_html(html)


def array_to_json(data):
    """ Convert an array or a list to JSON. """
    return json.dumps(np.asanyarray(data).tolist())

def dict_to_json(d):
    return json.dumps(d)
