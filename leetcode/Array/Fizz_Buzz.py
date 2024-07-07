class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == -0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans

n = 15
solution = Solution()
print(solution.fizzBuzz(n))

# Time Complexity O(n)
# Space Complexity O(n)