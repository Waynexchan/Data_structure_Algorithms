'''
https://chatgpt.com/c/108ba053-e224-4887-b474-1c20f32191c6
'''

# class Solution(object):
#     def firstUniqChar(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         seen_freq = {}
#         for char in s:
#             if char in seen_freq:
#                 seen_freq[char] += 1
#             else:       
#                 seen_freq[char] = 1

#         for i in range(0, len(s)):
#             if seen_freq[s[i]] == 1:
#                 return i
#         return -1
            
# s = "leetcode"
# solution = Solution()
# print(solution.firstUniqChar(s))

'''
from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter(s)
        
        # 找到第一个只出现一次的字符
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        
        return -1

s = "leetcode"
solution = Solution()
print(solution.firstUniqChar(s))
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        unique_set = set()
        repeat_set = set()

        for char in s:
            if char in unique_set:
                repeat_set.add(char)
            else:
                unique_set.add(char)
        
        for i, char in enumerate(s):
            if char not in repeat_set:
                return i
s = "loveleetcode"
solution = Solution()
print(solution.firstUniqChar(s))    