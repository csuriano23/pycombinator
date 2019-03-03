from __future__ import absolute_import


_fn = lambda f: lambda n: (n if n < 2 else f(n - 1) + f(n - 2))


def calculate(combinator, n):
    return combinator(_fn)(n)
