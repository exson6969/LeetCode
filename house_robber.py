class Solution:
    def rob(self, nums:[int]) -> int:
        rob1, rob2 = 0,0

        for n in nums:
            temp = max(n+rob1,rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

p1 = Solution()
print(p1.rob([1,2,3,1])) #4