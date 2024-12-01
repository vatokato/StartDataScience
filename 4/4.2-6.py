standard_input = "qwertyhasdfghzxcvb"

s = input()
middle = s[s.find("h") + 1 : s.rfind("h")]
print(s.replace(middle, middle * 2))
