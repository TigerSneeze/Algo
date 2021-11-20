import random
test_array = list(range(7))
random.shuffle(test_array)
print(test_array)

#Bubble Sort
def bubble_sort(arr):
    length = len(arr)
    for j in range(length):
        for i in range(length-j-1):
            if arr[i] > arr[i+1]:
#                 temp = arr[i]
#                 arr[i] = arr[i+1]
#                 arr[i+1] = temp
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
bubble_sorted_array = bubble_sort(test_array)
print("bubble sorted:", bubble_sorted_array)
