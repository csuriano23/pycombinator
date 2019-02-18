from __future__ import absolute_import


_fn = lambda f: lambda n, p, q: p if not n else f(n - 1, q, p + q)


def calculate(combinator, n):
    def wrapper(*args):
        out = combinator(_fn)(*args)
        while callable(out):
            out = out()
        return out

    return wrapper(n + 1, 0, 1)
