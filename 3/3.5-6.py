standard_input = ("10 20 30 40 50", "10 25 30 45 55", "5 10 25 27 30 ")
lot1 = set([int(i) for i in input().split()])
lot2 = set([int(i) for i in input().split()])
lot3 = set([int(i) for i in input().split()])
s = list(lot1 & lot2 & lot3)
if len(s) > 0:
    print(*sorted(s))
else:
    print("Удачных чисел нет")
