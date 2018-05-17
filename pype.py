"""
>>> import pype
>>> ([1, 2, 3, 4, 5]
...   | pype.l(filter, lambda x: x%2 == 1)
...   | pype.l(map, lambda x: x**2)
... )
[1, 9, 25]
"""

from functools import partial

class l(object):
    def __init__(self, func, *args, **kwargs):
        self.func = partial(func, *args, **kwargs)

    def __call__(self, arg):
        return self.func(arg)

    def __ror__(self, lhs):
        return self(lhs)

class r(object):
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self, arg):
        return self.func(arg, *args, **kwargs)

    def __ror__(self, lhs):
        return self(lhs)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
