"""
Objective: Implement an algorithm to count the number of prime numbers in an integer array.

Background: A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. 
For example, 5 is prime because the only ways to write it as a product, 1 × 5 or 5 × 1, involve 5 itself.

Input: arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]

Output: 4

Explanation: The prime numbers in the array are [2, 3, 5, 7].
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_prime_numbers(arr):
    count = 0
    for num in arr:
        if is_prime(num):
            count += 1
    return count

# Example input
arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]
output = count_prime_numbers(arr)
print(output)  # Output: 4
