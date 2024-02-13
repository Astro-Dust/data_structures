def find_number(numbers:list, target:int):
  for num in numbers:
    if num == target:
      return num
    if target not in numbers:
      return 'The number is not present.'

res = find_number([42,73,22,91,60], 42)

print(res)