from __future__ import absolute_import

import types


def trampoline(fn, *args, **kwargs):
    g = fn(*args, **kwargs)

    while isinstance(g, types.GeneratorType):
        g = next(g)

    return g
