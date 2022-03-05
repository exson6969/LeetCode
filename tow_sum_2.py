class Solution:
    def twoSum2(self, numbers: [int], target:int) -> [int]:
        l,r = 0, len(numbers)-1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l +=1
            else:
                return[l+1, r+1]
        return []
p1 = Solution()
print(p1.twoSum2([2,7,11,15], 9))
