t = []
for _ in range(3):
    t.append(int(input()))
    
result = 'YES'
for i in range(len(t)):
  if sum(t)-t[i] <= t[i]:
    result = "NO"
    
print(result)

