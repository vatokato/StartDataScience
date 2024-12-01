standard_input = "4"


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


sum = int(input())
primes = [i for i in range(2, sum + 1) if is_prime(i)]

for num in primes:
    if sum - num in primes:
        print(num, sum - num)
        break
