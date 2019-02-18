from __future__ import absolute_import


def calculate(n):
    if n < 2:
        return 1

    past2 = past1 = 1
    for m in range(2, n):
        curr = past1 + past2
        past2 = past1
        past1 = curr

    return past1 + past2
