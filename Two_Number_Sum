"""
This functions takes a non-empty integer array and an integer as the target sum
If any two elements in the array sum up to the target sum, return them in an array
"""
def twoNumberSum(array, targetSum):
  length = len(array)
  output = []
  for i in range(length):
    for j in range(i+1,length):
      sum = array[i] + array[j]
      if sum == targetSum:
        output.append(array[i])
        output.append(array[j])
        return output	
  return output
