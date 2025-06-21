class Solution:
    def heightChecker(self, heights):
        expected = sorted(heights)
        return sum(h != e for h, e in zip(heights, expected))
