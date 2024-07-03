numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def mergeSort(array):
    if len(array) == 1 : #Stop point
        return array
    
    #find the mid point and divide in two parts by using recursion
    mid = len(array)//2
    left_half = mergeSort(array[:mid])
    right_half = mergeSort(array[mid:])
    
    return merge(left_half, right_half) #sort and combine

def merge(left, right):
    result=[]
    i = j = 0

    #while loop to append the smaller item
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    #Extend the remaining part from left or right after the while loop
    result.extend(left[i:])
    result.extend(right[j:])

    return result



answer = mergeSort(numbers)
print(answer)