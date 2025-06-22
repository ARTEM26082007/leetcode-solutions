class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                # Возвращаем индексы с +1, так как вход 1-индексирован
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1
