# somar apenas numeros MAIORES que 10

def ten_plus_sum(numbers:list):
  sum = 0
  for num in numbers:
    if num > 10:
      sum += num
  return sum

res = ten_plus_sum([11,3,2,23])

print(f'The sum of elements greater than 10 is: {res}')