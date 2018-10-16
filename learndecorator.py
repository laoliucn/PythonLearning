import time
from datetime import datetime
import functools


# decorator example to add execution time to an function.
def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        # print("Caused ", elapsed, " time to execute the ", name, "(", arg_str, ")", "function, result is ",
        #       result)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


@functools.lru_cache()
@clock
def fibonacci(n):
    return 1 if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


@clock
def snooze(second):
    time.sleep(second)


if __name__ == '__main__':
    print('*' * 40, 'Calling factorial')
    print(fibonacci(30))
