#https://www.geeksforgeeks.org/problems/move-all-negative-elements-to-end1813/1
class Solution:
    def segregateElements(self, arr):
        n = len(arr)
        temp = []

        # Collect non-negative numbers
        for i in range(n):
            if arr[i] >= 0:
                temp.append(arr[i])

        # Collect negative numbers
        for i in range(n):
            if arr[i] < 0:
                temp.append(arr[i])

        # Copy the result back to the original array
        for i in range(n):
            arr[i] = temp[i]
          
