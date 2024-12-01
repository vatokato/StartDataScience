standard_input = ("5", "0 1 0 0 0", "1 0 1 1 0", "0 1 0 0 0", "0 1 0 0 0", "0 0 0 0 0")

N = int(input())
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

cities_count = 0
for l in range(N):
    for c in range(l):
        if matrix[l][c] == 1 and matrix[c][l] == 1:
            cities_count += 1

print(cities_count)
