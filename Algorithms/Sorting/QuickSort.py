def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)
    return array

def quick_sort_helper(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort_helper(array, low, pivot_index - 1)
        quick_sort_helper(array, pivot_index + 1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
result = quick_sort(numbers)
print(result)