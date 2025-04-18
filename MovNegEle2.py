def moveNegativesToEnd(arr):
    n = len(arr)
    j = 0  # Index for placing the next non-negative number

    # Step 1: Move non-negative numbers to the front
    for i in range(n):
        if arr[i] >= 0:
            arr[j] = arr[i]
            j += 1
   

    # Step 2: Move negative numbers to the end
    for i in range(n):
        if arr[i] < 0:
            arr[j] = arr[i]
            j += 1


# Example usage:
arr = [1, -2, 3, -4, 5, -6]
moveNegativesToEnd(arr)
print(arr)  # Output: [1, 3, 5, -2, -4, -6]
