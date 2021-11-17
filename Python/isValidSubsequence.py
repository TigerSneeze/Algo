"""
check whether array is a subsequence of sequence (order sensitive)
"""

def isValidSubsequence(array, sequence):
    # Write your code here.
	new_first_index = 0
	result = True
	for s in sequence:
		if s in array:
			new_first_index = array.index(s) + 1
			array = array[new_first_index:]
		else:
			return False	
	return result
