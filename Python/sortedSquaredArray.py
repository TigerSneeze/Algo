"""
return the sorted squared array
"""

def sortedSquaredArray(array):
	for a in array:
		array[array.index(a)] = a**2
    return sorted(array)
