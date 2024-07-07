class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        answer = []
        for i in range (len(s)-1, -1, -1):
            answer.append(s[i])

        return answer

s = ["h","e","l","l","o"]
solution = Solution()
print(solution.reverseString(s))