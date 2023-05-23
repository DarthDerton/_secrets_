"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from collections import Callable


"""
function that accepts another function
as an argument and returns a new function
that caches the results of the original function
for each set of arguments it is called with
"""


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def cached_func(*args):
        if args in cache_dict:
            return cache_dict[args]
        else:
            result = func(*args)
            cache_dict[args] = result
            return result

    return cached_func