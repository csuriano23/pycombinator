from __future__ import absolute_import


Y = lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args)))

Y_SHORT = lambda f: lambda *args: f(Y_SHORT(f))(*args)

Y_LONG = lambda b: ((lambda f: b(lambda *x: f(f)(*x)))((lambda f: b(lambda *x: f(f)(*x)))))

Y_LAZY = lambda f: (lambda x: x(x))(lambda y: f(lambda *args: lambda: y(y)(*args)))
