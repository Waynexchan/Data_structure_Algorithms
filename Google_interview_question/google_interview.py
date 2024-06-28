def has_pair_with_sum(arr, target_value):
	complements = set()
	
	for number in arr:
		if number in complements:
			return True
		complements.add(target_value-number)
		
	return False
	
arr1 = [1, 2, 3, 9]
arr2 = [1, 2, 4, 4]

print(has_pair_with_sum(arr1, 8))
print(has_pair_with_sum(arr2, 8))