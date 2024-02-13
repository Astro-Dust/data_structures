
# função que une 2 arrays e também evita números repetidos
def array_union(arr1:list, arr2:list):
  org_array = set()
  united = arr1 + arr2
  for n in united:
    org_array.add(n)
  return org_array

res = array_union([1,2,3], [3,4,4,5,6])
print(res)