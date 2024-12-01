standard_input = ("3", "черное белое", "день ночь", "далеко близко", "близко")
count = int(input())
my_dict = dict()
for _ in range(count):
    a, b = input().split()
    my_dict[a] = b

word = input()

for key, value in my_dict.items():
    if key == word:
        print(value)
    elif value == word:
        print(key)
