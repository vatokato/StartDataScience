standard_input = "1"

num = int(input())

sequence = []
for i in range(1, num + 1):
    if i == 1:
        a = 1
    elif i in sequence:
        a = sequence[i - 2] + 3
    else:
        a = sequence[i - 2] + 2
    sequence.append(a)

print(sequence[num - 1])
