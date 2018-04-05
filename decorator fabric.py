#!/usr/bin/env python
import functools


def fabric(fn):
    """Decorator fabric. Implements function to the result of decorated function.
    Decorator can be turned off throw putting True to parameter fabric.off:
    fabric.off = True => decorator will not be used to function.

    :param fn: function(lambda)
    """

    def decorator(deco):
        def arguments(first, *x):
            decorated = deco(first, *x)

            def function_to_decorate(func):
                func_decorated = decorated(func)

                def f_decorated(*args, **kwargs):
                    if not fabric.off:
                        res = func_decorated(*args, *kwargs)
                        res = fn(res)
                    else:
                        res = func(*args, **kwargs)
                        res = fn(res)
                    return res
                return f_decorated
            return function_to_decorate
        return arguments
    fabric.off = False
    return decorator


@fabric(lambda x: x ** 2)
def repeat(times):
    """Repeat times times and return average.

    :param times: int, times to repeat
    :returns: int
    """

    @functools.wraps(repeat)
    def decorator(func):
        def wrapper(*args):
            result = 0
            for i in range(times):
                result += func(*args)
            average = int(result / times)
            return average
        return wrapper
    return decorator


@repeat(3)
def foo(*args):
    """Prints "Foo called!" and nothing else.

    :returns: 3 (independent)
    """

    print("Foo called!")
    return 3


print(foo([1, 3, 5]))
fabric.off = True
print(foo([1, 3, 5]))
