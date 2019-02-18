from __future__ import absolute_import


cdef c_fibonacci(long n):
    if n < 2:
        return 1
    return c_fibonacci(n-1) + c_fibonacci(n-2)


cpdef long calculate(long n):
    return c_fibonacci(n)
