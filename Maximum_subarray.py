class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum <0:
                curSum = 0
            curSum +=n
            maxSub = max(maxSub, curSum)
        return maxSub

p1 = Solution()
print(p1.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) #6
