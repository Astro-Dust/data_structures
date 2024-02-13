# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true

def has_duplicate(nums:list):
  seen = set() # mais otimizado (set não aceita item duplicado)

  for num in nums:
    if num in seen:
      return True
    seen.add(num)
  return False

result = has_duplicate([1,2,3,1])
print(result)
