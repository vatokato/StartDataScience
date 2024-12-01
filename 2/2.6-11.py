wordLengths = []
while True:
  word=input()
  if word == 'КОНЕЦ':
    break
  wordLengths.append(len(word))
  
print(round(sum(wordLengths)/len(wordLengths),1))
    