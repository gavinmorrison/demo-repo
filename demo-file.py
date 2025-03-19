#!/usr/bin/env python3

def sum_of_evens(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

# Test the function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Sum of even numbers:", sum_of_evens(numbers))
