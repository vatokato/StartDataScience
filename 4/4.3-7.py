standard_input = ("АГЕИКЛМОРТ", "4", "8267", "19929", "54262", "000000000000")


alphabet = input()
count = int(input())
result = ""
nums = [input() for _ in range(count)]


def num_sum(num):
    summary = 0
    for i in range(len(num)):
        summary += int(num[i])
    if summary > 9:
        return num_sum(str(summary))
    return summary


result = "".join([alphabet[num_sum(n)] for n in nums])
print(result)
