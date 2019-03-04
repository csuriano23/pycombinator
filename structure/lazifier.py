from __future__ import absolute_import


def grow_lazy(f, *args, **kwargs):
    return lambda: f(*args, **kwargs)


def trampoline(f, *args, **kwargs):
    v = f(*args, **kwargs)

    while callable(v):
        v = v()

    return v
