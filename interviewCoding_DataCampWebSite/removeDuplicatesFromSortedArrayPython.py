#!/usr/local/bin/python3

def remove_duplicates(nums):
    if not nums:  # Handle empty array
        return 0

    # Pointer for the position of unique elements
    write_index = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:  # Check if current element is different from the previous
            nums[write_index] = nums[i]
            write_index += 1

    return write_index, nums[:write_index]  # Unique elements are in the first 'write_index' indices

# Example
sorted_array = [1, 1, 2, 2, 3, 4, 4, 5]
new_length, unique_array = remove_duplicates(sorted_array)
print(f"New length: {new_length}")
print(f"Unique array: {unique_array}")
