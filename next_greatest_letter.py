class Solution:
    def nextGreatestLetter(self, letters, target):
        left, right = 0, len(letters) - 1

        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        # Если left вышел за границы, возвращаем первый элемент
        return letters[left] if left < len(letters) else letters[0]
