import time
from functools import wraps


def memo(func):
    """
    Декоратор, запоминающий результаты исполнения функции func, чьи аргументы args должны быть хешируемыми
    """
    cache = {}

    @wraps(func)
    def fmemo(*args):
        args_hash = hash(args)
        if args_hash not in cache:
            cache[args_hash] = func(*args)
        return cache[args_hash]

    fmemo.cache = cache
    return fmemo


def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


start_time = time.time()
res = fib(38)
end_time = time.time()
print(f"Без кэша: {end_time - start_time} секунд. Результат: {res}")


@memo
def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


start_time2 = time.time()
res = fib(38)
end_time2 = time.time()
print(f"С кэшем: {end_time2 - start_time2} секунд. Результат: {res}")


# Без кэша: 6.313446760177612 секунд. Результат: 39088169
# С кэшем: 0.00011086463928222656 секунд. Результат: 39088169
