array1 = ['a','b','c','x']
array2 = ['x','y','z']

def bad_solution_find_match(array1, array2):
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] == array2[j]:
                return True
    return False

# O (x*Y)

result = bad_solution_find_match(array1, array2)
print(result)

#isdisjoint method in set
def has_common_element(array1, array2):
	set1 = set (array1)
	set2 = set (array2)
	return not set1.isdisjoint(set2)
	
array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'x']

print(has_common_element(array1, array2))
# o(n+m) Time complexity

def dict_common_element(array1, array2):
    dict = {}
    for i in range(len(array1)):
        dict[array1[i]] = True

    for i in range(len(array2)):
         if array2[i] in dict:
              return True
    return False

# O(n+m), but i will use more spaces . however it is time efficient

    