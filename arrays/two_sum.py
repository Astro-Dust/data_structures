#Given an array of integers nums and an 
#integer target, return indices of the two numbers
#such that they add up to target.

#Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


def two_sum(nums:list, target:int):
  
  # esses dois "for" lembra daquele exercicio do Fabio sobre selection sort
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if nums[i] + nums[j] == target:
        return [i , j]
  
  return []
    
result = two_sum([3,1,5,8,9,2], 9)

print(result)