class Solution:
    def twoSum(self, nums, target):
        seen = {}  # словарь для хранения числа и его индекса
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
