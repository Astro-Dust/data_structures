
# verificando se UM ARRAY é o mesmo de trás pra frente
def is_palindrome(numbers:list):
  return numbers == numbers[::-1]

res1 = is_palindrome([1,2,3])
res2 = is_palindrome([1,2,3,2,1])

print(f'Is the 1st a palindrome? {res1}')
print(f'Is the 2nd a palindrome? {res2}')