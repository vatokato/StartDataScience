standard_input = "comort"

word = input()

ff, lf = word.find("f"), word.rfind("f")

if ff != -1:
    if ff == lf:
        print(ff)
    else:
        print(ff, lf)
