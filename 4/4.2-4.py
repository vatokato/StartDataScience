standard_input = "In the hole in the ground there lived a hobbit"

s = input()
f = s[: s.find("h")]
l = s[s.rfind("h") + 1 :]
print(f + l)
