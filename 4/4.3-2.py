standard_input = "3"

s = int(input())
colors = []
# сторона минус 2 крайних, в квадрат чтобы вычислить площадь на одной стороне * 6 сторон
colors.append((s - 2) ** 2 * 6 if s > 1 else 0)

# сторона минус 2 крайних * 12 ребер
colors.append((s - 2) * 12 if s > 1 else 0)

colors.append(8 if s > 1 else 0)

for color in colors:
    print(color)
