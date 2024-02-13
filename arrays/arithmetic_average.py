from functools import reduce

def average(numbers:list):
  # sum = 0
  # for n in numbers:
  #   sum += n
  # return sum / len(numbers)
  avg = reduce(lambda x, y: x+y, numbers)
  return avg / len(numbers)

avg = average([2,2,1,44,73,54,14])

print(f'The arithmetic average is: {avg:.2f}')
