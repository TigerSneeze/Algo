#Insertion sort
test_array = list(range(7))
# test_array = [1,2,2,2,6,4]
random.shuffle(test_array)
print(test_array)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        check = arr[i]
        for j in reversed(range(i)):
            if check < arr[j]:
                arr[j], arr[j+1] = check, arr[j]
            else:
                break
    return arr

insertion_sort(test_array)
