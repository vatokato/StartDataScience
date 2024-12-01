f = int(input())
a = abs(f - int(input()))
b = abs(f - int(input()))
c = abs(f - int(input()))

min = min(a,b,c)
if a == min:
  print('A')
elif b == min:
  print('B')
else:
  print('C')

