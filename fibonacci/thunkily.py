from __future__ import absolute_import

from structure.thunks import identity, thunk, trampoline


_fibonacci = lambda n, previous=0, current=1: n if n < 2 else previous + current if n == 2 else \
    thunk(_fibonacci, n - 1, current, previous + current)

fibonacci = trampoline(_fibonacci)


def calculate(n):
    return fibonacci(n)
