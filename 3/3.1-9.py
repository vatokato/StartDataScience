standard_input = '8, 11, 12, 13, 11';
numbers = input()

sum_even = 0;
for num in numbers.split(','):
  if int(num)%2 == 0:
    sum_even += int(num)
    
print(sum_even)

