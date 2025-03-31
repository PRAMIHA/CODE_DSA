def rotate_clockwise(arr):
    if len(arr) > 1:  # Step 1: Check if array has more than 1 element
        last_element = arr[-1]  # Step 2: Store last element

        for i in range(len(arr) - 1, 0, -1):  # Step 3: Loop from last to first
            arr[i] = arr[i - 1]  # Step 4: Shift elements right
        
        arr[0] = last_element  # Step 5: Place last element at front

# Example usage
arr = [1, 2, 3, 4, 5]
rotate_clockwise(arr)
print(arr)  # Output: [5, 1, 2, 3, 4]
