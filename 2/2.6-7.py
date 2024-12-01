result = ''
for i in range(100, 1000):
  n = str(i)
  sum = 0;
  for l in n:
    sum += int(l)
  if i == sum * 70:
    result += n + ' '
    
print(result)

