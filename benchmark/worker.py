from __future__ import absolute_import, division

import timeit
from functools import partial
from pandas import DataFrame

from structure.ycombinator import Y, Y_LAZY
from fibonacci import accumulately, cythonely, iterately, lambdely, lazily, recursely, thunkily, trampolinely, yieldily


class BenchmarkRun(object):
    def __init__(self, iterations, cycles):
        self.iterations = iterations
        self.cycles = cycles

    def runner(self, executor):
        def inner():
            for i in range(self.iterations):
                executor(i)
        return inner

    def timed(self, executor):
        return lambda: timeit.repeat(self.runner(executor), number=self.cycles)

    @property
    def runners(self):
        return {
            ("iterative", self.timed(iterately.calculate)),
            ("recursive", self.timed(recursely.calculate)),
            ("recursive with cython", self.timed(cythonely.calculate)),
            ("simple y-combinator on pure recursion", self.timed(partial(lambdely.calculate, Y))),
            # TODO "lazy y-combinator on pure recursion": timed(partial(lambdely.calculate, Y_LAZY)),
            ("simple y-combinator on accumulator lambda", self.timed(partial(accumulately.calculate, Y))),
            ("lazy y-combinator on accumulator lambda", self.timed(partial(accumulately.calculate, Y_LAZY))),
            ("trampoline", self.timed(trampolinely.calculate)),
            ("generator", self.timed(yieldily.calculate)),
            ("lazy trampoline", self.timed(lazily.calculate)),
            ("thunked trampoline", self.timed(thunkily.calculate)),
        }


if __name__ == "__main__":
    benchmark = BenchmarkRun(20, 20)
    timings = DataFrame(index=["min_fn"])

    # warmup
    for _, run in benchmark.runners:
        run()

    for type_of_run, benchmark_fn in benchmark.runners:
        samples = benchmark_fn()
        timings[type_of_run] = [min(samples)]

    timings = timings.transpose()
    min_global = timings.apply(min, axis=0)["min_fn"]
    timings["diff_perc"] = (timings["min_fn"] / min_global) - 1

    print(timings.sort_values("diff_perc"))
