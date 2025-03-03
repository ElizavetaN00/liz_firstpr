def validate_arguments(func):
    def wrapper(*args):
        for i in args:
            if not (isinstance(i, (int, float)) and i > 0):
                raise ValueError(f"Argument {i} is not a positive number!")
        return func(*args)
    return wrapper


@validate_arguments
def summ(a, b):
    return a + b

print("Summ is", summ(8, 9))


def validate_number_result(func):
    def wrapper(*args):
        result = func(*args)
        if not isinstance(result, (int, float)):
            print(f"Error. Result of function {func.__name__} is not a number. Got {result}")
            return None
        return result
    return wrapper


@validate_number_result
def summ(a, b):
    return a + b


@validate_number_result
def text(name):
    return f"Good evening, {name}!"

print(summ(7,1))
print(text("Ivan"))


def typed(type):
    def decorator(func):
        def wrapper(*args):
            result_args = []
            for i in args:
                result_args.append(type(i))
            return func(*result_args)
        return wrapper
    return decorator


@typed(type=str)
def add(a, b):
    return a + b


@typed(type=int)
def add_int(a, b, c):
    return a + b + c


@typed(type=float)
def add_float(a, b, c):
    return a + b + c


print(add("3", 5))
print(add(5, 5))
print(add('a', 'b'))

print(add_int(5, 6, 7))
print(add_int("5", 6.0, "7"))

print(add_float(0.1, 0.2, 0.4))
print(add_float("0.1", 0.2, "0.4"))


def cache(func):
    cached_result_dictionary = {}
    def wrapper(*args):
        if args in cached_result_dictionary:
            print(f"Result for {args} is from cache")
            return cached_result_dictionary[args]
        result = func(*args)
        cached_result_dictionary[args] = result
        print(f"Result for {args} is moved to cache")
        return result
    return wrapper


@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))  # Вывод: 5
print(fibonacci(10))  # Вывод: 55
print(fibonacci(5))  # Вывод: 5 (значение взято из кэша)