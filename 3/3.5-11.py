standard_input = "8 11 23 45 -20"
# standard_input = "10 20 3 5 6 7 -33"

inp = input().split()

pairs = []
for i in range(0, len(inp) - 1):
    pairs.append([int(inp[i][-1]), int(inp[i + 1][-1])])

suspicious_count = 0
for p in pairs:
    if p[0] != p[1] and (p[0] == 3 or p[1] == 3):
        suspicious_count += 1

print("YES" if suspicious_count >= 3 else "NO")
