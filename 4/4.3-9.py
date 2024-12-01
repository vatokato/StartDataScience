standard_input = ("5 5", "2", "1 1 3 3", "2 2 4 4")

w, h = map(int, input().split())
figures_count = int(input())
figures = [[int(i) for i in input().split()] for _ in range(figures_count)]

board = [[1] * w for _ in range(h)]

for l in range(h):
    for c in range(w):
        for x1, y1, x2, y2 in figures:
            if x1 <= c < x2 and y1 <= l < y2:
                board[l][c] = 0

print(sum(sum(row) for row in board))
