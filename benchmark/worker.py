from __future__ import absolute_import, division

import timeit
from functools import partial
from pandas import DataFrame

from structure.ycombinator import Y, Y_LAZY
from fibonacci import accumulately, cythonely, iterately, lambdely, recursely


CYCLE_SIZE = 20


def run():
    def runner(executor, iterations=20):
        def inner():
            for i in range(iterations):
                executor(i)
        return inner

    def timed(executor):
        return lambda: timeit.repeat(runner(executor), number=CYCLE_SIZE)

    return {
        "iterative": timed(iterately.calculate),
        "recursive": timed(recursely.calculate),
        "recursive with cython": timed(cythonely.calculate),
        "simple y-combinator on pure recursion": timed(partial(lambdely.calculate, Y)),
        # TODO "lazy y-combinator on pure recursion": timed(partial(lambdely.calculate, Y_LAZY)),
        "simple y-combinator on accumulator lambda": timed(partial(accumulately.calculate, Y)),
        "lazy y-combinator on accumulator lambda": timed(partial(accumulately.calculate, Y_LAZY)),
    }


if __name__ == "__main__":
    timings = DataFrame(index=["min_fn"])

    for type_of_run, benchmark_fn in run().items():
        samples = benchmark_fn()
        timings[type_of_run] = [min(samples)]

    timings = timings.transpose()
    min_global = timings.apply(min, axis=0)["min_fn"]
    timings["diff_perc"] = (timings["min_fn"] / min_global) - 1

    print(timings.sort_values("diff_perc"))
