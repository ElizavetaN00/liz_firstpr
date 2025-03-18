def decorator(*args, **kwargs):
    def wrapper(func):
        def inner(*func_args, **func_kwargs):
            print((args, kwargs))
            return func(*func_args, **func_kwargs)
        return inner
    return wrapper


@decorator(1, 2, 3, [1, 2, 3], 'one',
           'two', 'three', one=1, two=2, three=3)
def identity(x):
    return x


print(identity(42))


@decorator()
def identity(x):
    return x


print(identity(42))
