class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in nums:
            result ^= i
        return result
        
nums = [2,2,1]
solution = Solution()
print(solution.singleNumber(nums))


# Time Complexity O(n)
# Space Complexity O (1)
        

'''
異或操作的特性：
任何數字與自身異或結果為0： 
𝑎
⊕
𝑎
=
0
a⊕a=0
任何數字與0異或結果為自身： 
𝑎
⊕
0
=
𝑎
a⊕0=a
異或操作具有交換性和結合性：
𝑎
⊕
𝑏
=
𝑏
⊕
𝑎
a⊕b=b⊕a 和 
(
𝑎
⊕
𝑏
)
⊕
𝑐
=
𝑎
⊕
(
𝑏
⊕
𝑐
)
(a⊕b)⊕c=a⊕(b⊕c)
應用這些特性：
當你將所有數字依次進行異或操作時，成對出現的數字會互相抵消為0，只有那個只出現一次的數字會留下來。

具體例子：
考慮數組 [2, 1, 4, 2, 1]，我們逐步進行異或操作：

初始化：

result = 0
遍歷數組：

result = 0 \oplus 2 = 2
result = 2 \oplus 1 = 3
result = 3 \oplus 4 = 7
result = 7 \oplus 2 = 5
result = 5 \oplus 1 = 4
在每一步中：

第一次遇到2， result 變成2。
第一次遇到1， result 變成3（即2 \oplus 1）。
第一次遇到4， result 變成7（即3 \oplus 4）。
第二次遇到2， result 變成5（即7 \oplus 2，因為2 \oplus 2 = 0，然後7 \oplus 0 = 7，所以最終變成7 \oplus 2 = 5）。
第二次遇到1， result 變成4（即5 \oplus 1，因為1 \oplus 1 = 0，然後5 \oplus 0 = 5，所以最終變成5 \oplus 1 = 4）。
最後， result 的值是4，這就是數組中唯一沒有被抵消的數字，即唯一只出現一次的數字。
'''