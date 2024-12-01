standard_input = "2.5, 'hello', 1, (2, {1,True}, 3, {a: 213}), 3"
inp = input().replace(" ", "")

types = set()
elString = ""
isString = False
for l in inp:
    if isString and l == '"':
        isString = False
    elif l == '"':
        isString = True
    if not isString:
        if l == "[":
            types.add("list")
        if l == "(":
            types.add("tuple")
        if l == "{":
            types.add("set")
        if l == ":":
            types.add("dict")

els = (
    inp.replace("(", "")
    .replace(")", "")
    .replace("{", "")
    .replace("}", "")
    .replace("[", "")
    .replace("]", "")
    .split(",")
)

for el in els:
    if el[0] == "T" or el[0] == "F":
        types.add("bool")
    if el.isdigit():
        types.add("int")
    elif el.replace(".", "", 1).isdigit():
        types.add("float")
    elif el[0] == '"' or el[0] == "'":
        types.add("string")


print(len(types))
