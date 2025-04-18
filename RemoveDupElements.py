def removeDuplicates(arr):
    if not arr:
        return 0  # if array is empty

    j = 0  # Start with the first element

    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    return j + 1  # Total number of unique elements

# Test array
arr = [1, 2, 2, 3, 3, 4]

# Call the function
new_length = removeDuplicates(arr)

# Print the results
print(new_length)
print(arr[:new_length])
