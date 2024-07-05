numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def SelectionSort(array):
    
    
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:               
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
        
    
    return array
#O(n^2)
        
        


print(SelectionSort(numbers))