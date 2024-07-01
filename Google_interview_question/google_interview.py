def bad_nested_solution(arr, target_value):
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if arr[i] + arr[j] == target_value:
				return "Yes"
	return "NO"

# O(n^2)

print(bad_nested_solution(arr1, tar))

def has_pair_with_sum(arr, target_value):
	complements = set()
	
	for number in arr:
		if number in complements:
			return True
		complements.add(target_value-number)
		
	return False
	
arr1 = [1, 2, 3, 9]
arr2 = [1, 2, 4, 4]

#(O(x+y))
print(bad_nested_solution(arr1, 8))
print(bad_nested_solution(arr2, 8))


print(has_pair_with_sum(arr1, 8))
print(has_pair_with_sum(arr2, 8))