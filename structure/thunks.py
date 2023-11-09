from __future__ import absolute_import


def _trampoline(bouncer):
    while callable(bouncer):
        bouncer = bouncer()
    return bouncer


identity = lambda x: x
thunk = lambda name, *args, **kwargs: lambda: name(*args, **kwargs)
trampoline = lambda f: lambda *args, **kwargs: _trampoline(f(*args, **kwargs))
