standard_input = 'мама'
word = input().lower()
vowels = tuple('aeiouаеёиоуыэюя')
consonants = tuple("bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ")

countVowels = 0
countCons = 0

for vowel in vowels:
  if(vowel in word):
    countVowels+=1
    
for cons in consonants:
  if(cons in word):
    countCons+=1

print((countVowels, countCons))


