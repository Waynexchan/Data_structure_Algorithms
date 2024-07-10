# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        compliments = {}
        for i in range(len(nums)):
            if nums[i] in compliments:
                return True
            else:
                compliments[nums[i]] = True
        print("No Duplicate Num")

nums = [1,2,3,1]
solution = Solution()
result = solution.containsDuplicate(nums)
print(result)


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
       
        seen_freq = {}
        for i in nums:
            if i in seen_freq:
                return True
            else:
                seen_freq[i] = 1
        return False

nums = [1,2,3,1]
solution = Solution()
result = solution.containsDuplicate(nums)
print(result)