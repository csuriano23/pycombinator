from __future__ import absolute_import

from structure.trampoline import Trampoline


class Fibonacci(Trampoline):
    def __init__(self, create_fn, original, current, prev2, prev1):
        self.create_fn = create_fn
        self.original = original
        self.current = current
        self.prev1 = prev1
        self.prev2 = prev2

    def value(self):
        return self.prev2 + self.prev1

    def next(self):
        return self.create_fn(self.original, self.current + 1, self.prev1, self.value())


def calculate(value):
    def _inner(n, current, fibt2, fibt1):
        if current == n or n < 2:
            return Fibonacci(lambda *args: None, n, current, fibt2, fibt1)

        return Fibonacci(_inner, n, current, fibt2, fibt1)

    return _inner(value, 2, 0, 1 if value else 0).compute()
