# class Solution(object):
#     def intersect(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         result = []
#         num2_copy = list(nums2)
#         for num in nums1:
#             if num in num2_copy:
#                 result.append(num)
#                 num2_copy.remove(num)
        
#         return result

# nums1 = [1,2,2,1]
# nums2 = [2,2]
# solution = Solution()
# print(solution.intersect(nums1,nums2))

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        nums1.sort()
        nums2.sort()

        i,j = 0,0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i +=1
                j += 1
        
        return result

        

nums1 = [1,2,2,1]
nums2 = [2,2]
solution = Solution()
print(solution.intersect(nums1,nums2))