standard_input = (
    "11",
    "266 199 13 13 99 97",
    "281	223	211	4 140 94",
    "115	261	191	167	151	175",
    "85 205 236 275 98 126",
    "217	54 276 146 170 13",
    "58 43 223 284 43 100",
    "216	30 15 211 139 30",
    "19 164	74 2 2 277",
    "280	22 9 129 164 9",
    "80 121 165 169 80 224",
    "36 39 282 105 198 39",
)

lines_num = int(input())
lines = dict()
true_lines_count = 0
for i in range(lines_num):
    line = [int(n) for n in input().split()]

    repeated = [n for n in line if line.count(n) == 2]
    uniq = [n for n in line if line.count(n) == 1]

    if len(repeated) == 2 and len(uniq) == 4 and sum(repeated) < sum(uniq) / len(uniq):
        true_lines_count += 1

print(true_lines_count)
