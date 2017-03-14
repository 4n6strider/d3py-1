#!/usr/bin/env python

################################################################################
# Copyright (C) 2016 Jaakko Luttinen
#
# This file is licensed under the MIT License.
################################################################################


# Read version number __version__ from the file
# See: https://packaging.python.org/en/latest/single_source_version/#single-sourcing-the-version
import os
version = {}
base_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(base_dir, 'd3py', 'version.py')) as fp:
    exec(fp.read(), version)
__version__ = version['__version__']

NAME         = 'd3py'
DESCRIPTION  = 'Thin Python wrapper for D3.js'
AUTHOR       = 'Jaakko Luttinen'
AUTHOR_EMAIL = 'jaakko.luttinen@iki.fi'
URL          = 'https://github.com/jluttine/d3py'
LICENSE      = 'MIT'
VERSION      = __version__


if __name__ == "__main__":

    # Utility function to read the README file.
    # Used for the long_description.  It's nice, because now 1) we have a top level
    # README file and 2) it's easier to type in the README file than to put a raw
    # string in below ...
    def read(fname):
        return open(os.path.join(os.path.dirname(__file__), fname)).read()

    from setuptools import setup, find_packages

    setup(
        install_requires = [
        ],
        packages         = find_packages(),
        name             = NAME,
        version          = VERSION,
        author           = AUTHOR,
        author_email     = AUTHOR_EMAIL,
        description      = DESCRIPTION,
        license          = LICENSE,
        url              = URL,
        long_description = read('README.rst'),
        keywords         = [
            'visualization',
        ],
        classifiers = [
            'Programming Language :: Python',
            'Development Status :: 1 - Planning',
            'Framework :: IPython',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Topic :: Multimedia :: Graphics :: Presentation',
            'Topic :: Scientific/Engineering :: Visualization',
        ],
    )

