from __future__ import absolute_import

import pytest
from functools import partial

from structure.ycombinator import Y, Y_SHORT, Y_LONG, Y_LAZY
from fibonacci import accumulately, cythonely, iterately, lambdely, recursely, trampolinely, yieldily


@pytest.fixture(params=[
    iterately.calculate,
    cythonely.calculate,
    partial(lambdely.calculate, Y),
    partial(lambdely.calculate, Y_SHORT),
    partial(lambdely.calculate, Y_LONG),
    partial(accumulately.calculate, Y),
    partial(accumulately.calculate, Y_SHORT),
    partial(accumulately.calculate, Y_LONG),
    partial(accumulately.calculate, Y_LAZY),
    trampolinely.calculate,
    yieldily.calculate
])
def calculating_fn(request):
    yield request.param


@pytest.fixture(params=[i for i in range(0, 30)])
def references(request):
    yield request.param, recursely.calculate(request.param)


def test_algorithm(calculating_fn, references):
    input_value, output_expected = references
    assert output_expected == calculating_fn(input_value)
