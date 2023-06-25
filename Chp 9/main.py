import functools
import time

from clock_decorator import clock, clock_2


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock_2
def factorial(n, useless_arg='test'):
    return 1 if n < 2 else n*factorial(n-1)


@functools.cache
@clock_2
def fibonacci(n):
    if n <2:
        return 1
    return fibonacci(n-2) + fibonacci(n - 1)


fibonacci(8)


snooze(3)
print(factorial(5))