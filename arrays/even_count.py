def find_even(numbers:list):
  even_count = 0
  for n in numbers:
    if n%2 == 0:
      even_count += 1
  return even_count

res = find_even([1,3,2,7,8,4,10])

print(f'There are {res} even numbers.')