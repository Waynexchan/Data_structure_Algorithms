'''
https://leetcode.com/problems/majority-element/
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        # verify
        count = 0
        for num in nums:
            if num == candidate:
                count +=1

        if count > (len(nums)//2):
            return candidate
        else:
            return None

nums = [3,2,3]
solution = Solution()
print(solution.majorityElement(nums))    
        