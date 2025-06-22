class Solution:
    def relativeSortArray(self, arr1, arr2):
        order = {num: index for index, num in enumerate(arr2)}
        return sorted(arr1, key=lambda x: (order.get(x, len(arr2) + x), x))
