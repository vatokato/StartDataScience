c = int(input())

lesson = 45
bigBreak = 10
smallBreak = 5

duration = 0
for i in range(c):
  duration+=lesson
  if(i+1 == c):
    continue
    
  if((i+1)%2 == 0):
    duration += bigBreak
  else:
    duration += smallBreak
    
print(f'{8+duration//60} {duration%60}')
    