class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target -n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
p1 = Solution()
print(p1.twoSum([2,7,11,15], 9)) # [0,1]
