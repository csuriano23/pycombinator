from __future__ import absolute_import


class Trampoline(object):
    def value(self):
        raise NotImplementedError

    def next(self):
        raise NotImplementedError

    def compute(self):
        trampoline = self

        while True:
            next_trampoline = trampoline.next()

            if next_trampoline is None:
                break
            else:
                trampoline = next_trampoline

        return trampoline.value()


class Factorial(Trampoline):
    def __init__(self, create_fn, current, total):
        self.create_fn = create_fn
        self.current = current
        self.total = total

    def value(self):
        return self.total

    def next(self):
        return self.create_fn(self.current - 1, self.current * self.total)


def factorial(value):
    def _inner(n, tot):
        if n == 1:
            return Factorial(lambda *args: None, n, tot)

        return Factorial(_inner, n, tot)

    return _inner(value, 1).compute()
