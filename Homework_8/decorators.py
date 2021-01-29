import time


def warn_slow(func):
    def inner(x, y):
        start = time.time()
        result = func(x, y)
        duration = time.time() - start
        if duration >= 2:
            print(f'execution of {func.__name__} {x}, {y} took more then 2 seconds.')
        else:
            print(f'execution of {func.__name__} {x}, {y} arguments took {duration} seconds.')
        return result
    inner.__name__ = func.__name__
    return inner


@warn_slow
def func_slow(x, y):
    time.sleep(3)
    print(x, y)


@warn_slow
def func_fast(x, y):
    print(x, y)


print(func_fast(2, 5))
print(func_slow(2, 5))
