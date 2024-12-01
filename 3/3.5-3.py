standard_input = "165 163 160 160 157 157 155 154", "162"
hs = [int(i) for i in input().split()]
h = int(input())
i = len(hs)
for index, value in enumerate(hs):
    if value < h:
        i = index
        break
hs.insert(i, h)
print(i + 1)
