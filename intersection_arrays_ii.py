from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        result = []

        for num in count1:
            if num in count2:
                times = min(count1[num], count2[num])
                result.extend([num] * times)
        return result
