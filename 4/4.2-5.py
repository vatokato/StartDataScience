standard_input = "comort"

s = input()

first = s.find("f")
second = s.find("f", first + 1)

if second > 0:
    print(second)
elif first > 0:
    print(-1)
else:
    print(first + second)
