def average(numbers:list):
  sum = 0
  for n in numbers:
    sum += n
  return sum / len(numbers)

avg = average([11,4,22,43,5,8,77])

print(f'The arithmetic average is: {avg:.2f}')
