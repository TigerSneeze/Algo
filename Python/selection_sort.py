def selectionSort(arr):
    for i in range(len(arr)-1):
        min_ind = i
        for j in range(i , len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        if i != min_ind:
            arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr

sorted_array = selectionSort(test_array)
