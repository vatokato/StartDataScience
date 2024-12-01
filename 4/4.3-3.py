standard_input = "круг", "4", "3"


def triangle_area(a, b, c):
    a, b, c = map(abs, (a, b, c))
    p = (a + b + c) / 2.0
    if a + b <= c or a + c <= b or b + c <= a:
        return 0.0  # такого треугольника не существует
    return float((p * (p - a) * (p - b) * (p - c)) ** 0.5)


def rectangle_area(a, b):
    return float(a * b)


def circle_area(r):
    return float(3.14 * r**2)


get_area = {
    "треугольник": {"params_count": 3, "func": triangle_area},
    "круг": {"params_count": 1, "func": circle_area},
    "прямоугольник": {"params_count": 2, "func": rectangle_area},
}

type = input()
inps = []
for _ in range(get_area[type]["params_count"]):
    inps.append(int(input()))

print(round(get_area[type]["func"](*inps), 1))
