from __future__ import absolute_import


from structure.generator import trampoline


def fibonacci(n, previous=0, current=1):
    if n < 1:
        yield previous

    yield fibonacci(n - 1, current, previous + current)


def calculate(n):
    return trampoline(fibonacci, n)
