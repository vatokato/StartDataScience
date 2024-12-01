n = int(input())
tickets = []
happy = 0
while len(tickets) < n:
  t = input()
  if 100000 <= int(t) <= 999999:
    tickets.append(t)
    lSide = 0
    rSide = 0
    for i in range(len(t)):
      if i<3:
        lSide += int(t[i])
      else:
        rSide += int(t[i])
    if(lSide == rSide):
      happy+=1
  else:
    print('incorrect, only 6 digits')
    continue

print(happy)