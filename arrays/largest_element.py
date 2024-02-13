from functools import reduce

def largest_element(numbers:list):
  largest = reduce(lambda x,y: x if x > y else y, numbers)
  return largest

res = largest_element([13,35,22,58,61,2])

print(f'Largest element: {res}')