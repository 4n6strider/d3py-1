D3Py
====

D3Py is a thin Python wrapper for D3.js. The main goal is to enable users to
easily copy-paste beautiful D3.js visualizations from http://bl.ocks.org and use
them in their Jupyter Notebooks for their own data.

Other features:

- two-way synchronization:
  - update graphs based on updates on Python data
  - update Python data based on (user) interactions on the graph
  
- support other JS libraries

Change of plans:

Support general JavaScript plotting libraries. D3.js is often too low level, so
make it possible to use other JS libraries easily. Some of them are built on top
of D3.js and some are not, but that shouldn't matter.

Here's one list: http://thenextweb.com/dd/2015/06/12/20-best-javascript-chart-libraries/

Some highlights:

- Really nice timeseries plotting:
  http://dygraphs.com/gallery/
- Nice innovation for timeseries plotting to save vertical space:
  https://square.github.io/cubism/
- Basics of several plot types: http://code.shutterstock.com/rickshaw/examples/
- Basics of several plot types: http://c3js.org/examples.html
- Basics of several plot types: http://nvd3.org/examples/index.html
- Graphs: http://js.cytoscape.org/
- Graphs: http://sigmajs.org/
- Miscellaneous plots: http://plottablejs.org/


Installation
------------

Install latest release from PyPI:

.. code:: console

   pip install d3py


Install latest development version from GitHub:

.. code:: console

   pip install git+https://github.com/jluttine/d3py.git@develop
   
   
Usage
-----
   

Contributing
------------

Contributions are most welcome. You can, for instance, improve the core methods
in order to make using D3.js easier, or provide example graphs as a function in
`plot` module along the Javascript and CSS files under `lib` folder.


License
-------

The GNU GPL v2 applies for the package as a whole. Most of the individual files
are released under the MIT license. However, some Javascript and CSS files of
the example graphs from other people have been released under other FLOSS
licenses. Thus, the package as a whole is released under the GPLv2 license.
Contributions are assumed to be MIT licensed unless otherwise stated.
