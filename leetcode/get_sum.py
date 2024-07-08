class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b)  & mask
            b =carry  & mask
        

        if a > MAX:
            a = ~(a ^ mask)

        return a

# 测试
solution = Solution()
print(solution.getSum(1, 2))  # 输出: 3
print(solution.getSum(2, 3))  # 输出: 5
print(solution.getSum(-1, 1))  # 输出: 0
