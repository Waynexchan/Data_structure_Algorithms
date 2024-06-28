array1 = ['a','b','c','x']
array2 = ['x','y','z']

def bad_solution_find_match(array1, array2):
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] == array2[j]:
                return True
    return False

result = bad_solution_find_match(array1, array2)
print(result)