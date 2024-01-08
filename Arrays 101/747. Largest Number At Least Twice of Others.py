class Solution:
    def dominantIndex(self, nums) -> int:
        maxVal= max(nums)
        maxIndex = nums.index(maxVal)
        for num in nums:
            if maxVal < num*2 and num!=maxVal:
                return -1
        return maxIndex