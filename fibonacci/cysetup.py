from __future__ import absolute_import

from distutils.core import setup
from Cython.Build import cythonize


setup(
    name="pYcombinator",
    ext_modules=cythonize("fibonacci/cythonely.pyx"),
)
