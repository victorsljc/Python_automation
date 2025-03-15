"""

A generator is a function that produces a sequence of values lazily (on-the-fly) using the yield keyword.

Unlike regular functions that return a single value and exit, generators pause execution after yielding a value and
resume when the next value is requested.

Generators are iterators, meaning you can loop over them or use them with functions like next().


"""
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_simple_yield_usage():
    def func():
        for x in range(10):
            yield x

    a = func()
    for x in a:
        print(x)

def test_using_next_usage():
    def func():
        for x in range(10):
            yield x

    a = func()
    print(next(a))
    print(next(a))





