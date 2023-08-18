"""
Given an array of integers, find and return the largest difference between two elements such that the smaller 
element precedes the larger element.

Input:
arr = [7, 9, 5, 6, 3, 2]

output: 2

Explanation :The largest difference where the smaller number comes before the larger number is
between 7 and 9 (9-7 = 2).
"""

def largest_preceding_difference(arr):
    if len(arr) < 2:
        return 0  # If there are less than 2 elements, the difference is 0
    
    min_val = arr[0]
    max_diff = 0
    
    for num in arr:
        max_diff = max(max_diff, num - min_val)
        min_val = min(min_val, num)
    
    return max_diff

arr = [7, 9, 5, 6, 3, 2]
output = largest_preceding_difference(arr)
print(output)  # Output: 2
