from __future__ import absolute_import

from structure.lazifier import grow_lazy, trampoline


def fibonacci(n, previous, current):
    if n < 1:
        return grow_lazy(lambda x: x, previous)

    return grow_lazy(fibonacci, n - 1, current, previous + current)


def calculate(n):
    return trampoline(grow_lazy(fibonacci, n, 0, 1))
