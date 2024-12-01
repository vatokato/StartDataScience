import requests
import time
import re
from functools import wraps


def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло выполнение декорируемой функции
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time}")
        return result

    return wrapper


def logging(func):
    """
    Декоратор, который выводит параметры с которыми была вызвана функция
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Функция вызвана с параметрами: {args}, {kwargs}")
        return result

    return wrapper


def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции
    """

    count = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        result = func(*args, **kwargs)
        print(f"Функция была вызвана: {count} раз")
        return result

    return wrapper


@counter
@logging
@benchmark
def word_count(word, url="https://www.gutenberg.org/files/2638/2638-0.txt"):

    # отправляем запрос в библиотеку Gutenberg и забираем текст
    raw = requests.get(url).text

    # заменяем в тексте все небуквенные символы на пробелы
    processed_book = re.sub("[\W]+", " ", raw).lower()

    # считаем
    cnt = len(re.findall(word.lower(), processed_book))

    return f"Cлово {word} встречается {cnt} раз"


print(word_count("whole"))

# Время выполнения функции word_count: 3.988222122192383
# Функция вызвана с параметрами: ('whole',), {}
# Функция была вызвана: 1 раз
# Cлово whole встречается 176 раз
