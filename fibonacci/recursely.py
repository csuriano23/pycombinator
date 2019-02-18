from __future__ import absolute_import


def calculate(n):
    if n < 2:
        return 1
    return calculate(n - 1) + calculate(n - 2)
