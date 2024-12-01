standard_input = (
    "3",
    "вода кислород водород",
    "аммиак азот водород",
    "ацетон углерод водород кислород",
    "2",
    "кислород",
    "водород",
)

inner_count = int(input())
my_dict = dict()

for _ in range(inner_count):
    line = input().split()
    el = line[0]
    for i in range(1, len(line)):
        if line[i] not in my_dict:
            my_dict[line[i]] = []
        my_dict[line[i]].append(el)

outer_count = int(input())
for _ in range(outer_count):
    mol = input()
    print(*my_dict[mol])
