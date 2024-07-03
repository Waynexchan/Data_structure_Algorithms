numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def insertionSort(array):
    for i in range(1, len(array)):
        
        key = array[i]
        j = i-1
        # move right handside
        while j >= 0 and key < array[j]:
            array[j+1] = array[j] 
            j -= 1
        # insert key
        array[j+1] = key
    return array


print(insertionSort(numbers))