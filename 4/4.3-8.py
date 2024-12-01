standard_input = "30 300"

s, f = map(int, input().split())


def is_prime(x):
    x = int(x)
    if x <= 1:
        return False
    if x == 2:
        return True
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def is_magic(x):
    x = str(x)
    if len(x) == 1:
        return is_prime(x)
    else:
        return is_magic(x[: len(x) - 1]) if is_prime(x) else False


primes = [i for i in range(s, f + 1) if is_magic(i)]

print(*primes if len(primes) > 0 else "0")
