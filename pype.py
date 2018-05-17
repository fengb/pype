from functools import partial

class l(object):
    def __init__(self, func, *args, **kwargs):
        self.func = partial(func, *args, **kwargs)

    def __ror__(self, lhs):
        return self.func(lhs)

class r(object):
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __ror__(self, lhs):
        return self.func(lhs, *args, **kwargs)
