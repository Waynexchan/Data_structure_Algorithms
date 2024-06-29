# def first_recurring(arr):
#     complements = []
#     for i in range(len(arr)):
#         if arr[i] in complements:
#             return arr[i]
#         complements.append(arr[i])
#     return "undefined"

array = [2,5,5,1,2,3,5,1,2,4]
# result = first_recurring(array)
# print(result)

# def first_recurring_set(arr):
#     complements = set()
#     for i in range(len(arr)):
#         if arr[i] in complements:
#             return arr[i]
#         complements.add(arr[i])
#     return "undefined"

# result = first_recurring_set(array)
# print(result)

def first_recurring_dict(arr):
    complements = {}
    for i in range(len(arr)):
        if arr[i] in complements:
            return arr[i]
        complements[arr[i]] = True
    return "undefined"

result = first_recurring_dict(array)
print(result)

def native_frc(arr):
    l = len(arr)
    i = 0
    frc = None
    while (i < l):
        j = i + 1
        while (j < l):
            if arr[i] == arr[j]:
                l = j
                frc = array[j]
                continue
            else:
                j+=1
        i += 1
    return frc

print(native_frc(array))