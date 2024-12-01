standard_input = "1000 1500 7000 6000 7000"
inp = [int(i) for i in input().split()]
print(inp.index(max(inp)) + 1)
