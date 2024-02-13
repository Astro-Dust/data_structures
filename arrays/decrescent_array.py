def decres_array(numbers:list):
  numbers.sort(reverse=True)
  return numbers

res = decres_array([1,4,2,5,6,3,5])

print(res)