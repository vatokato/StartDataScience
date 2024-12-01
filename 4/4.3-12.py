standard_input = "29"


c = int(input())


def dolly_ate(c, e=0):
    if c < 4:
        return e
    if c % 5 == 0:
        e += dolly_ate(c * 1 / 5)
        e += dolly_ate(c * 3 / 5)
        return e
    else:
        return dolly_ate(c - 4, e + 4)


print(dolly_ate(c))
