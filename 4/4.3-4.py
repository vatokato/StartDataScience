standard_input = "5"

side = int(input())

for l in range(1, side * 2):
    line = ""
    for c in range(side):
        if (l <= side and c >= side - l) or (l > side and c >= l - side):
            line += "0"
        else:
            line += " "
        line += " " if c < side - 1 else ""
    first_zero = line.find("0")
    last_zero = line.rfind("0")
    if first_zero != last_zero:
        line = (
            line[: first_zero + 2]
            + "x " * ((last_zero - first_zero) // 2 - 1)
            + line[last_zero:]
        )
    print(line)
