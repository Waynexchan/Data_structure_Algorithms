def mergeSortedArray(list1, list2):
    len1 = len(list1)-1
    len2 = len(list2)-1
    totalLen = len(list1) +len(list2)
    ans = [0] * totalLen
    totalLen -= 1

    if len(list1) == 0:
        return list2
    
    if len(list2) == 0:
        return list1
    

    while len1 >=0 and len2 >=0:
        if list1[len1] > list2[len2]:
            
            ans[totalLen] = list1[len1]
            len1 -= 1

        else:
            ans[totalLen] = list2[len2]
            len2 -= 1

        totalLen -= 1

    while len1 >=0:
        ans[totalLen] = list1[len1]
        len1 -= 1
        totalLen -= 1

    while len2 >=0:
        ans[totalLen] = list2[len2]
        len2 -= 1
        totalLen -= 1

    return ans

list1 = [0,3,4,31] 
list2 = [4,5,30]

result = mergeSortedArray(list1, list2)
print(result)


def mergeSortArray3(list1, list2):
    mergeArray = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            mergeArray.append(list1[i])
            i += 1
        else:
            mergeArray.append(list2[j])
            j += 1

    while i < len(list1):
        mergeArray.append(list1[i])
        i +=1

    while j < len(list2):
        mergeArray.append(list2[j])
        j +=1

    return mergeArray

list1 = [0,3,4,31] 
list2 = [4,5,30]

result = mergeSortArray3(list1, list2)
print(result)

def mergeSortedArray2(list1, list2):
    merged_list = []
    for i in range(len(list1)):
        merged_list.append(list1[i])
    
    for j in range(len(list2)):
        # 將 list2[j] 插入 merged_list 中的正確位置
        inserted = False
        for k in range(len(merged_list)):
            if list2[j] < merged_list[k]:
                merged_list.insert(k, list2[j])
                inserted = True
                break
        if not inserted:
            merged_list.append(list2[j])
    
    return merged_list

list1 = [0, 3, 4, 31]
list2 = [4, 5, 30]

result = mergeSortedArray2(list1, list2)
print(result)