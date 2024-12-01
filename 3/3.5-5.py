standard_input = ("3", "откепскЭ мунортап", "asdfasfd", "муидрагниВ асоивел", 2)

magic_list = []
for _ in range(int(input())):
    magic_list.append(" ".join(str(input())[::-1].split(" ")[::-1]))
print(magic_list[int(input()) - 1])
