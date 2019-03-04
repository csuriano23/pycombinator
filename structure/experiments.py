from __future__ import absolute_import

def _trampoline(fn):
    while callable(fn):
        fn = fn()
    return fn


identity = lambda x: x
thunk = lambda fn, *args, **kwargs: lambda: fn(*args, **kwargs)
trampoline = lambda f: lambda *args, **kwargs: _trampoline(f(*args, **kwargs))


def icounter(n):
    if n < 1:
        return n

    return n + icounter(n - 1)


def ifactorial(n):
    if n < 2:
        return 1

    return n * ifactorial(n - 1)


def ifibonacci(n):
    if n < 2:
        return n
    return ifibonacci(n-1) + ifibonacci(n-2)


def itribonacci(n):
    if n < 3:
        return n

    return itribonacci(n - 1) + itribonacci(n - 2) + itribonacci(n - 3)


_counter = lambda n, cps=identity: cps(0) if n < 1 else thunk(_counter, n - 1, lambda result: thunk(cps, result + n))
counter = trampoline(_counter)

_factorial = lambda n, cps=identity: cps(1) if n < 1 else \
    thunk(_factorial, n - 1, lambda result: thunk(cps, result * n))
factorial = trampoline(_factorial)

_fibonacci = lambda n, cps=identity: cps(n) if n < 2 else \
    thunk(_fibonacci, n - 1, lambda result1: thunk(_fibonacci, n - 2, lambda result2: thunk(cps, result1 + result2)))
fibonacci = trampoline(_fibonacci)

_tribonacci = lambda n, cps=identity: cps(n) if n < 3 else \
    thunk(_tribonacci, n - 1, lambda result1: thunk(_tribonacci, n - 2, lambda result2:
        thunk(_tribonacci, n - 3, lambda result3: thunk(cps, result1 + result2 + result3))))
tribonacci = trampoline(_tribonacci)

for i in range(20):
    assert icounter(i) == counter(i)
    assert ifactorial(i) == factorial(i)
    assert ifibonacci(i) == fibonacci(i)
    assert itribonacci(i) == tribonacci(i)
