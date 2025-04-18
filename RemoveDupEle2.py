def removeDuplicates(arr):
    seen = set()  # Set to track unique elements
    j = 0  # Pointer to place unique elements

    # Loop through each element of the array
    for i in range(len(arr)):
        if arr[i] not in seen:
            seen.add(arr[i])  # Add the element to the set (unique elements)
            arr[j] = arr[i]   # Place unique element at index j
            j += 1  # Move j forward
    
    # Return the new length of the array with unique elements
    return j

# Example
arr = [4, 5, 4, 2, 3, 5, 1]
new_length = removeDuplicates(arr)

# Print the result
print(new_length)
print(arr[:new_length])
