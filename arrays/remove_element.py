def remove_element(numbers:list, target:int):
  for num in numbers:
    if num == target:
      numbers.remove(target)
      return numbers
  return 'The number is not present.'

res = remove_element([1,4,2,5,3], 7)
print(res)