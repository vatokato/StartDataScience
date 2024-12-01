w = ''
longWord = ''
while  w!='КОНЕЦ':
  w=input()
  if len(longWord) < len(w):
    longWord = w
    
print(longWord)
    