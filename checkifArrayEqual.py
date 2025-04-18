class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True
