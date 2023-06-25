import functools
import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f'[{elapsed:0.8f}s {name}({arg_str}) -> {result!r}')
        return result
    return clocked


def clock_2(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_list = [repr(arg) for arg in args]
        arg_list.extend(f'{k}={v}' for k, v in kwargs.items())
        arg_str = ', '.join(arg_list)
        print(f'[{elapsed:0.8f}s {name}({arg_str}) -> {result!r}')
        return result
    return clocked
