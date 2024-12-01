standard_input = "220 284"

first, second = map(int, input().split(" "))


def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0 and i != n:
            divisors.append(i)
    return divisors


first_sum = sum(find_divisors(first))
second_sum = sum(find_divisors(second))

print("YES" if first_sum == second and second_sum == first else "NO")
