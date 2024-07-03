numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                
                array[j], array[j+1] = array[j+1], array[j]
                
    return array
                
print(bubblesort(numbers))