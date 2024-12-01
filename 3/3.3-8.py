standard_input = 'ЛинАл, 4, МатАн, 5, АнГем, 3'
ratings = [int(r) for r in input().split(', ')[1::2]]
print(round(sum(ratings)/len(ratings), 1))